import os
import random
import sopel.module
from sopel.module import commands,priority
from scapy.all import *

@commands('mousetrap', 'mt', 'mouse')
def mousetrap(bot, trigger):
    bot.say('Gotcha bitch!')
    os.popen('DISPLAY=:0 xdotool mousemove --sync 0 0')

