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
    username_blank=0
    name=request.form["name"]
    username=request.form["username"]
    password=request.form["password"]
    mycursor = mydb.cursor()
    mycursor.execute("SELECT username FROM member")
    if len(username)==0 or username.isspace==True:
        username_blank=1
    username_search=(username,)
    myresult = mycursor.fetchall()
    if username_search in myresult:
        error01="帳號已經被註冊" 
        mycursor.close()    
        mydb.close()   
        return redirect(url_for('register.message',error=error01))
                # error01="帳號已註冊，請重新輸入"     
        # return redirect(url_for('error01',error=error01))
    elif len(name)==0 or len(password)==0 or username_blank==1 or name.isspace()==True or password.isspace()==True :
        error02="請輸入姓名&帳號&密碼"  
        mycursor.close()  
        mydb.close()      
        return redirect(url_for('register.message',error=error02))
    else:
        new="INSERT INTO member (name,username,password) VALUES(%s,%s,%s)"
        val=(name,username,password)
        mycursor.execute(new, val)
        mydb.commit()
        mycursor.close()  
        mydb.close()   
        return render_template ("index.html")
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
    

   