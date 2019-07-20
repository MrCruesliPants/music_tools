
import os

from src.utils import list_tracks, get_orgtags

fpath = os.getcwd()

extensions = ['.mp3', '.flac']

tracks = list_tracks(fpath, extensions)

for track in tracks:
    print(get_orgtags(track))


