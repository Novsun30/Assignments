from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key="You know nothing, Jon Snow"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin",methods=["POST"])
def signIn():
    account = request.form["acc"]
    password = request.form["pass"]
    if account == "test" and password == "test":
        res = make_response(redirect("/member"))
        res.set_cookie(key="login", value="True")
        return res
    elif account == "" or password == "":
        return redirect(url_for("error",message=["請輸入帳號、密碼"]))
    return redirect(url_for("error",message=["帳號、或密碼輸入錯誤"]))

@app.route("/signout")
def signOut():
    res = make_response(redirect("/"))
    res.set_cookie(key="login", value="False")
    return res

@app.route("/member")
def member():
    login = request.cookies.get("login")
    if login == "True":
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/error")
def error():
    return render_template("error.html", showMessage=request.args.get("message"))

@app.route("/square/<int:number>")
def square(number):
        return render_template("square.html", answer = number**2)

app.run(port=3000)