import time
import pyglet
pyglet.options['audio'] = ('openal', 'silent')
# pyglet.options['debug_media'] = True

import pyglet.media

from Queue import Queue
from threading import Thread

class SongPlayer(object):
	"""
	"""

	def __init__(self, filename):
		"""
		"""
		self.player = pyglet.media.Player()
		self.player.queue(pyglet.media.load(filename))

		self.queue = Queue()

		t = Thread(target=self.poller, args = (self.player,))
		t.daemon = True # TODO: ???
		t.start()

	def poller(self, player):
		while True:
			command = self.queue.get()
			if command == "play":
				while True:
					if not self.queue.empty():
						command = self.queue.get()
						if command and command == "pause":
							break

					time.sleep(1)
					print(player.time)

	def play(self):
		"""
		"""
		self.player.play()
		self.queue.put("play")
		# self.playing = self.player.play()

	def pause(self):
		"""
		"""
		self.player.pause()
		self.queue.put("pause")

