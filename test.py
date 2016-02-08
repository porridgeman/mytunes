#!/usr/bin/env python

import time
from songplayer import SongPlayer
import rethinkdb as r

def handler(song_time):
	"""
	"""
	# print("time: {}".format(int(song_time + 0.5)))
	r.table("controllers").get("now_playing").update({"time": song_time}).run(conn)

def create_tables(tables):
	"""
	"""
	existing_tables = r.table_list().run(conn)
	for table in tables:
		if table not in existing_tables:
			r.table_create(table).run(conn)


conn = r.connect( "rolandmechler.com", 28015, db="rmechler")

# print(r.db_list().run(conn))
print(r.table_list().run(conn))

create_tables(['songs', 'controllers'])

r.table("controllers").insert({
    "id": "now_playing",
    "title": "Circles",
    "time": 0,
    "playing": False
}, conflict="update").run(conn)

player = SongPlayer('Circles.mp3', callback=handler)
player.play()
time.sleep(10)
player.pause()
time.sleep(10)
player.play()
time.sleep(10)
