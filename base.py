from flask import Flask, render_template, request

app = Flask(__name__)


# # Load Flask configurations from config.py
# app.secret_key = app.config["SECRET_KEY"]
# app.config.from_object("config")


@app.route("/")
def hello_world():
    return "Hello world!"


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/data/", methods=["POST", "GET"])
def data():
    if request.method == "GET":
        return (
            f"The URL /data is accessed directly. Try going to '/form' to submit form"
        )
    if request.method == "POST":
        form_data = request.form
        return render_template("data.html", form_data=form_data)


app.run(host="localhost", port=8000, debug=True)
