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
    print(username)
    if len(username)==0 or len(password)==0 or username.isspace()==True or password.isspace()==True:
        login_error01="請輸入帳號或密碼"
        mycursor.close()  
        mydb.close()     
        return redirect(url_for('login_system.message',error=login_error01))
    sql="SELECT `name`,`username`,`password` FROM `member` WHERE `username` = %s"
    username_sql=(username,)
    mycursor.execute(sql,username_sql)
    myresult=mycursor.fetchall()
    if myresult==[]:
        login_error02="帳號錯誤或不存在，請重新輸入或註冊帳號"  
        mycursor.close()  
        mydb.close()      
        return redirect(url_for('login_system.message',error=login_error02))
    else:
        member_data=myresult[0]
        member_user=member_data[0]
        member_username=member_data[1]
        member_password=member_data[2] 
        if password==member_password:     
            session["username"]=member_user
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
    return redirect("/")