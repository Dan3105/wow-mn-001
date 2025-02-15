from flask import Blueprint, g, jsonify
from werkzeug.exceptions import Unauthorized
from app.web.hooks import login_required, handle_file_upload, load_model
from app.db.model import File as Pdf
# from app.tasks.embeddings import process_document
from app.web import files

bp = Blueprint("file", __name__, url_prefix="/api/files")


@bp.route("/", methods=["GET"])
@login_required
def list():
    files = Pdf.where(user_id=g.user.id)

    return Pdf.as_dicts(files)


@bp.route("/", methods=["POST"])
@login_required
@handle_file_upload
def upload_file(file_id, file_path, file_name):
    res, status_code = files.upload(file_path)
    if status_code >= 400:
        return res, status_code

    file = Pdf.create(id=file_id, name=file_name, user_id=g.user.id)

    # TODO: Defer this to be processed by the worker (by using delay)
    # process_document.delay(file.id)

    return file.as_dict()


@bp.route("/<string:file_id>", methods=["GET"])
@login_required
@load_model(Pdf)
def show(file):
    return jsonify(
        {
            "file": file.as_dict(),
            "download_url": files.create_download_url(file.id),
        }
    )
