from flask import Flask, render_template, request, redirect, session, url_for
import mysql.connector, re

app = Flask(__name__)
app.secret_key = "!!xxx YOU SHALL NOT PASS xxx!!"
cnx = mysql.connector.connect(host = "127.0.0.1", user = "root",  password = "1234", database = "website") 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    acc = request.form["account"]
    psword = request.form["password"]
    if re.search("[^ \w]", name):
        return redirect(url_for("error", message = "姓名不能包含特殊符號(除了空格與底線)"))
    if re.search("[^a-zA-Z0-9]", "{}{}".format(acc, psword)):
        return redirect(url_for("error", message = "帳號、密碼只能由英文字母大小寫以及數字組成"))
    with cnx.cursor() as cursor:
        checkUsername = ("SELECT username FROM member WHERE username = %s")
        cursor.execute(checkUsername, (acc,))
        accData = cursor.fetchone()
        if accData != None :
            return redirect(url_for("error", message = "帳號已經被註冊"))
    with cnx.cursor() as cursor:
        newMember = ("INSERT INTO member (name, username, password)VALUES(%s,%s,%s)")
        memberData = (name, acc, psword)
        cursor.execute(newMember, memberData)
        cnx.commit()
    return redirect("/")

@app.route("/signin", methods=["POST"])
def signin():
    acc = request.form["account"]
    psword = request.form["password"]
    with cnx.cursor() as cursor:
        checkAcc = ("SELECT id, name, username, password FROM member WHERE username = %s AND password = %s ")
        cursor.execute(checkAcc, (acc, psword))
        memberData = cursor.fetchone()
        if memberData != None:
            session["login"] = True
            session["id"] = memberData[0]
            session["name"] = memberData[1]                
            return redirect("/member")
    return redirect(url_for("error", message = "帳號或密碼輸入錯誤"))

@app.route("/signout")
def signout():
    session.pop("login")
    session.pop("id")
    session.pop("name")
    return redirect("/")

@app.route("/error")
def error():
    return render_template("error.html", mes = request.args.get("message"))

@app.route("/member")
def memeber():
    if session.get("login") == True:
        with cnx.cursor() as cursor:
            showMsg = "SELECT member.name, member.username, message.content, message.time From member INNER JOIN message ON member.id = message.member_id ORDER BY message.time"
            cursor.execute(showMsg)
            msgData = cursor.fetchall()                        
        return render_template("member.html", showUsername = session["name"], msg = msgData  )
    return redirect("/")

@app.route("/message", methods = ["POST"])
def message():
    msg = request.form["message"]
    if len(msg) > 250:
        return redirect(url_for("error", message = "字數需在250字以內"))
    with cnx.cursor() as cursor:
        addMsg = ("INSERT INTO message( member_id, content )VALUES( %s, %s )") 
        msgData = (session["id"], msg)
        cursor.execute(addMsg, msgData)
        cnx.commit()
    return redirect("/member")

app.run(port=3000)