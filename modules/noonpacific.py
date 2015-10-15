import os
from time import sleep
import random
from sopel.module import commands, priority
try:
	import simplejson as json
except:
	import json

NOON_FILE = '/home/atxbawt/Music/noonpacific.json'

def key_press(bot, key):
	bot.say('Pressing key: %s' % key)
	os.popen('DISPLAY=:0 xdotool key %s' % key)
	return

@commands('mixnext', 'mixprev', 'mixskip')
def skip(bot, trigger):
	command = {'mixnext': 'next', 'mixskip': 'next', 'mixprev': 'prev'}.get(trigger.group(1))
        open_windows =  os.popen('DISPLAY=:0 wmctrl -l').readlines()
        if len(open_windows) == 0:
        	bot.say('No open windows')
		return
	else:
		for window in open_windows:
			if 'noon' in window.lower():
				mix = 'noon'
			elif 'hype' in window.lower():
				mix = 'hype'
        coords = {'noon': {'prev': {'x': '900', 'y': '1050'}, 'next': {'x': '1000', 'y': '1050'}},
		'hype': {'prev': {'x': '450', 'y': '160'}, 'next': {'x': '525', 'y': '160'}}}
        bot.say('Moving to the %s track on %s' % (command, mix.title()))
	os.popen('DISPLAY=:0 xdotool mousemove --sync %s %s' % (coords[mix][command]['x'], coords[mix][command]['y']))
        os.popen('DISPLAY=:0 xdotool click 1')

# Noon pacific is stupid and mix # != number in URL
def get_noon_translation(noon_file):
	with open(noon_file) as f:
		noon_json = json.loads(f.read())
	return noon_json

@commands('np', 'noon', 'noonpacific')
def noon_pacific(bot, trigger):
        noon_base_url = 'http://noonpacific.com/'
        try:
        	target = trigger.group(2).split(' ')[0].zfill(3)
                noon_json = get_noon_translation(NOON_FILE)
                mix_target = noon_json[target]
                mix_url = '%s%s' % (noon_base_url, mix_target)
        except:
		target = 'latest'
                mix_url = noon_base_url
        bot.say('Launching Noon Pacific mix: %s' % target)
        os.popen('DISPLAY=:0 chromium-browser -new-window %s &' % mix_url)
        sleep(5)
        key_press(bot, 'space')
        return

@commands('hype', 'hm', 'stack')
def hype_stack(bot, trigger):
        noon_base_url = 'http://hypem.com/stack/'
        try:
                target = trigger.group(2).split(' ')[0]
                mix_url = '%s%s' % (noon_base_url, target)
        except:
                target = 'latest'
                mix_url = noon_base_url
        bot.say('Launching Hype Machine Stack mix: %s' % target)
        os.popen('DISPLAY=:0 chromium-browser -new-window %s &' % mix_url)
        sleep(5)
        key_press(bot, 'space')
        return
