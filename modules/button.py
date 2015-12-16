import os
import random
import sopel.module
from scapy.all import *
from sopel.module import commands, priority

@sopel.module.commands("dash")
@sopel.module.thread(True)
def dash_sniff(bot, trigger):
    def play_clip(clip_name):
        os.chdir('/home/atxbawt/Music')
        os.system('play -q -V0  %s &' % clip_name)

    def play_fup(bot):
            fk_versions = ['fdup1.wav', 'fdup2.wav', 'fdup3.wav',
                             'fdup4.wav', 'fdup5.wav']
            play_version = random.choice(fk_versions)
            play_clip(play_version)
            bot.say('You have fucked up now!')
            return

    def arp_display(pkt):
        if pkt.haslayer(ARP):
            if pkt[ARP].op == 1: #who-has (request)
                if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
                    if pkt[ARP].hwsrc == '74:75:48:5f:99:30': # Huggies
                        bot.say('Pushed Huggies')
                    elif pkt[ARP].hwsrc == '10:ae:60:00:4d:f3': # Elements
                        bot.say('Pushed Elements')
                    elif pkt[ARP].hwsrc == 'a0:02:dc:73:49:f9': # OLAY
                        play_fup(bot)
                    else:
                        bot.say('ARP Probe from unknown device: ' + pkt[ARP].hwsrc)

    bot.say('Dash starting.')
    sniff(prn=arp_display, filter="arp", store=0, count=0)
