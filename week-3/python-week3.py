import urllib.request as request
import json
url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

with request.urlopen(url) as response:
    data=json.load(response)

view=data["result"]["results"]  #取出results 列表
# stitle 
# address 
# longitude
# latitude
# file

with open("data.csv","w",encoding="utf-8") as file: #寫入檔案
   for add in view :
        jpgg=add["file"].lower().split("jpg",1)  #將file 中的字串轉為小寫，再用jpg 分割字串(只找第一張圖)放到第0個位子
        file.write(add["stitle"]+","+add["address"][5:8]+","+add["longitude"]+","+add["latitude"]+","+jpgg[0]+"jpg"+"\n")
