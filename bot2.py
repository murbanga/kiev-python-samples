#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import pandas
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

table = pandas.read_excel("8classDataBase.xlsx")


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('All hail to Ukraine!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

# поиск сервиса подходящего для запроса 
def search_for_request(s):
    # наш счётчик строк
    row = 0

    # перебираем все сервисы из колонки SERVICE в таблице
    for services in table["SERVICE"]:
        # у каждого ментора сервисы записаны через запятую
        # разделим эту строку на список сервисов
        services_list = list(str(services).split(", "))

        # переберем все сервисы из этой строки
        for serv in services_list:
            if s == serv:
                print("found!")
                # сервис нашелся!
                # составим ответ "Первый ментор который вам подходит - это"
                reply = "Your first found mentor is\n"
                # соберем все ячейки из нашей строки
                # (мы считали строки, пока перебирали их, и знаем номер строки)
                # "для всех ячеек из строки row приклеить их по-очереди к строке reply, через запятую"
                for i in table.iloc[row]: reply += str(i) + ", "
                # вернуть ответ как результат этой подпрограммы
                # здесь все циклы прерываются и мы сразу возвращаемся ровно в то место,
                # откуда вызвали search_for_request()
                return reply

        # в этой строке подходящего сервиса не нашлось переходим к следующей, если она есть
        # и увеличиваем наш счетчик строк
        row = row + 1
    
    # мы перебрали все сервисы и ничего не нашли
    # возвращаем "Ничего"
    return None

def echo(update, context):
 
    s = update.message.text
    try:
        i = int(s)
        if i == 1:
            update.message.reply_text('12')
        elif i == 2:
            update.message.reply_text('22')
        else:
            update.message.reply_text('unknown')
    except: 
        # если сообщение от пользователя s начинается со слов "request"
        if s.startswith("request"):
            # s[8:] превращает "request google" в "google"
            #                   01234567<---->
            # "взять всю строку начиная с восьмого символа"
            requested_service = s[8:]
            # вызываем подпрограмму, которая ищет сервис
            reply = search_for_request(requested_service)
            if reply != None:
                update.message.reply_text(reply)
            else:
                update.message.reply_text(f"Sorry, nothing found for you request '{requested_service}'")

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

"""Start the bot."""
# Create the Updater and pass it your bot's token.
# Make sure to set use_context=True to use the new context based callbacks
# Post version 12 this will no longer be necessary
updater = Updater("5398235656:AAHlKJiabiQwZ2rQhsuer3Afsk-eT1ZMlv8", use_context=True)

# Get the dispatcher to register handlers
dp = updater.dispatcher

# on different commands - answer in Telegram
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))

# on noncommand i.e message - echo the message on Telegram
dp.add_handler(MessageHandler(Filters.text, echo))

# log all errors
dp.add_error_handler(error)

# Start the Bot
updater.start_polling()

# Run the bot until you press Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT. This should be used most of the time, since
# start_polling() is non-blocking and will stop the bot gracefully.
updater.idle()
