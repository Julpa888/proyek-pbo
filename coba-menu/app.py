from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def menu():
    return render_template("menu.html")

@app.route("/jadwal")
def jadwal():
    data = [
        {"hari": "Senin", "jam": "16.00", "mapel": "Matematika"},
        {"hari": "Rabu", "jam": "16.00", "mapel": "Fisika"},
    ]
    return render_template("jadwal.html", jadwal=data)

if __name__ == "__main__":
    app.run(debug=True)