from flask import Flask, render_template, send_from_directory
from conf import flaskconf
from os import path, listdir

app = Flask(__name__)
filespath = path.join(path.dirname(__file__), "files")
files = listdir(filespath)
print(files)

@app.route("/")
def index():
    return render_template("index.html", filesList=files)

@app.route('/<filename>')
def download(filename):
    return send_from_directory(filespath, filename)


if __name__ == "__main__":
    app.run(**flaskconf)