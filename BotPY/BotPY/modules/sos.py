import configparser
import pymongo
import telepot
from modules import keyboard
from telepot.loop import MessageLoop

def sendSos(bug, idUser):  
    toInsert = {"bug" : bug,  "idUser": idUser}
    mycol.insert_one(toInsert)

def getSosUser(chat_id, bot):
    if getSosLength() > 0:
        bot.sendMessage(chat_id, getSos(), reply_markup= keyboard.getKeyboardSos())
    else:
        bot.sendMessage(chat_id, "Nessuna nuova segnalazione")

def getSos():
    sos = mycol.find_one()
    return sos["bug"]

def delSos():
    myquery = { "bug": getSos() }
    mycol.delete_one(myquery)

def getSosLength():
    return mycol.find().count()


read_config = configparser.ConfigParser()
read_config.read("prop.ini")

myclient = pymongo.MongoClient(read_config.get("Database", "process.env.dbconnection"))
mydb = myclient[read_config.get("Database", "dbName")]
mycol = mydb[read_config.get("Database", "sos")]