from flask import Blueprint, g, request, Response, jsonify, stream_with_context
from app.web.hooks import login_required, load_model
from app.db.model import File as Pdf, Conversation
from app.rag.chat import build_chat
from app.rag.shared.models import ChatArgs

bp = Blueprint("conversation", __name__, url_prefix="/api/conversations")


@bp.route("/", methods=["GET"])
@login_required
@load_model(Pdf, lambda r: r.args.get("file_id"))
def list_conversations(file):
    return [c.as_dict() for c in file.conversations]


@bp.route("/", methods=["POST"])
@login_required
@load_model(Pdf, lambda r: r.args.get("file_id"))
def create_conversation(file):
    conversation = Conversation.create(user_id=g.user.id, file_id=file.id)

    return conversation.as_dict()


@bp.route("/<string:conversation_id>/messages", methods=["POST"])
@login_required
@load_model(Conversation)
def create_message(conversation):
    input = request.json.get("input")
    streaming = request.args.get("stream", False)

    file = conversation.file

    chat_args = ChatArgs(
        conversation_id=conversation.id,
        file_id=file.id,
        streaming=streaming,
        metadata={
            "conversation_id": conversation.id,
            "user_id": g.user.id,
            "file_id": file.id,
        },
    )

    chat = build_chat(chat_args)

    if not chat:
        return "Chat not yet implemented!"

    if streaming:
        return Response(
            stream_with_context(chat.stream(input)), mimetype="text/event-stream"
        )
    else:
        return jsonify({"role": "assistant", "content": chat.run(input)})
