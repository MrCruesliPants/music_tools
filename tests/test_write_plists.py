
import unittest, os

from src.write_plists import write_plists


class Test_ist_tracks(unittest.TestCase):

    def test_run(self):

        dirs = ['./samples']

        write_plists(dirs, '', extensions=['.mp3', '.flac'])

        # print(list_tracks(directory, ['.mp3']))

        self.assertTrue(True)
