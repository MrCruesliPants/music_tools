
import unittest, os

from src.write_plists import Plists_Generator


class Test_Plists_Generator(unittest.TestCase):

    def test_run(self):

        dirs = ['samples/']

        plists = {'soundtrack_all'  : {'mode' : 'match',
                                       'tags' : ['soundtrack']},
                  'soundtrack_anime': {'mode' : 'match',
                                       'tags' : ['soundtrack', 'anime']}}


        PG = Plists_Generator(dirs, 'output', plists,
                              extensions=['.mp3', '.flac'])

        PG.generate()
        # print(list_tracks(directory, ['.mp3']))

        # self.assertTrue(True)
