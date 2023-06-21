from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext

# import db
from db import UsersDB, SmartphonesDB

# create db obj
usersDB = UsersDB()
smartphonesDB = SmartphonesDB()


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


def shop(update: Update, context: CallbackContext):
    # get all brends from database
    brends = smartphonesDB.get_brends()
    # keyboards
    keyboard = []
    for brend in brends:
        keyboard.append([InlineKeyboardButton(brend, callback_data=f"brend:{brend}")])
    
    # send brends as message
    update.message.reply_html(
        text='<b>Available Brends</b>\n\n',
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


def smartphone(update: Update, context: CallbackContext):
    # get brend from callback_data
    brend = update.callback_query.data.split(':')[1]
    # get all smartphones from brend
    smartphones = smartphonesDB.get_smartphones(brend)
    # keyboards
    keyboard = []
    row = []
    for phone in smartphones:
        row.append(InlineKeyboardButton(text=f"{phone.doc_id}",callback_data=f'phone:{brend}-{phone.doc_id}'))
        if len(row)==8:
            keyboard.append(row)
            row = []
    keyboard.append(row)
    # send smartphones as message
    update.callback_query.message.reply_html(
        text=f'<b>Available Smartphones from {brend}</b>\n\n',
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


def phone(update: Update, context: CallbackContext):
    # get brend and phone from callback_data
    brend, phone = update.callback_query.data.split(':')[1].split('-')
    # get smartphone from database
    smartphone = smartphonesDB.db.table(brend).get(doc_id=phone)
    # send smartphone as message
    update.callback_query.message.reply_photo(
        photo=smartphone['img_url'],
        caption=f'<b>Smartphone {smartphone.doc_id}</b>\n\n' +
        f'<b>Model:</b> {smartphone["name"]}\n'
        f'<b>Brend:</b> {smartphone["company"]}\n' +
        f'<b>Price:</b> {smartphone["price"]}\n' +
        f'<b>Memeory:</b> {smartphone["memory"]}\n' +
        f'<b>Color:</b> {smartphone["color"]}\n' +
        f'<b>Ram:</b> {smartphone["RAM"]}',
        parse_mode='HTML',
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Add to Cart', callback_data=f'add:{brend}-{phone}')]])
    )