from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import emoji
import configparser

def getKeyboard(usr):
    if usr == 0:
        k = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text=emoji.emojize(ini.get("key","readPun"), use_aliases=True))],
		        [KeyboardButton(text=emoji.emojize(ini.get("key","sendPun"), use_aliases=True))],
                [KeyboardButton(text=emoji.emojize(ini.get("key","sendBug"), use_aliases=True))],
                [KeyboardButton(text=emoji.emojize(ini.get("key","info"), use_aliases=True)), KeyboardButton(text=emoji.emojize(ini.get("key","noti"), use_aliases=True))], #KeyboardButton(text="Invita un amico")
            ], resize_keyboard=True
        )
    elif usr == 1:
        k = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text=emoji.emojize(ini.get("key","readPun"), use_aliases=True))],
		        [KeyboardButton(text=emoji.emojize(ini.get("key","sendPun"), use_aliases=True))],
                [KeyboardButton(text=emoji.emojize(ini.get("key","sendBug"), use_aliases=True))],
                [KeyboardButton(text=emoji.emojize(ini.get("key","info"), use_aliases=True)), KeyboardButton(text=emoji.emojize(ini.get("key","noti"), use_aliases=True))], #KeyboardButton(text="Invita un amico")
                [KeyboardButton(text=emoji.emojize(ini.get("key","admin"), use_aliases=True))]
            ], resize_keyboard=True
        )
    elif usr == 2:        
        k = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text=emoji.emojize(ini.get("key","errorBan"), use_aliases=True))],
                [KeyboardButton(text=emoji.emojize(ini.get("key","noti"), use_aliases=True))]
            ], resize_keyboard=True
        )
    return k

def getKeyboardFreddure():
    kFreddure = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=emoji.emojize(ini.get("category","IT"), use_aliases=True)),KeyboardButton(text=emoji.emojize(ini.get("category","food"), use_aliases=True)),KeyboardButton(text=emoji.emojize(ini.get("category","animal"), use_aliases=True))],
            [KeyboardButton(text=emoji.emojize(ini.get("category","man"), use_aliases=True)),KeyboardButton(text=emoji.emojize(ini.get("category","woman"), use_aliases=True)),KeyboardButton(text=emoji.emojize(ini.get("category","kid"), use_aliases=True))],
            [KeyboardButton(text=emoji.emojize(ini.get("category","jew"), use_aliases=True)),KeyboardButton(text=emoji.emojize(ini.get("category","racist"), use_aliases=True)),KeyboardButton(text=emoji.emojize(ini.get("category","cop"), use_aliases=True))],
            [KeyboardButton(text=emoji.emojize(ini.get("category","thing"), use_aliases=True)),KeyboardButton(text=emoji.emojize(ini.get("category","other"), use_aliases=True))],
            [KeyboardButton(text=emoji.emojize(ini.get("admin","menu"), use_aliases=True))]
        ], resize_keyboard=True
    )
    return kFreddure

def getKeyboardNotifiche():
    kNotifiche = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=emoji.emojize(ini.get("key","deleteNoti"), use_aliases=True))],
            [KeyboardButton(text=emoji.emojize(ini.get("admin","menu"), use_aliases=True))]
        ], resize_keyboard=True
    )
    return kNotifiche

def getKeyboardAdmin():
    kAdmin = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=emoji.emojize(ini.get("admin","visualizeBug"), use_aliases=True))],
            [KeyboardButton(text=emoji.emojize(ini.get("admin","approvePun"), use_aliases=True)),KeyboardButton(text=emoji.emojize(ini.get("admin","deletePun"), use_aliases=True))],
            [KeyboardButton(text=emoji.emojize(ini.get("admin","makeAdmin"), use_aliases=True)),KeyboardButton(text=emoji.emojize(ini.get("admin","removeAdmin"), use_aliases=True)),KeyboardButton(text=emoji.emojize(ini.get("admin","banUser"), use_aliases=True))],
            [KeyboardButton(text=emoji.emojize(ini.get("admin","menu"), use_aliases=True))]
        ], resize_keyboard=True
    )
    return kAdmin

def getKeyboardSos():
    kSos = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=emoji.emojize(ini.get("inline","delete"), use_aliases=True), callback_data=ini.get("callback","deleteBug"))],
        ]
    )
    return kSos


def getKeyboardPun():
    kPun = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=emoji.emojize(ini.get("inline","approve"), use_aliases=True), callback_data=ini.get("callback","ApprovePun")), InlineKeyboardButton(text=emoji.emojize(ini.get("inline","delete"), use_aliases=True), callback_data=ini.get("callback","deletePun"))],

        ]
    )
    return kPun

def getKeyboardDeletePun():
    kPun = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=emoji.emojize(ini.get("inline","delete"), use_aliases=True), callback_data=ini.get("callback","deletePunDef")), InlineKeyboardButton(text=emoji.emojize(ini.get("inline","ignore"), use_aliases=True), callback_data=ini.get("callback","ignorePun"))],     
        ]
    )
    return kPun

def getKeyboardCancel():
    kCancel = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=emoji.emojize(ini.get("inline","cancel"), use_aliases=True), callback_data=ini.get("callback","cancel"))],
        ]
    )
    return kCancel

ini = configparser.ConfigParser()
ini.read("keyboard.ini")