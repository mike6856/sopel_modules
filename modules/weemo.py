import os

from sopel.module import commands, priority
from sets import Set


@commands('let', 'weemo', 'outlet', 'light')
def toggle_weemo(bot, trigger):
    target = trigger.group(2).split(' ')[0]
    t = target.lower().strip()
    onset = Set(['there', 'on'])
    if t in onset:
        bot.say('Turning weemo on')
        os.popen('wemo switch "perimeter" on &')
        return
    elif t == 'off':
        bot.say('Turning weemo off')
        os.popen('wemo switch "perimeter" off &')
        return
    elif t == 'status':
        wee_status =  os.popen('wemo -v switch "perimeter" status').readlines()
        bot.say('Weemo is %s' % wee_status)
        return
    else:
        bot.say('wut?')
