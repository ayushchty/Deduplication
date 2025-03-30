from flask import Flask, render_template, request, send_file
from load import FileChecker  
from dedupe import Dedupe  
import os
import pandas as pd

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file.filename == "":
            return render_template("index.html", error="No file selected!")

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        file_loader = FileChecker(filepath)
        df = file_loader.get_dataframe()  

        deduper = Dedupe(df)
        cleaned_df, duplicate_count = deduper.word_match_ayush()  
        cleaned_df = deduper.remove()  
        cleaned_filepath = os.path.join(UPLOAD_FOLDER, "cleaned_" + file.filename)
        cleaned_df.to_csv(cleaned_filepath, index=False)

        return render_template(
            "index.html",
            duplicate_count=duplicate_count,
            file_saved=True,
            cleaned_filepath="cleaned_" + file.filename,
        )

    return render_template("index.html")

@app.route("/download/<filename>")
def download(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)


