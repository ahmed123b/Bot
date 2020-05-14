import telepot
import time
import emoji
import configparser
from telepot.loop import MessageLoop
from modules import users, freddure, sos, info, input, keyboard

read_config = configparser.ConfigParser()
read_config.read("prop.ini")
ini = configparser.ConfigParser()
ini.read("keyboard.ini")

insert, pun = None, ""

def on_chat_message(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	command = msg['text'] #get del comando inviato
	global insert , pun; 
	if insert != None and insert != True :
			if (insert == "pun"):
				pun = command
			insert = input.insertDefault(bot, pun, command, chat_id, insert)
	elif command == "/home" or command == emoji.emojize(ini.get("admin","menu"), use_aliases=True):
            users.newUser(chat_id,  bot.getChat(chat_id)["first_name"], bot)
	elif command == emoji.emojize(ini.get("key","readPun"), use_aliases=True):
            bot.sendMessage(chat_id, "Scegli la categoria che preferisci", reply_markup=keyboard.getKeyboardFreddure())
	elif command in read_config.get("Database","category"):
			freddure.sendPunUser(insert, pun, command, chat_id, bot)
	elif command == emoji.emojize(ini.get("key","sendBug"), use_aliases=True):
            insert = "bug" 
            bot.sendMessage(chat_id, "Inserisci la segnalazione che vuoi effettuare:")
	elif command == emoji.emojize(ini.get("key","sendPun"), use_aliases=True):
    		bot.sendMessage(chat_id, "Inserisci la battuta che vuoi mandare:")
    		insert = "pun"
	elif command == emoji.emojize(ini.get("key","info"), use_aliases=True):
    		bot.sendMessage(chat_id, info.getInfo())
	elif command == emoji.emojize(ini.get("key","noti"), use_aliases=True):
			info.getNotification(chat_id, bot)	
	elif command == emoji.emojize(ini.get("key","deleteNoti"), use_aliases=True):
    		bot.sendMessage(chat_id, info.delNotification(chat_id))
	elif command == emoji.emojize(ini.get("key","admin"), use_aliases=True):
    		bot.sendMessage(chat_id,"Benvenuto nella sezione admin", reply_markup=keyboard.getKeyboardAdmin())
	elif command == emoji.emojize(ini.get("admin","visualizeBug"), use_aliases=True):
			sos.getSosUser(chat_id, bot)
	elif command == emoji.emojize(ini.get("admin","approvePun"), use_aliases=True):
			freddure.getApprove(chat_id, bot)
	elif command == emoji.emojize(ini.get("admin","makeAdmin"), use_aliases=True):
			insert = "admin"
			bot.sendMessage(chat_id, "Inserisci il nome della persona che vuoi rendere admin:", reply_markup=keyboard.getKeyboardCancel())
	elif command == emoji.emojize(ini.get("admin","removeAdmin"), use_aliases=True):
			insert = "user"
			bot.sendMessage(chat_id, "Inserisci il nome della persona che vuoi degradare:", reply_markup=keyboard.getKeyboardCancel())
	elif command == emoji.emojize(ini.get("admin","deletePun"), use_aliases=True):
			insert = "delPun"
			bot.sendMessage(chat_id, "Inserisci il testo della freddura che vuoi eliminare:", reply_markup=keyboard.getKeyboardCancel())
	elif command == emoji.emojize(ini.get("admin","banUser"), use_aliases=True):
			insert = "banUser"
			bot.sendMessage(chat_id, "Inserisci il nome della persona che vuoi bannare:", reply_markup=keyboard.getKeyboardCancel())
	else:
			bot.sendMessage(chat_id, "Comando non riconosciuto")

def on_callback_query(msg): 
	query_id, chat_id, query_data = telepot.glance(msg, flavor='callback_query')
	if query_data == ini.get("callback","deleteBug"):
		sos.delSos()
		bot.deleteMessage((chat_id, msg["message"]["message_id"]))
		bot.answerCallbackQuery(query_id, text="Segnalazione eliminata")
	elif query_data == ini.get("callback","approvePun"):
		freddure.ApprovePun()
		bot.deleteMessage((chat_id, msg["message"]["message_id"]))
		bot.answerCallbackQuery(query_id, text="Freddura approvata")
	elif query_data == ini.get("callback","deletePun"):
		freddure.delApprove()
		bot.deleteMessage((chat_id, msg["message"]["message_id"]))
		bot.answerCallbackQuery(query_id, text="Freddura eliminata")
	elif query_data == ini.get("callback","deletePunDef"):
		freddure.deletePun(msg["message"]["text"], chat_id, bot)
		bot.deleteMessage((chat_id, msg["message"]["message_id"]))
		bot.answerCallbackQuery(query_id, text="Freddura eliminata")
	elif query_data == ini.get("callback","Cancel"):
		bot.deleteMessage((chat_id, msg["message"]["message_id"]))
		bot.answerCallbackQuery(query_id, text="Operazione annullata")
		global insert
		insert = None
	elif query_data == ini.get("callback","ignorePun"):
		bot.deleteMessage((chat_id, msg["message"]["message_id"]))
		

bot = telepot.Bot(read_config.get("Bot", "TOKEN"))
MessageLoop(bot, {'chat': on_chat_message,
				  'callback_query': on_callback_query}).run_as_thread() 
print("Running")

while 1:
	time.sleep(10)