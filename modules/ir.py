import requests
from sopel.module import commands, priority
from sets import Set

def make_request(tail):
    url = 'http://192.168.1.38:5000/ir/%s' % tail
    r = requests.post(url)
    if 'okay' in r.text:
        return
    bot.say('IR Server is not happy')

@commands('tv')
def tv_power(bot, trigger):
    target = trigger.group(2).split(' ')[0]
    t = target.lower().strip()
    toggles = Set(['pwr', 'on', 'off', 'toggle'])
    channels = Set(['fox', 'nbc', 'cbs', 'bot', 'chrome'])
    if t in toggles:
        bot.say('Toggling TV power')
        make_request('tv/on')
    elif t in channels:
        bot.say('Changing TV to %s' % t)
        make_request('tv?channel=%s' % t)
    elif 'input' in t:
        bot.say('Next input')
        make_request('tv/input')
    else:
        bot.say('wut?')
    return

@commands('sound')
def soundbar_power(bot, trigger):
    target = trigger.group(2).split(' ')[0]
    t = target.lower().strip()
    toggles = Set(['pwr', 'on', 'off', 'toggle'])
    channel = Set(['optical', 'bot'])
    if t in toggles:
        bot.say('Toggling soundbar power')
        make_request('soundbar/on')
    elif t in channel:
        bot.say('Changing soundbar to %s' % t)
        make_request('soundbar?button=%s' % t)
    else:
        bot.say('wut?')
    return

@commands('vol')
def volume_commands(bot, trigger):
    target = trigger.group(2).split(' ')[0]
    t = target.lower()
    if 'up' in t or '+' in t :
        bot.say('Raising volume')
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
