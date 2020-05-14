import configparser
import pymongo
import random
import telepot
import datetime
from modules import keyboard
from telepot.loop import MessageLoop


def getPun(category):
    count = myPun.find({"category": category}).sort("category").count()
    if count > 0:
        fred = myPun.find({"category": category}).sort(
            "category").limit(-1).skip(random.randrange(count)).next()["pun"]
    else:
        fred = "Freddure non disponibili per questa categoria\nSuggericene una"
    return fred


def sendPun(pun, category, idUser):
    insCol = mydb[read_config.get("Database", "approve")]
    toInsert = {"pun": pun, "category": category, "idUser": int(
        idUser), "date": datetime.datetime.utcnow()}
    insCol.insert_one(toInsert)


def sendPunUser(insert, pun, category, chat_id, bot):
    if insert == True:
        insert = None
        sendPun(pun, category, str(chat_id))
        bot.sendMessage(chat_id, "La tua battuta è stata inviata con successo ora dev'essere approvata")
    else:
        bot.sendMessage(chat_id, getPun(category))


def getApprove(chat_id, bot):
    if getApproveLen() > 0:
        approve = getFirstApprove()
        bot.sendMessage(chat_id, approve["pun"]+"\nCategoria: " +
                        approve["category"], reply_markup=keyboard.getKeyboardPun())
    else:
        bot.sendMessage(chat_id, "Nessuna nuova freddura da approvare")


def getFirstApprove():
    a = myApprove.find().sort("date").next()
    approve = {"pun": a["pun"], "category": a["category"]}
    return approve


def getApproveLen():
    count = myApprove.find().count()
    return count


def delApprove():
    query = {"pun": getFirstApprove()["pun"]}
    myApprove.delete_one(query)


def ApprovePun():
    a = getFirstApprove()
    query = {"pun": a["pun"], "category": a["category"]}
    myPun.insert_one(query)
    myApprove.delete_one({"pun": a["pun"]})


def findPun(src, chat_id, bot):
    doc = myPun.find({'pun': {'$regex': src, '$options': 'i'}})
    for d in doc:
        bot.sendMessage(chat_id, d["pun"] + "\nCategoria: " +
                        d["category"], reply_markup=keyboard.getKeyboardDeletePun())


def deletePun(msg, chat_id, bot):
    pun = msg[0:  msg.index("\nCategoria: ")]
    category = msg[msg.index("\nCategoria: "):].replace("\nCategoria: ", "")
    myPun.delete_many({"pun": pun, "category": category})
    myDeleted.insert_one({"pun": pun, "category": category, "user": chat_id})


read_config = configparser.ConfigParser()
read_config.read("prop.ini")

myclient = pymongo.MongoClient(read_config.get("Database", "dbconnection"))
mydb = myclient[read_config.get("Database", "dbName")]
myPun = mydb[read_config.get("Database", "pun")]
myDeleted = mydb[read_config.get("Database", "deleted")]
myApprove = mydb[read_config.get("Database", "approve")]
