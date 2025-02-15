from app.web.hooks import login_required
from flask import Blueprint, request, send_file, jsonify
from werkzeug.utils import secure_filename
from app.config import Config
import os

bp = Blueprint("upload", __name__, url_prefix="/upload")

ALLOWED_EXTENSIONS = {"file"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route("/", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"message": "No file part in the request"}, 400)
    file = request.files["file"]

    if file.filename == "":
        return jsonify({"message": "No selected file"}, 400)
    if file:
        filename = secure_filename(file.filename)
        print(filename)
        file.save(os.path.join(Config.UPLOAD_FOLDER, filename))
        return jsonify({"message": f"File {filename} uploaded successfully"}, 200)
    else:
        return jsonify({"message": "File type not allowed"}, 400)


@bp.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
    if os.path.exists(filepath):
        return send_file(filepath, as_attachment=False, mimetype="application/file")
    else:
        return jsonify({"message": "File not found"}, 404)