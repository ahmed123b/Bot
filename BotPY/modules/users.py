import configparser
import pymongo
import telepot
from modules import info, keyboard


def newUser(id, name, bot):
    if mycol.find_one({"id": id}) is None:  # se non presente inserisci
        mydict = {"id": id, "name": name, "admin": False, "banned": False}
        mycol.insert_one(mydict)
    usr = getUser(id)
    if usr == 2:
        bot.sendMessage(id, "Risulti essere un utente bannato", reply_markup=keyboard.getKeyboard(usr))
    elif usr == 1:
        bot.sendMessage(id, "Scegli un opzione", reply_markup=keyboard.getKeyboard(usr))
    else:
        bot.sendMessage(id, "Scegli un opzione", reply_markup=keyboard.getKeyboard(usr))

def getUser(id):
    x = mycol.find_one({"id": id}, {"admin": 1, "banned": 1})
    if x["banned"] == True:
        return 2
    elif x["admin"] == True:
        return 1
    else:
        return 0

def doAdmin(name, chat_id, bot):
    myquery = {"name": name}
    newvalues = {"$set": {"admin": True}}
    if mycol.find(myquery).count() > 0:
        mycol.update_one(myquery, newvalues)
        bot.sendMessage(chat_id, "L'utente " + name + " è stato reso admin")
        info.NotiUpgradeToAdmin(name, bot.getChat(chat_id)["first_name"])
    else:
        bot.sendMessage(chat_id, 'Nessun utente con nome "' + name + '" è stato trovato')


def doUser(name, chat_id, bot):
    myquery = {"name": name}
    newvalues = {"$set": {"admin": False}}
    if mycol.find(myquery).count() > 0:
        mycol.update_one(myquery, newvalues)
        bot.sendMessage(chat_id, "L'utente " + name + " è stato retrocesso")
        info.NotiUpgradeToUser(name, bot.getChat(chat_id)["first_name"])
    else:
        bot.sendMessage(chat_id, 'Nessun utente con nome "' + name + '" è stato trovato')


def getIdByName(name):
    return mycol.find_one({"name": name})["id"]


def banUser(name, chat_id, bot):
    myquery = {"name": name}
    newvalues = {"$set": {"banned": True}}
    if mycol.find(myquery).count() > 0:
        mycol.update_one(myquery, newvalues)
        bot.sendMessage(chat_id, "L'utente " + name + " è stato bannato")
        bot.sendMessage(getIdByName(name), "Sei appena stato bandito da questo bot da " + name, reply_markup=keyboard.getKeyboard(2))
        info.NotiBan(name, bot.getChat(chat_id)["first_name"])
    else:
        bot.sendMessage(chat_id, 'Nessun utente con nome "' + name + '" è stato trovato')

read_config = configparser.ConfigParser()
read_config.read("prop.ini")

myclient = pymongo.MongoClient(read_config.get("Database", "dbconnection"))
mydb = myclient[read_config.get("Database", "dbName")]
mycol = mydb[read_config.get("Database", "users")]
