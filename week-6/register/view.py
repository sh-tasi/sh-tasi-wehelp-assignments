from flask import Flask,Blueprint,render_template,request,redirect,url_for
import mysql.connector


register = Blueprint( 'register', __name__, template_folder= 'templates/register' )


@register.route('/',methods=["GET","POST"])
def signup(): 
    mydb = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='qweasdzxc',
    database='website'
    )
    name=request.form["name"]
    username=request.form["username"]
    password=request.form["password"]
    mycursor = mydb.cursor()
    sql="SELECT `username` FROM `member` WHERE `username` = %s"
    username_sql=(username,)
    mycursor.execute(sql,username_sql)
    myresult = mycursor.fetchone()
    print(myresult)
        # error01="帳號已註冊，請重新輸入"     
        # return redirect(url_for('error01',error=error01))
    if len(name)==0 or len(password)==0 or len(username)==0 or len(username)==0 or name.isspace()==True or password.isspace()==True :
        error02="請輸入姓名&帳號&密碼"  
        mycursor.close()  
        mydb.close()      
        return redirect(url_for('register.message',error=error02))
    elif myresult==None:
        new="INSERT INTO member (name,username,password) VALUES(%s,%s,%s)"
        val=(name,username,password)
        mycursor.execute(new, val)
        mydb.commit()
        mycursor.close()  
        mydb.close()   
        return render_template ("index.html")
    else:
        error01="帳號已經被註冊" 
        mycursor.close()    
        mydb.close()   
        return redirect(url_for('register.message',error=error01))
@register.route("/message/")
def message():
    
    error=request.args.get("error",None)
    return render_template("message.html",error=error)   
    # else:
    #     sql="INSERT INTO member (name,username,password) VALUES(%s,%s,%s)"
    #     val=(name,username,password)
    #     mycursor.execute(sql, val)
    #     mydb.commit()
    #     sucess="註冊成功"
    #     return redirect(url_for('success',error=sucess))
    

   