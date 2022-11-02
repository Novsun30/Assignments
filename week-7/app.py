from flask import Flask, render_template, request, Response, redirect, session, url_for
import mysql.connector, re, json

app = Flask(__name__)
app.secret_key = "!!xxx YOU SHALL NOT PASS xxx!!"
cnx = mysql.connector.connect(host = "127.0.0.1", user = "root",  password = "1234", database = "website") 

@app.route("/api/member", methods=["GET", "PATCH"])
def api_member():
    if request.method == "GET":
        get_username = request.args.get("username")
        with cnx.cursor() as cursor:
            search_username = "SELECT id, name, username FROM member WHERE username = %s"
            cursor.execute(search_username, (get_username,))
            data = cursor.fetchone()
            if data != None:
                data = {
                    "data":{
                        "id": data[0],
                        "name": data[1],
                        "username": data[2]
                    }
                }
                result = Response(json.dumps(data, ensure_ascii = False), mimetype = "application/json")
                return result
        data = {"data":None}
        result = Response(json.dumps(data))
        return result
    if request.method == "PATCH":
        data = request.get_json()["name"].strip()
        if re.search("[^ \w]", data) or data == "":
            result = Response(json.dumps({"error":True}))
            return result
        with cnx.cursor() as cursor:
            update_name = "UPDATE member SET name = %s WHERE name = %s"
            cursor.execute(update_name,(data, session["name"]))
            cnx.commit()
        session["name"] = data
        result = Response(json.dumps({"ok":True}))
        return result


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=["POST"])
def sign_up():
    name = request.form["name"].strip()
    account = request.form["account"].strip()
    password = request.form["password"].strip()
    if re.search("[^ \w]", name) or name == "":
        return redirect(url_for("error", message = "姓名不能包含特殊符號(除了空格與底線)"))
    if re.search("[^a-zA-Z0-9]", "{}{}".format(account, password)):
        return redirect(url_for("error", message = "帳號、密碼只能由英文字母大小寫以及數字組成"))
    with cnx.cursor() as cursor:
        check_username = ("SELECT username FROM member WHERE username = %s")
        cursor.execute(check_username, (account,))
        accData = cursor.fetchone()
        if accData != None :
            return redirect(url_for("error", message = "帳號已經被註冊"))
    with cnx.cursor() as cursor:
        new_member = ("INSERT INTO member (name, username, password)VALUES(%s,%s,%s)")
        member_data = (name, account, password)
        cursor.execute(new_member, member_data)
        cnx.commit()
    return redirect("/")

@app.route("/signin", methods=["POST"])
def sign_in():
    account = request.form["account"]
    password = request.form["password"]
    with cnx.cursor() as cursor:
        check_account = ("SELECT id, name, username, password FROM member WHERE username = %s AND password = %s ")
        cursor.execute(check_account, (account, password))
        member_data = cursor.fetchone()
        if member_data != None:
            session["login"] = True
            session["id"] = member_data[0]
            session["name"] = member_data[1]                
            return redirect("/member")
    return redirect(url_for("error", message = "帳號或密碼輸入錯誤"))

@app.route("/signout")
def sign_out():
    session.pop("login")
    session.pop("id")
    session.pop("name")
    return redirect("/")

@app.route("/error")
def error():
    return render_template("error.html", message = request.args.get("message"))

@app.route("/member")
def memeber():
    if session.get("login") == True:
        with cnx.cursor() as cursor:
            show_message = "SELECT member.name, member.username, message.content, message.time From member INNER JOIN message ON member.id = message.member_id ORDER BY message.time"
            cursor.execute(show_message)
            message_data = cursor.fetchall()                        
        return render_template("member.html", show_name = session["name"], message = message_data  )
    return redirect("/")

@app.route("/message", methods = ["POST"])
def message():
    message = request.form["message"]
    if len(message) > 250:
        return redirect(url_for("error", message = "字數需在250字以內"))
    with cnx.cursor() as cursor:
        add_message = ("INSERT INTO message( member_id, content )VALUES( %s, %s )") 
        message_data = (session["id"], message)
        cursor.execute(add_message, message_data)
        cnx.commit()
    return redirect("/member")

app.run(port = 3000, debug = True)