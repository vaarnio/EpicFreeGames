import epic
import bot

message = ''.join([epic.offerToString(offer) + '\n' for offer in epic.getFree()])
bot.updateAndMessage(message)