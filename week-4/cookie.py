from flask import Flask, render_template, request, redirect, url_for, make_response
from cryptography.fernet import Fernet
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
key = Fernet.generate_key()
f=Fernet(key)


@app.route("/signin",methods=["POST"])
def signIn():
    account = request.form["acc"]
    password = request.form["pass"]
    if account == "test" and password == "test":
        res = make_response(redirect("/member"))
        valueT = f.encrypt(b"True")
        res.set_cookie(key="login", value=valueT)
        return res
    elif account == "" or password == "":
        return redirect(url_for("error",message=["請輸入帳號、密碼"]))
    return redirect(url_for("error",message=["帳號、或密碼輸入錯誤"]))

@app.route("/signout")
def signOut():
    res = make_response(redirect("/"))
    res.set_cookie(key="login", expires=0)
    return res

@app.route("/member")
def member():
    login = request.cookies.get("login")
    try:
        loginValue = f.decrypt(login).decode("ascii")
        if loginValue == "True":
            return render_template("member.html")
    except:
        return redirect("/")

@app.route("/error")
def error():
    return render_template("error.html", showMessage=request.args.get("message"))

@app.route("/square/<int:number>")
def square(number):
        return render_template("square.html", answer = number**2)

app.run(port=3000)