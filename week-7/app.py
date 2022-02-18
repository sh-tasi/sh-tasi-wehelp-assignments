from pickle import TRUE
from flask import Flask,Blueprint,render_template,session,url_for,request,redirect,session
from register.view import register
from login_system.view import login_system
from member_system.view import member_system

app=Flask(
    __name__,
)
app.secret_key="123456789d"
app.register_blueprint(register, url_prefix='/signup')
app.register_blueprint(login_system, url_prefix='/signin')
app.register_blueprint(member_system, url_prefix='/api')

@app.route("/")
def index():
    
    return render_template ("index.html")

@app.route("/member",methods=["GET","POST"])
def member():
    member_user=session.get('name')
    print(member_user)
    if member_user==None:
        return render_template ("index.html")
    else:   
        return render_template("member.html",name=member_user)
    # else :
    #     return render_template ("index.html")



app.run(port=3000)