
import os

from utils import list_tracks, exclude_tags, match_tags, \
                  match_any_tag

# plists = {'all_shuffle' : {'mode' : 'exclude',
#                            'tags' : ['protected']}}


class Plists_Generator():


    def __init__(self, audio_dirs, plist_dir,
                 plists, extensions=['.mp3', '.flac']):
        
        self.audio_dirs = audio_dirs
        self.plist_dir = plist_dir
        self.plists = plists
        self.extensions = extensions

        
    def _add_output_array(self):
        for fname in self.plists.keys():
            self.plists[fname]['tracks']=[]


    def _match_track_to_plist(self, track, fname):
        if self.plists[fname]['mode'] == 'match':
            if match_tags(track, self.plists[fname]['tags']):
                self.plists[fname]['tracks'].append(track)
        elif self.plists[fname]['mode'] == 'any':
            if match_any_tag(track, self.plists[fname]['tags']):
                self.plists[fname]['tracks'].append(track)
        

    def scan_audio_dirs_and_add_tracks(self):

        for folder in self.audio_dirs:

            for track in list_tracks(folder, self.extensions):
                
                for fname in self.plists.keys():
                    # add_to_plist(track, fname)
                    # self.plists[fname]['tracks'].append(track)
                    self._match_track_to_plist(track, fname)

                    
    def save_plists(self):

        for fname in self.plists.keys():

            fpath = os.path.join(self.plist_dir, fname + '.m3u8')

            tracks = [os.path.relpath(track, self.plist_dir)
                        for track in self.plists[fname]['tracks']]
            
            tracks = map(lambda x: x + '\n', tracks)

            
            with open(fpath, 'w') as file_m3u8:
                file_m3u8.writelines(tracks)

                    
    def generate(self):

        self._add_output_array()
        self.scan_audio_dirs_and_add_tracks()
        
        # for fname in self.plists.keys():
        #     print(self.plists[fname]['tracks'])

        # print(self.plists)


        self.save_plists()




