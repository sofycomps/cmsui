from flask import Flask, jsonify, render_template

app = Flask(__name__, static_url_path="/static", static_folder="static")


@app.route("/")
def main():
    return render_template("base.html")

@app.route("/a")
def maina():
    return render_template("home.html")

# wereq
if __name__ == "__main__":
    app.run("0.0.0.0", "3005")
