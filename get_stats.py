# scrapes espn for nba stats by team code
# gets roster and player stats

# author: Devin Jones
# date: 6/4/2015

import json
import urllib
from bs4 import BeautifulSoup
import re
import MySQLdb
import random


try:
	with open("connection_params.json","r") as infile:
		connection_params = json.load(infile)
except:
	SystemExit("couldnt find connection params file")

db = MySQLdb.connect(**connection_params)


def main():
	insert_player_stats()
	update_player_vals()
	generate_pf()
	calc_pf_value()
	return


# TODO make sure to only insert new games
# TODO retreive player codes from db and then iterate
def insert_player_stats():

	team_codes = ['cle','gsw']

	rosters = []
	stats   = []
	for code in team_codes:

		roster = get_roster(code)
		load_roster(roster)
		rosters.append(roster)
		
		for player in roster:
			stat = get_stats(player.get('player_url'))
			load_stats(stat)
			stats.append(stat)
	return


# compute sum of indices over average stats
def update_player_vals():
	
	c = db.cursor()
	c.execute("truncate table PLAYER_VALS;")
	db.commit()

	c.execute("""insert into PLAYER_VALS
		SELECT s.PID, 
		       AVG(s.POINTS)/a.AVG_POINTS + 
		       AVG(s.STEALS)/a.AVG_STEALS +
		       AVG(s.ASSISTS)/a.AVG_ASSISTS +
		       AVG(s.REBOUNDS)/a.REBOUNDS as VALUE
		FROM STATS s, (SELECT AVG(POINTS) AVG_POINTS, 
				       AVG(STEALS) AVG_STEALS, 
				       AVG(ASSISTS) AVG_ASSISTS, 
				       AVG(REBOUNDS) REBOUNDS 
				FROM STATS) a
		GROUP BY s.PID;""")
	db.commit()
	c.close()
	return


# sample users for the project
def generate_users():
	c = db.cursor()
	for i,name in enumerate(['Mike','Sarah','John','Michelle']):
		c.execute("""insert into USERS (UID,NAME)
				values ('{}','{}')""".format(i,name))
		db.commit()
	c.close()
	return


# sample portfolio selection for the project
def generate_pf():
	c = db.cursor()
	
	c.execute('truncate table PF;')
	db.commit()

	c.execute('select UID from USERS;')
	users = [user[0] for user in c.fetchall()]
	
	c.execute('select PID from PLAYERS;')
	players = [player[0] for player in c.fetchall()]
	
	for user in users:
		selection = random.sample(range(len(players)),5)
		for_insert = [(user,players[idx]) for idx in selection]
		c.executemany('''insert into PF
				values (%s,%s)''',for_insert)
		db.commit()
	c.close()
	return


# calculate portfolio value based on player valuations and user selected portfolio
def calc_pf_value():
	c = db.cursor()
	c.execute('truncate table PF_VALUE;')
	db.commit()

	c.execute('''insert into PF_VALUE
			select a.UID, sum(b.VALUE) as VALUE
			from PF a
			inner join PLAYER_VALS b
			on a.PID = b.PID
			group by a.UID''')
	db.commit()
	c.close()
	return


def load_roster(roster):
	
	for_insert = [(player.get("PID"),
		       player.get("NAME"),
		       player.get("TEAM")) for player in roster]
	
	c   = db.cursor()
	c.executemany("""INSERT INTO PLAYERS (PID,NAME,TEAM)
			VALUES (%s, %s, %s)""", for_insert)
	db.commit()
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
	db.commit()
	c.close()
	return


# gets roster by team code
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


# TODO generate url based on PID
# gets stats on a per player basis
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
