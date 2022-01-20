from threading import activeCount
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
app=Flask(
    __name__,
    static_folder="static",          #對應資料夾
    static_url_path="/static"        #對應網址路徑
)
app.secret_key="123456789"
@app.route("/")                      #首頁路徑
def index():                         #首頁
    # print("請求方法",request.method)
    # print("通訊協定",request.scheme)
    # print("主機名稱",request.host)
    # print("路徑",request.path)
    # print("完整的網址",request.url)
    # print("瀏覽器和作業系統",request.headers.get("user-agent"))
    # print("語言偏好",request.headers.get("accept-language"))
    # print("引薦網址",request.headers.get("referrer"))
    # return redirect(網址路徑)
    # return "Hello Flask"
    if session["username01"]==True:
        return redirect("/member")
    else:    
        return render_template("index.html")
@app.route("/signin",methods=["GET","POST"])
def signin():
    # data=request.args.get("參數","預設值")
    account=request.form["account"]
    pw=request.form["pw"]
    if account=="test" and pw =="test":
        session["username01"]=True
        return redirect("/member")
    elif account.isspace()==True or pw.isspace()==True or len(account)==0 or len(pw)==0:  
        error01="請輸入帳號密碼"     
        return redirect(url_for('message',error=error01))
    else:
        error02="帳號或密碼輸入錯誤"
        return redirect(url_for('message',error=error02))
 
@app.route("/member",methods=["GET","POST"])
def member():
    if session["username01"]==True:
        return render_template("member.html")
    else:
        return redirect("/")
@app.route("/message/")
def message():
    error=request.args.get("error",None)
    return render_template("message.html",error=error)
#可透過port 參數指定埠號
@app.route("/signout")
def signout():
    session["username01"]=False        
    return redirect("/")
app.run(port=3000)