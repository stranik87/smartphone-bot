from telegram.ext import Updater, CommandHandler
import os
from callbacks import (
    start,
    users,
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

    # start polling 
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()