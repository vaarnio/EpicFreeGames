import epic
import sys
import bot
import pickle

try:
    free_games = epic.getFree()
except:
    sys.exit('Could not get list of free games')

try:
    old_games = pickle.load(open('old_games', 'rb'))
except FileNotFoundError:
    old_games = []
except:
    sys.exit('Something went wrong when reading old_games pickle file.')

old_ids = [game['id'] for game in old_games]
new_games = [game for game in free_games if game['id'] not in old_ids] # filter out old but active deals

free_ids = [game['id'] for game in free_games]
old_games = [game for game in old_games if game['id'] in free_ids] # filter out expired deals

pickle.dump(old_games + new_games, open('old_games', 'wb')) #pickle old_games + new_games

if len(new_games) == 0:
    sys.exit('No new deals.')

old_games_string = ''.join([offer['title'] + '\n' for offer in old_games])
new_games_string = ''.join([offer['title'] + '\n' for offer in new_games])

message = 'New free games:\n{0}'.format(new_games_string)
if len(old_games) != 0 : message += '\nContinuing free game deals:\n{0}'.format(old_games_string)

bot.updateAndMessage(message)