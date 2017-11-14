from flask import Flask, jsonify, render_template

app = Flask(__name__, static_url_path="/static", static_folder="static")


@app.route("/")
def main():
    return render_template("base.html")
	
@app.route("/a")
def maina():
    return render_template("home.html")

@app.route("/accounts")
def accounts():
    return render_template("accounts.html")
	
@app.route("/partnersList")
def partnersList():
    return render_template("partnersList.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/docedit")
def docedit():
    return render_template("docedit.html")

@app.route("/documentList")
def documentList():
    return render_template("documentList.html")
	
@app.route("/partnerInfo")
def partnerInfo():
    return render_template("partnerInfo.html")
		
@app.route("/userInfo")
def userInfo():
    return render_template("userInfo.html")

@app.route("/docView2")
def docView2():
    return render_template("docView2.html")

@app.route("/docView")
def docView():
    return render_template("docView.html")


	
# wereq
if __name__ == "__main__":
    app.run("0.0.0.0", 3005, debug=True)	

