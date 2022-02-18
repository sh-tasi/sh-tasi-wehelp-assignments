from pickle import FALSE, TRUE
from flask import Flask,Blueprint,render_template,request,redirect,url_for,jsonify,session
import json
import mysql.connector
from sqlalchemy import true
from werkzeug import Response

member_system = Blueprint('member_system',__name__,template_folder='templates/member_system')


@member_system.route('/members',methods=["GET"])
def search_member():
    username=request.args.get("username","test")
    mydb = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='qweasdzxc',
    database='website'
    )
    mycursor = mydb.cursor()
    sql="SELECT `id`,`name`,`username` FROM `member` WHERE `username` = %s  "
    username_sql=(username,)
    mycursor.execute(sql,username_sql)
    myresult=mycursor.fetchone()
    print(myresult)
    if myresult!=None:
        datas_field=list(zip(*mycursor.description))[0]  #ZIP(*ZIPPEDLIST)拆開LIST 取元組0號為，重新列成datas_field列表
        # print(datas_field)
        # print(type(datas_field[0]))
        # print(myresult)
        # print(type(myresult))
        data_resoponse=dict(zip(datas_field,myresult))
        data_resoponse_data={'data':data_resoponse}
        data_resoponse_js=jsonify(data_resoponse_data)
        # print(type(data_resoponse_js))
        # print(type(p))
        # print(data_resoponse)
        mycursor.close()
        mydb.close()
        return (data_resoponse_js)
    else:
        data_resoponse={"data":None}
        data_resoponse_js=jsonify(data_resoponse)
        return(data_resoponse_js)
@member_system.route('/member',methods=["POST"])
def updat_name():
    if "application/json" in request.headers["content-Type"]:
        body=request.json
        member_user=session.get('username')
        print(body)
        request_user=body["name"]
        print(request_user)
        print(member_user)
        print(request_user.isspace())
        if member_user!=None and " " not in request_user and bool(request_user)==True: 
            mydb = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='qweasdzxc',
            database='website'
            )
            mycursor = mydb.cursor()
            # SAFE_UPDATES="SET SQL_SAFE_UPDATES = 0;"
            # mycursor.execute(SAFE_UPDATES)
            sql_updata="UPDATE `member` SET `name`= %s WHERE `username`= %s ;"
            val_updata=(request_user,member_user)
            # val_updata=(member_user,request_user)
            mycursor.execute(sql_updata,val_updata)
            mydb.commit()
            mycursor.close()
            mydb.close()
            response_body={
                "ok":True
            }
            response_body_js=jsonify(response_body)
            return(response_body_js)
        else :
            response_body={
                "error":True
            }
            response_body_js=jsonify(response_body)
            return(response_body_js)
    else:
        return Response(status=415)

    