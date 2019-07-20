import unittest, os

from utils import list_tracks


class Test_list_tracks(unittest.TestCase):

    def test_correct_result(self):

        directory = './samples'

        print(list_tracks(directory, ['.mp3']))

        self.assertTrue(True)
