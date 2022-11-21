from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! I am a Kiev Scholar Sample Bot!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def reply(update, context):
    s = update.message.text
    if s.startswith("="):
        try:
            answer = eval(s[1:])
            update.message.reply_text(answer)
        except:
            update.message.reply_text("error!")
    else:
        update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    print(f"Update {update} caused error {context.error}")

# Create the Updater and pass it your bot's token.
# Make sure to set use_context=True to use the new context based callbacks
# Post version 12 this will no longer be necessary
updater = Updater("5772398306:AAGYDTKRjWBaF46t_nMeq5nosDSusJ0aIsY", use_context=True)

# Get the dispatcher to register handlers
dp = updater.dispatcher

# on different commands - answer in Telegram
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))

# on noncommand i.e message - echo the message on Telegram
dp.add_handler(MessageHandler(Filters.text, reply))

# log all errors
dp.add_error_handler(error)

# Start the Bot
updater.start_polling()

# Run the bot until you press Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT. This should be used most of the time, since
# start_polling() is non-blocking and will stop the bot gracefully.
updater.idle()
