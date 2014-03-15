from flask import Flask, render_template, redirect, session, url_for, request
import lis

app = Flask(__name__)
app.secret_key = "thisisasecret"

@app.route("/")
def index():
    html = render_template("index.html")
    return html




if __name__ == "__main__":
    app.run(debug=True)