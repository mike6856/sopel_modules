import requests
from sopel.module import commands, priority
from sets import Set

def make_request(tail):
    url = 'http://192.168.1.38:5000/ir/%s' % tail
    r = requests.post(url)
    print r
    print r.text
    return

@commands('tv')
def tv_power(bot, trigger):
    target = trigger.group(2).split(' ')[0]
    t = target.lower()
    toggles = Set(['pwr', 'on', 'off', 'toggle'])
    if t in toggles:
        bot.say('Toggling TV power')
        make_request('tv/on')
    return

@commands('sound')
def soundbar_power(bot, trigger):
    target = trigger.group(2).split(' ')[0]
    t = target.lower()
    toggles = Set(['pwr', 'on', 'off', 'toggle'])
    if t in toggles:
        bot.say('Toggling soundbar power')
        make_request('soundbar/on')
    return

@commands('vol')
def volume_commands(bot, trigger):
    target = trigger.group(2).split(' ')[0]
    t = target.lower()
    if 'up' in t or '+' in t :
        bot.say('Lowering volume')
        make_request('soundbar?button=vol_up')
    elif 'down' in t or '-' in t:
        bot.say('Lowering volume')
        make_request('soundbar?button=vol_down')
    elif 'mute' in t:
        bot.say('Muting soundbar')
        make_request('soundbar?button=mute')
    else:
        bot.say('wut?')
    return
