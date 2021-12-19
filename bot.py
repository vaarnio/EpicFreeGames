import epic
import os
import telegram
import pickle

token = os.environ.get('epic_bot_token')
bot = telegram.Bot(token=token)

try:
    group_ids = pickle.load(open('group_ids', 'rb'))
except FileNotFoundError:
    group_ids = []

updates = bot.get_updates()
for update in updates:
    try:
        new_chat = update['my_chat_member']['chat']
        if new_chat.id not in group_ids:
            print('New group chat: {0}'.format(new_chat.id))
            group_ids.append(new_chat.id)
    except TypeError:
        pass

group_ids = list(set(group_ids)) #remove duplicates by converting to set and back to list

message = ''.join([epic.offerToString(offer) + '\n' for offer in epic.getFree()])

for c_id in group_ids:
    try:
        bot.send_message(text=message, chat_id=c_id)
    except telegram.error.BadRequest:
        print('Could not send message to: {0}'.format(c_id))

pickle.dump(group_ids, open('group_ids', 'wb'))