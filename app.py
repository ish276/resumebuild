from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "email": request.form["email"],
            "phone": request.form["phone"],
            "address": request.form["address"],
            "career": request.form["career"],
            "education": request.form["education"],
            "skills": request.form["skills"],
            "projects": request.form["projects"],
            "experience": request.form["experience"],
            "certificates": request.form["certificates"]
        }

        return render_template("resume.html", data=data)

    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)