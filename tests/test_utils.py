# - *- coding: utf- 8 - *-

import unittest, os

from utils import list_tracks, get_orgtags


class Test_list_tracks(unittest.TestCase):

    def test_correct_result(self):

        directory = './samples'

        print(list_tracks(directory, ['.mp3']))

        self.assertTrue(True)


class Test_get_org_tags(unittest.TestCase):

    def test_get_tags_for_mp3(self):
        pass

    def test_get_tags_for_flac(self):
        pass

    def test_get_tags_for_non_musicbrainz(self):

        track = './samples/Ranma ½/Ranma ½ - Opening Theme (German).mp3'
        
        self.assertEqual(get_orgtags(track),
                         ['soundtrack', 'anime', 'nobrainz'])
