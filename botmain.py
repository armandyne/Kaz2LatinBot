# -*- coding: utf-8 -*-
import telebot
import kzlattranslit
import re
import settings
import SQLiteHelper
import jsonpickle
from flask import Flask, request
import os

server = Flask(__name__)
bot = telebot.TeleBot(settings.API_TOKEN)

def validate_text(text):
    if re.match("[А-Яа-яӘІҢҒҮҰҚӨҺәіңғүұқөһ]+", text) is None:
        return False
    else:
        return True
    
@bot.message_handler(commands=["start", "help"])
def send_ans_help_cmd(message):
    bot.reply_to(message, settings.HELP_COMMAND_RESPONCE_TEXT.format(message.from_user.first_name))
    db = SQLiteHelper.SQLiteHelper(settings.DATABASE_NAME)
    db.save_request(jsonpickle.encode(message), message.message_id, message.from_user.first_name,
                    message.from_user.username, message.date, message.text)
    db.close()
    print(message.from_user.first_name, message.from_user.username, message.text)

@bot.message_handler(commands=["author"])
def send_ans_author_cmd(message):
    bot.reply_to(message, settings.FEEDBACK_COMMAND_RESPONCE_TEXT.format(message.from_user.first_name))
    db = SQLiteHelper.SQLiteHelper(settings.DATABASE_NAME)
    db.save_request(jsonpickle.encode(message), message.message_id, message.from_user.first_name,
                    message.from_user.username, message.date, message.text)
    db.close()
    print(message.from_user.first_name, message.from_user.username, message.text)

@bot.message_handler(commands=["1", "2", "3"])
def send_ans_bot_cmd(message):
    rgx = re.compile(r"^\/([123])\s{1,}(.{1,})")
    mo = rgx.match(message.text)
    
    if mo is not None:
        command = mo.group(1)
        text = mo.group(2)
    else:
        command = None
        text = None
    
    if text is None:
        bot.reply_to(message, settings.EMPTY_CONTENT_RESPONCE_TEXT.format(message.from_user.first_name))
        bot.send_message(message.chat.id, settings.EMPTY_CONTENT_RESPONCE_TEXT2)
    else:
        if len(text) > settings.MAX_TEXT_LENGTH:
            bot.reply_to(message, settings.LONG_CONTENT_RESPONCE_TEXT.format(settings.MAX_TEXT_LENGTH, message.from_user.first_name))
        else:
            if not validate_text(text):
                bot.reply_to(message, settings.NO_KAZ_CONTENT_RESPONCE_TEXT.format(message.from_user.first_name))
            else:
                if len(text) < 4:
                    bot.reply_to(message, settings.SHORT_CONTENT_RESPONCE_TEXT.format(message.from_user.first_name))
                
                tr = kzlattranslit.kzlattranslit(text)        
                trans_text = tr.transliterate(tr.get_available_options()[int(command) - 1])
                
                bot.reply_to(message, trans_text)
    
    db = SQLiteHelper.SQLiteHelper(settings.DATABASE_NAME)
    db.save_request(jsonpickle.encode(message), message.message_id, message.from_user.first_name,
                    message.from_user.username, message.date, message.text)
    db.close()
    print(message.from_user.first_name, message.from_user.username, message.text)
    
@bot.message_handler(content_types=["text"])
def send_ans_default(message):
    bot.reply_to(message, settings.DEFAULT_RESPONCE_TEXT.format(message.from_user.first_name))
    db = SQLiteHelper.SQLiteHelper(settings.DATABASE_NAME)
    db.save_request(jsonpickle.encode(message), message.message_id, message.from_user.first_name,
                    message.from_user.username, message.date, message.text)
    db.close()
    print(message.from_user.first_name, message.from_user.username, message.text)
     

@server.route('/' + settings.API_TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "POST", 200


@server.route("/")
def web_hook():
    bot.remove_webhook()
    bot.set_webhook(url='https://kaz2latbot.herokuapp.com/' + settings.API_TOKEN)
    return "CONNECTED", 200

server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))   
