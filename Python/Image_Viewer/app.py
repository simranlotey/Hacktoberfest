from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = ""  # path to pic folder

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_directory = request.form.get("image_directory")

        if os.path.exists(user_directory):
            app.config["UPLOAD_FOLDER"] = user_directory  #  set pic folder dynamic
            image_files = os.listdir(app.config["UPLOAD_FOLDER"])
            return render_template("index.html", image_files=image_files, user_directory=user_directory)
        else:
            return "The folder doesn't exists."

    return render_template("index.html", image_files=None, user_directory=app.config["UPLOAD_FOLDER"])

@app.route("/view/<image_path>")
def view_image(image_path):
    return send_from_directory(app.config["UPLOAD_FOLDER"], image_path)

if __name__ == "__main__":
    app.run(debug=True)
