from flask import Flask
from flask import render_template, request, send_from_directory, redirect
import os
from werkzeug.utils import secure_filename
from rembg import remove


app = Flask(__name__)

app.secret_key = "scr"

STATIC_FOLDER = "static"
app.config["S_FOLDER"] = STATIC_FOLDER

@app.route("/")
def hello_world():

    return render_template("main.html")


@app.route("/fi", methods=["POST"])
def filee():
    if request.method == "POST":
        fileee = request.files["hfile"]

        file_name = fileee.filename
        file_path = os.path.join(f"{app.config["S_FOLDER"]}/upload", secure_filename(file_name))

        fileee.save(file_path)

        with open(file_path, "rb") as i:
            with open(f"static/opl/{file_name}", "wb") as o:
                input = i.read()
                output = remove(input)
                o.write(output)

        return render_template("main.html", output_f=f"static/opl/{file_name}")


def servestatic():
    outputfile = ""
    send_from_directory(app.config["S_FOLDER"], outputfile)
    pass


if __name__ == "__main__":
    app.run(debug=True)