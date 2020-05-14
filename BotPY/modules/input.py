import configparser
import pymongo
import random
import telepot
import datetime
from modules import keyboard, users, sos, freddure
from telepot.loop import MessageLoop

def insertDefault(bot, pun, command, chat_id, insert):
	if insert == "pun":
			bot.sendMessage(chat_id, "Seleziona a categoria a cui appartine", reply_markup=keyboard.getKeyboardFreddure())
			return True
	elif insert == "bug":
    		sos.sendSos(command, chat_id) 
    		bot.sendMessage(chat_id, "La tua segnalazione è stata inviata e presto verrà presa in considerazione") 
	elif insert == "admin":
    		users.doAdmin(command, chat_id, bot)
	elif insert == "user":
    		users.doUser(command, chat_id, bot)
	elif insert == "delPun":
    		freddure.findPun(command, chat_id, bot)
	elif insert == "banUser":
    		users.banUser(command, chat_id, bot)
	return None