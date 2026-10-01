from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # TODO: sambungkan ke models/user.py (User.login()) dan database asli
        print(f"Login dicoba: {username} / {password}")
        return redirect("/")
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)