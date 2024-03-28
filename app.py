# app.py
from flask import Flask, request, render_template, redirect, url_for
import base64
import random
import string

app = Flask(__name__, static_folder="static")


def generate_random_string(length):
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=length))


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        base64_img = request.form.get("image")
        img_data = base64.b64decode(base64_img.split(",")[1])
        filename = generate_random_string(10)
        with open(f"static/{filename}.png", "wb") as f:
            f.write(img_data)
        return redirect(url_for("static", filename=f"{filename}.png"))
        return "Image uploaded successfully"
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
