
from utils import list_tracks, get_orgtags, exclude_tags

plists = {'8bit' : '8bit',
          'soundtracks' : 'soundtrack'}



def write_plists(audio_dirs, plist_dir, extensions=['.mp3', '.flac']):

    not_soundtrack = []

    for folder in audio_dirs:

        for track in list_tracks(folder, extensions):

            if not exclude_tags(track, ['soundtrack']):
                not_soundtrack.append(track)


        
    print(not_soundtrack)


