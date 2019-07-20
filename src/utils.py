
import sys, os

from mutagen.id3 import ID3
from mutagen.flac import FLAC


def list_tracks(directory, extensions):
    
    tracks = []


    def _is_audio_track(fname):
        return any(fname.endswith(e) for e in extensions)

    for root, subdirs, files in os.walk(directory):
        for item in filter(_is_audio_track, files):
            tracks.append(os.path.join(root, item))


    return tracks




def get_orgtags(track):

    _, extension = os.path.splitext(track)

    if extension=='.mp3':

        audio = ID3(track)

        try:
            orgtags = str(audio[u'TXXX:organization']).split('/')
        except KeyError:
            orgtags = ['']

    elif extension=='.flac':

        audio = FLAC(track)
        
        try:
            orgtags = audio[u'organization']
        except KeyError:
            orgtags = ['']

    else:
        raise Exception('Unrecognized extension ', extension)


    return orgtags





def exclude_tags(track, tags):

    assert type(tags)==list

    orgtags = get_orgtags(track)

    print(track)
    print(tags)
    print(orgtags)

    print(set(orgtags))
    print(set(tags))

    if set(orgtags).intersection(set(tags)):
        print('no match')
    else:
        print('match')

    print('\n')

