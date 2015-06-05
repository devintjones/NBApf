# scrapes espn for nba stats by team code
# gets roster and player stats

# author: Devin Jones
# date: 6/4/2015

import urllib
from bs4 import BeautifulSoup
import re
import MySQLdb



def main():

	team_codes = ['cle','gsw']
	team_codes = ['cle']

	rosters = []
	stats   = []
	for code in team_codes:

		roster = get_roster(code)
		rosters.append(roster)
		
		for player in roster:
			stats.append(get_stats(player.get('player_url')))

	return


db  = MySQLdb.connect(user="root",passwd="root",db="NBAPF")


def load_roster(roster):
	
	for_insert = [(player.get("PID"),
		       player.get("NAME"),
		       player.get("TEAM")) for player in roster]
	
	c   = db.cursor()
	c.executemany("""INSERT INTO PLAYERS (PID,NAME,TEAM)
			VALUES (%s, %s, %s)""", for_insert)
	c.close()
	return

def load_stats(stat):

	for_insert = [(row.get("PID"),
			row.get('DATE').split(' ')[-1] + '/15',
			row.get('PTS'),
			row.get('STL'),
			row.get('REB'),
			row.get('AST')) for row in stat]
	c = db.cursor()
	c.executemany("""INSERT INTO STATS (PID, GAMEID, POINTS, STEALS, REBOUNDS, ASSISTS)
			VALUES ( %s, %s, %s, %s, %s, %s)""", for_insert)
	c.close()
	return


def get_roster(team_code):
	baseurl = 'http://espn.go.com/nba/team/roster/_/name/{}'.format(team_code)
	html    = urllib.urlopen(baseurl)
	soup = BeautifulSoup(html)
	
	# need bs4.2 to search class attr
	head_row = soup.find_all('tr',class_=re.compile('colhead'))[0]
	headers  = [entry.get_text() for entry in head_row.find_all('td')]
	
	players = []
	for tag in soup.find_all('tr',class_=re.compile('player')):
		
		player_info = {'TEAM':team_code}
		for idx,entry in enumerate(tag.find_all('td')):
			player_info[headers[idx]] = entry.get_text()

		player_link = tag.find_all('a')[0].get('href')
		player_id   = player_link.split('/')[-2]

		player_info['player_url'] = player_link
		player_info['PID']  = player_id

		players.append(player_info)
	
	return players

def get_stats(player_url,full_stats=False):
	
	player_id   = player_url.split('/')[-2]

	# will get most recent 5 games without this
	# haven't tested this page format
	if full_stats:
		player_url.replace('player/','player/gamelog/')
	
	html = urllib.urlopen(player_url)
	soup = BeautifulSoup(html)

	head_row = soup.find_all('tr',class_=re.compile('colhead'))[2]
	headers  = [entry.get_text() for entry in head_row.find_all('th')]

	stats = []
	for tag in soup.find_all('tr',class_=re.compile('team')):
		
		game_stats = {'PID':player_id}
		for idx,entry in enumerate(tag.find_all('td')):
			game_stats[headers[idx]] = entry.get_text()
		
		stats.append(game_stats)

	return stats


if __name__ == 'main':
	main()
	pass
