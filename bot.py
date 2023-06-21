from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from callbacks import (
    start,
    users,
    shop,
)

TOKEN = os.environ.get('TOKEN')
if TOKEN is None:
    print("set TOKEN env variable.")

def main():
    # create udpate
    updater = Updater(TOKEN)

    # get updater from updater obj
    dp = updater.dispatcher

    # add handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('users', users))
    dp.add_handler(MessageHandler(Filters.text('🛍 Shop'), shop))

    # start polling 
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()