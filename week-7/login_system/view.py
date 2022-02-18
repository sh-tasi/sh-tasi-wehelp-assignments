from flask import Flask,Blueprint,render_template,request,redirect,url_for,session
import mysql.connector

login_system = Blueprint('login_system', __name__, template_folder= 'templates/login_system' )


@login_system.route('/',methods=["GET","POST"])

def signin():
    mydb = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='qweasdzxc',
    database='website'
    )
    mycursor = mydb.cursor()
    username=request.form["username"]
    password=request.form["password"]
    if len(username)==0 or len(password)==0 or username.isspace()==True or password.isspace()==True:
        login_error01="請輸入帳號或密碼"
        mycursor.close()  
        mydb.close()     
        return redirect(url_for('login_system.message',error=login_error01))
    sql="SELECT `name`,`password` FROM `member` WHERE `username` = %s  "
    username_sql=(username,)
    mycursor.execute(sql,username_sql)
    myresult=mycursor.fetchone()
    print(myresult)
    if myresult==[]:
        login_error02="帳號或密碼錯誤，請重新輸入"  
        mycursor.close()  
        mydb.close()      
        return redirect(url_for('login_system.message',error=login_error02))
    else:
        member_user=myresult[0]
        member_password=myresult[1]
        print(member_user)  
        print(member_password) 
        if password==member_password: 
            session["name"]=member_user
            session["username"]=username
            print(session["username"])
            mycursor.close()  
            mydb.close()   
            return redirect(url_for('member'))
        else:
            login_error03="密碼錯誤，請重新輸入"     
            mycursor.close()  
            mydb.close()   
            return redirect(url_for('login_system.message',error=login_error03)) 
@login_system.route("/message/")
def message():
    
    error=request.args.get("error",None)
    return render_template("message.html",error=error)   
@login_system.route("/signout")
def signout():
    session.pop('username',None)
    session.pop('name',None)
    return redirect("/")