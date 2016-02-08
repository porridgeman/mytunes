import time
import pyglet
pyglet.options['audio'] = ('openal', 'silent')
# pyglet.options['debug_media'] = True

import pyglet.media

from threading import Thread

class SongPlayer(object):
    """
    """

    def __init__(self, filename=None, song=None, callback=None):
        """
        """
        self.player = pyglet.media.Player()
        filename = filename if filename else song['filename']
        self.source = pyglet.media.load(filename)
        self.song = song if song else self.get_song(filename)
        
        self.player.queue(self.source)

        if callback:
            self.callback = callback
            t = Thread(target=self.poller, args = (self.player, self.song))
            t.daemon = True # TODO: ???
            t.start()

    def poller(self, player, song):
        while True:
            self.callback(self.song, player.time, player.playing)
            time.sleep(1)

    def get_song(self, filename):
        """
        """
        return {
            "filename": filename,
            "duration": self.source.duration,
            "title": self.source.info.title,
            "artist": self.source.info.author,
            "album": self.source.info.album
        }

    def play(self):
        """
        """
        self.player.play()


    def pause(self):
        """
        """
        self.player.pause()


