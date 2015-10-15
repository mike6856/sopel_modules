import os
import random
from sopel.module import commands, priority


def play_clip(clip_name):
	os.chdir('/home/atxbawt/Music')
	os.system('play -q -V0  %s &' % clip_name)
	#call(['play', clip_name])


@commands('shake','taylor','taytay')
def play_shake(bot, trigger):
	play_clip('shake_it_off_full.mp3')
	bot.say('Haters gonna hate, hate, hate, hate')
	return

@commands('fucked_up', 'fup')
def play_fup(bot, trigger):
	fk_versions = ['fdup1.wav', 'fdup2.wav', 'fdup3.wav',
			'fdup4.wav', 'fdup5.wav']
	play_version = random.choice(fk_versions)
	play_clip(play_version)
	if not trigger.group(2):
        	bot.say('Now you fucked up!')
		return
	target = trigger.group(2).split(' ')[0]
	bot.say('%s, now you fucked up!' % target)
	return

@commands('space')
def play_space(bot, trigger):
	play_clip('uspace.wav')
	bot.say('The United States of Space')
	return

@commands('out')
def play_out(bot, trigger):
	play_clip('out.wav')
	bot.say("Fuck this shit I'm out")
	return

@commands('mars')
def play_mars(bot, trigger):
	play_clip('mars.wav')
	bot.say('M A R S')
	return

@commands('down')
def play_down(bot, trigger):
	play_clip('down.wav')
	bot.say('PANIC')
	return

@commands('becks','und','undbecks','beerfest')
def play_und(bot, trigger):
        play_clip('undbecks.mp3')
        bot.say('Fourth best behind Steinemarzen, Rottenburger, und... und...')
        return

@commands('stfu', 'shutup')
def stfu(bot, trigger):
        os.system('pkill play')
        for winder in ['noon', 'hype']:
        	os.popen('DISPLAY=:0 wmctrl -c "%s"' % winder)
	play_clip('stfu.mp3')
	bot.say('Shut. The. Fuck. Up.')
	return
