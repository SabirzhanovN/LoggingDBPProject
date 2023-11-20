import telebot
from telebot import types

my_token = '6858776423:AAEIQeQ8WvVN_RUDwgBJehc8zEp9BX6E6DI'
my_id = '1404363032'

client = telebot.TeleBot(token=my_token)


@client.message_handler()
def send_message(text):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text='YES', callback_data='yes')
    item_no = types.InlineKeyboardButton(text='NO', callback_data='no')

    markup_inline.add(item_yes, item_no)
    client.send_message(my_id, text, reply_markup=markup_inline)


@client.callback_query_handler(func=lambda callback: callback.data)
def answer(callback):
    if callback.data == 'yes':
        client.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="Success!")
        return 'OK'
    else:
        client.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="Cancelled!")
        return 'NO'

