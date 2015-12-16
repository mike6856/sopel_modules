import os
from sopel.module import commands, priority


@commands('ow')
def open_windows(bot, trigger):
	open_windows =  os.popen('DISPLAY=:0 wmctrl -l').readlines()
	if len(open_windows) == 0:
		bot.say('No open windows')
		return
	for line in open_windows:
		title = line.split('ATXBawt')[1]
		bot.say(title)
	return

@commands('cw')
def close_window(bot, trigger):
	target = trigger.group(2).split(' ')[0]
	if target == 'all':
		bot.say('Closing all windows')
		open_windows =  os.popen('DISPLAY=:0 wmctrl -l').readlines()
		for line in open_windows:
			hex_val = line.split('0 ATXBawt')[0].strip()
			os.popen('DISPLAY=:0 wmctrl -ic "%s"' % hex_val)
	else:
		bot.say('Closing %s' % target)
		os.popen('DISPLAY=:0 wmctrl -c "%s"' % target)
	return

@commands('ls')
def launch_site(bot, trigger):
	target = trigger.group(2).split(' ')[0]
	bot.say('Launching site %s' % target)
	os.popen('DISPLAY=:0 chromium-browser -new-window %s &' % target)
	return

@commands('lyt')
def launch_youtube(bot, trigger):
	target = trigger.group(2).split(' ')[0]
	bot.say('Launching YouTube in TV MODE')
	url_pieces = target.split('/watch')
	new_url = '%s/tv#/watch%s' % (url_pieces[0], url_pieces[1])
	os.popen('DISPLAY=:0 chromium-browser -new-window %s &' % new_url)
	return

@commands('fw')
def focus_window(bot, trigger):
	target = trigger.group(2).split(' ')[0]
	bot.say('Focusing window %s' % target)
	os.popen('DISPLAY=:0 wmctrl -a %s &' % target)
	return

@commands('max')
def maximize_window(bot, trigger):
	bot.say('Maximizing current window')
	os.popen('DISPLAY=:0 wmctrl -r :ACTIVE: -b toggle,maximized_vert,maximized_horz &')
	return

@commands('kp', 'k')
def key_press(bot, trigger):
	target = trigger.group(2).split(' ')[0]
	bot.say('Pressing key: %s' % target)
	os.popen('DISPLAY=:0 xdotool key %s' % target)
	return
