from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key="You know nothing, Jon Snow"

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/signin",methods=["POST"])
def signIn():
    account = request.form["acc"]
    password = request.form["pass"]
    if account == "test" and password == "test":
        session["login"]=True
        return redirect("/member")
    elif account == "" or password == "":
        return redirect(url_for("error",message=["請輸入帳號、密碼"]))
    return redirect(url_for("error",message=["帳號、或密碼輸入錯誤"]))

@app.route("/signout")
def signOut():
    session['login'] = False
    return redirect("/")

@app.route("/member")
def member():
    try:
        if session["login"] == True:
            return render_template("member.html")
        elif session["login"] == False:
            return redirect("/")
        elif session["login"] == True:
            return redirect("/square/6")
    except:
        return redirect("/")
    


@app.route("/error")
def error():
    return render_template("error.html", showMessage=request.args.get("message"))

@app.route("/square/<int:number>")
def square(number):
        return render_template("square.html", answer = number**2)

app.run(port=3000)