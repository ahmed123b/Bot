#"886061784:AAE3-BeNa0idp4RRuGXp0ZWqn-OPnBUunxQ"
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
 
from pprint import pprint
import time
import datetime
import json
import emoji

TOKEN="886061784:AAE3-BeNa0idp4RRuGXp0ZWqn-OPnBUunxQ" #da sostituire
 
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
		bot.sendMessage(chat_id, "my_ip")
	elif query_data=='info':
		info=json.dumps(bot.getUpdates(),sort_keys=True, indent=4)
		bot.sendMessage(chat_id, info)
	elif query_data=='time':
		ts = time.time()
		bot.answerCallbackQuery(query_id, text=datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')) #messaggio a comparsa
 
 
bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
				  'callback_query': on_callback_query}).run_as_thread() 
print('Listening ...')
 
 
while 1:
	time.sleep(10)