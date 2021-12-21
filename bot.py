import epic
import os
import telegram
import pickle

token = os.environ.get('epic_bot_token')
bot = telegram.Bot(token=token)
try:
    chat_ids = pickle.load(open('chat_ids', 'rb'))
except FileNotFoundError:
    chat_ids = []

def updateChatIds():
    updates = bot.get_updates()
    for update in updates:
        try:
            new_group = update['my_chat_member']['chat']
            if new_group['id'] not in chat_ids:
                print('New group chat: {0}'.format(new_group['id']))
                chat_ids.append(new_group['id'])
        except TypeError:
            pass
    pickle.dump(chat_ids, open('chat_ids', 'wb'))

def sendMessage(message):
    for c_id in chat_ids:
        try:
            bot.send_message(text=message, chat_id=c_id)
        except telegram.error.BadRequest:
            print('Could not send message to: {0}'.format(c_id))

def updateAndMessage(message):
    updateChatIds()
    sendMessage(message)