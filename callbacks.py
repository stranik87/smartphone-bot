from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext

# import db
from db import UsersDB

# create db obj
usersDB = UsersDB()


def start(update: Update, context: CallbackContext):
    # add user into database
    user = update.effective_user
    output = usersDB.add_user(
        user_id=user.id,
        firstname=user.first_name,
        lastname=user.last_name,
        username=user.username
    )
    # keyborads
    keyboard = [
        ['🛍 Shop', '🛒 Cart'],
        ['📞 Contact', '📝 About']
    ]
    # send welcome message
    if output == False:
        update.message.reply_html(
            text=f'<b>Hi {user.first_name}</b>\n\nWelcome back!',
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        )
    if output == True:
        update.message.reply_html(
            text=f'<b>Hello {user.first_name}</b>\n\nWelcome to our bot!',
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        )


def users(update: Update, context: CallbackContext):
    # get all users from database
    users = usersDB.get_all_users()

    # send users as message
    text = '<b>Available Users</b>\n\n'
    for user in users:
        text += f"{user['firstname']} {user['lastname']} - @{user['username']}\n"
    update.message.reply_html(
        text=text
    )
