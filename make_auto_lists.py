
from src.write_plists import Plists_Generator


base = '/media/fh/94ed305a-e630-4f3e-9aff-32995da5fb03/home/fh/'

audio_dirs = [base+'audio/artists',
              base+'audio/soundtracks',
              base+'audio/still_sort',
              base+'audio/tmp']

plist_dir = base + 'audio/playlists/generic_[new]'


plists = {'shfx'           : {'mode' : 'exclude',
                              'tags' : ['soundtrack']},
          'deutsch'        : {'mode' : 'match',
                              'tags' : ['deutsch']},
          'deutsch_hip-hop': {'mode' : 'match',
                              'tags' : ['deutsch', 'hip-hop']},
          'other-lang'     : {'mode' : 'match',
                              'tags' : ['other_lang']},
          '8bit'          : {'mode' : 'any',
                              'tags' : ['bit', 'bittunes', '8bit']},
          'fantasy'        : {'mode' : 'match',
                              'tags' : ['fantasy']},
          'french'         : {'mode' : 'match',
                              'tags' : ['french']},
          'indian'         : {'mode' : 'match',
                              'tags' : ['indian']},
          'folk'           : {'mode' : 'match',
                              'tags' : ['folk']},
          'trance'         : {'mode' : 'match',
                              'tags' : ['trance']},
          'hip-hop'        : {'mode' : 'match',
                              'tags' : ['hip-hop']},
          'piano'          : {'mode' : 'match',
                              'tags' : ['piano']},
          'hipster'        : {'mode' : 'match',
                              'tags' : ['hipster']},
          'nocopyright'    : {'mode' : 'match',
                              'tags' : ['nocopyright']},
          'post-rock'      : {'mode' : 'match',
                              'tags' : ['post-rock']},
          'truehiphop'     : {'mode' : 'match',
                              'tags' : ['truehiphop']},
          'soundtrack'       : {'mode' : 'match',
                                'tags' : ['soundtrack']},
          'soundtrack_games' : {'mode' : 'match',
                                'tags' : ['soundtrack','game']},
          'soundtrack_movie' : {'mode' : 'match',
                                'tags' : ['soundtrack', 'movie']},
          'soundtrack_anime' : {'mode' : 'match',
                                'tags' : ['soundtrack', 'anime']},
          'soundtrack_tv'    : {'mode' : 'match',
                                'tags' : ['soundtrack', 'tv']},
          'gx_cyberpunk'     : {'mode' : 'match',
                                'tags' : ['cyberpunk']}}



PG = Plists_Generator(audio_dirs, plist_dir, plists,
                      extensions=['.mp3', '.flac'])

PG.generate()
