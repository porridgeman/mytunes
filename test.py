#!/usr/bin/env python

import time
from songplayer import SongPlayer

def handler(song_time):
	"""
	"""
	print("time: {}".format(int(song_time + 0.5)))

player = SongPlayer('Circles.mp3', callback=handler)
player.play()
time.sleep(10)
player.pause()
time.sleep(10)
player.play()
time.sleep(10)
