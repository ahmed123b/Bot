import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
 
from pprint import pprint
import time
import datetime
import json
import emoji
import pymongo
import test

TOKEN="886061784:AAE3-BeNa0idp4RRuGXp0ZWqn-OPnBUunxQ" #da sostituire
k = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Yes"), KeyboardButton(text="No")],
		[KeyboardButton(text="1"), KeyboardButton(text="2")]
    ], resize_keyboard=True
)

def on_chat_message(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
 
	keyboard = InlineKeyboardMarkup(inline_keyboard=[
                     [InlineKeyboardButton(text='IP', callback_data='ip'),
                     InlineKeyboardButton(text='Info', callback_data='info')],
                     [InlineKeyboardButton(text=emoji.emojize('Time :watch:', use_aliases=True), callback_data='time')],
                 ])

	bot.sendMessage(chat_id, 'Use inline keyboard'+ emoji.emojize('Time :watch:', use_aliases=True), reply_markup=keyboard)
 
 
def on_callback_query(msg): 
	query_id, chat_id, query_data = telepot.glance(msg, flavor='callback_query')
	print('Callback Query:', query_id, chat_id, query_data)
	if query_data=='ip':
		#my_ip = urlopen('http://ip.42.pl/raw').read()
		myclient = pymongo.MongoClient("mongodb://localhost:27017/")
		mydb = myclient["mydb"]
		mycol = mydb["freddure"]

		for x in mycol.find():
  			print(x["freddura"])
			#bot.sendMessage(chat_id, x["freddura"])
	elif query_data=='info':
		#info=json.dumps(bot.getUpdates(),sort_keys=True, indent=4)
		#bot.sendMessage(chat_id, info)
		 bot.sendMessage(chat_id, test.greeting(),
                            reply_markup=k)
	elif query_data=='time':
		ts = time.time()
		bot.answerCallbackQuery(query_id, text=datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')) #messaggio a comparsa

 
 
bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
				  'callback_query': on_callback_query}).run_as_thread() 
print('Listening ...')
 
 
while 1:
	time.sleep(10)