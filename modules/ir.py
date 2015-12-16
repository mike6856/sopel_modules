import requests
from sopel.module import commands, priority

@commands('tv_power')
def maximize_window(bot, trigger):
	bot.say('Toggling TV power')
    r = requests.post("http://192.168.1.38:5000/ir/tv/on")
	return
