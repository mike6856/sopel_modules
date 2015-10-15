from bs4 import BeautifulSoup
import sys
import re
import subprocess
import pprint
from sopel.module import commands, priority


def run_distance(address):
	egress = '5200+Duval+St,+Austin,+TX+78751'
        ingress = re.sub(' ', '+', address)

	url = 'https://www.google.com/maps/dir/%s/%s' % (egress, ingress)
	#print url

	subprocess.call("phantomjs /home/atxbawt/.sopel/eta/advanced.js %s" % url, shell=True)

	html = open('/home/atxbawt/.sopel/eta/result.html', 'r')
	soup = BeautifulSoup(html)

	all_text = soup.get_text().split('\n')
	chop_front = all_text[-1].split('No Routes Found.')[1]
	chunkz = chop_front.split('CONFIDENTIAL')
	routeNtime = chunkz[0].strip()
	distance = chunkz[1].strip().split(' ')
	say = '%s %s %s' %(distance[-2], distance[-1], routeNtime)
	return say

@commands('eta')
def eta(bot, trigger):
	destination = trigger.group(2)
	result = run_distance(destination)
	bot.say(result)
	return
