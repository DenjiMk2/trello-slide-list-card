import configparser
import requests

inifile = configparser.ConfigParser()
inifile.read("./dailyUpdate.ini", "UTF-8")

key = inifile.get("settings","key")
token = inifile.get("settings","token")
boardID = inifile.get("IDs","board")
listNumber = int(inifile.get("IDs","listNumber"))
lists = [inifile.get("IDs",str(i+1)) for i in range(listNumber)]

# print(lists)
for x,y in zip(lists[::-1],lists[:-1][::-1]):
	url = "https://api.trello.com/1/lists/"+ y +"/moveAllCards"
	querystring = {"idBoard":boardID,"idList":x,"key":key,"token":token}
	response = requests.request("POST", url, params=querystring)
	response.raise_for_status()
