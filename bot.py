from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import os
from callbacks import (
    start,
    users,
    shop,
    smartphone,
    phone,
    add_cart,
    contact,
)

TOKEN = os.environ.get('TOKEN')
if TOKEN is None:
    print("set TOKEN env variable.")

def main():
    # create udpate
    updater = Updater(TOKEN,use_context=True)

    # get updater from updater obj
    dp = updater.dispatcher

    # add handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('users', users))
    dp.add_handler(MessageHandler(Filters.text('🛍 Shop'), shop))
    dp.add_handler(CallbackQueryHandler(smartphone, pattern='brend:'))
    dp.add_handler(CallbackQueryHandler(phone, pattern='phone:'))
    dp.add_handler(CallbackQueryHandler(add_cart, pattern='add:'))
    dp.add_handler(MessageHandler(Filters.text('📞 Contact'),contact))

    # start polling 
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()