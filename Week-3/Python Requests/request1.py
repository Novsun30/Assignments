import urllib.request as requst
import json
with requst.urlopen("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json") as response:
    src = json.load(response)
result = src["result"]["results"]
with open("data.csv", "w" , encoding="utf-8") as file :
    targetAddress = {"中正區","萬華區","中山區","大同區","大安區","松山區","信義區","士林區","文山區","北投區","內湖區","南港區"}
    for i in range(len(result)):
        date = int(result[i]["xpostDate"][0:4])
        title = result[i]["stitle"]
        jsonAdress = {result[i]["address"][5:8]}
        address = str(targetAddress & jsonAdress)[2:5]
        longitude = result[i]["longitude"]
        latitude = result[i]["latitude"]
        firstPic = ""
        if date <2015:
             continue
        for j in range(len(result[i]["file"])):
            url = result[i]["file"].lower()
            if url[j] == "j" and url[j+1] == "p" and url[j+2] == "g":
                firstPic = url[0:j+3]
                break
        file.write(title + "," + address + "," + longitude + "," + latitude + "," + firstPic + "\n")