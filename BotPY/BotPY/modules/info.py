import configparser
import pymongo
import random
import telepot
from modules import users, keyboard
from telepot.loop import MessageLoop


def getNotification(chat_id, bot):
    if getNotificationLength(chat_id) > 0:
        bot.sendMessage(chat_id, "Nessuna nuova notifica")
    else:
        doc = myNotification.find({"idUser": chat_id})
        for n in doc:
            bot.sendMessage(chat_id, n["note"], reply_markup=keyboard.getKeyboardNotifiche())


def getNotificationLength(idUser):
    len = myNotification.find({"idUser": idUser}).count()
    return len


def delNotification(idUser):
    myNotification.delete_many({"idUser": idUser})
    return "Le notifiche sono state cancellate"


def getInfo():
    info = "informazioni del caso\nche al momento non ho sbatti di scrivere"
    return info


def NotiUpgradeToAdmin(nameUser, adminName):
    mydict = {"idUser": users.getIdByName(
        nameUser), "note": "Complimenti sei stato promosso ad admin da " + adminName}
    myNotification.insert_one(mydict)


def NotiUpgradeToUser(nameUser, adminName):
    mydict = {"idUser": users.getIdByName(
        nameUser), "note": "Siamo spiacenti ma sei stato retrocesso dal tuo ruolo di admin da " + adminName}
    myNotification.insert_one(mydict)


def NotiBan(nameUser, adminName):
    mydict = {"idUser": users.getIdByName(
        nameUser), "note": "Siamo spiacenti ma sei stato bannato da " + adminName}
    myNotification.insert_one(mydict)


read_config = configparser.ConfigParser()
read_config.read("prop.ini")

myclient = pymongo.MongoClient(read_config.get("Database", "process.env.dbconnection"))
mydb = myclient[read_config.get("Database", "dbName")]
myNotification = mydb[read_config.get("Database", "notification")]
