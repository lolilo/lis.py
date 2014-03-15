from flask import Flask, render_template, redirect, session, url_for, request
import lis

app = Flask(__name__)
app.secret_key = "thisisasecret"

# asks user to input Scheme code
@app.route("/")
def index():
    html = render_template("index.html")
    return html

@app.route("/", methods=["POST"])
def code_submitted():
    user_input = request.form.get("user_input")
    print user_input
    if user_input:
        json_object = lis.return_json(user_input)
        print json_object
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)