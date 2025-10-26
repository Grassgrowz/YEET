import os
import pandas as pd
from pathlib import Path
from tinytag import TinyTag

# root_directory = Path(__file__).parent
# music_directory = root_directory / "music"

music_directory = "/home/misha/Music"


root_list = [] # album path
dirs_list = [] # useless
files_list = [] # album image, not the full path yet
first_songs = [] # list of first songs in suitable directories
artists = [] # list of artists
albums = []

# walk thru music directory and append to lists directory info where a directory has both audio and image files
for (root,dirs,files) in os.walk(music_directory, topdown=True):
    if (any(f.lower().endswith(('.mp3', '.flac', '.opus', '.wav', '.m4a')) for f in files) and any(f.lower().endswith(('.jpg', '.jpeg', '.png')) for f in files)):
        root_list.append(root)
        dirs_list.append(dirs)
        tempfiles_list = [item for item in files if item.lower().endswith(('.jpg', '.jpeg', '.png'))]
        if 'cover.jpg' in tempfiles_list: # check for lower case covers with different endings
            files_list.append('cover.jpg')
        elif 'cover.jpeg' in tempfiles_list:
            files_list.append('cover.jpeg')
        elif 'cover.png' in tempfiles_list:
            files_list.append('cover.png')
        elif 'cover.JPG' in tempfiles_list:
            files_list.append('cover.JPG')
        elif 'Cover.jpg' in tempfiles_list: # check for capital case covers with different endings
            files_list.append('Cover.jpg')
        elif 'Cover.jpeg' in tempfiles_list:
            files_list.append('Cover.jpeg')
        elif 'Cover.png' in tempfiles_list:
            files_list.append('Cover.png')
        elif 'Cover.JPG' in tempfiles_list:
            files_list.append('Cover.JPG')
        else:
            files_list.append(tempfiles_list[0])

        # add first song name of suitable directory to the list
        tempsong_list = [item for item in files if item.lower().endswith(('.mp3', '.flac', '.opus', '.wav', '.m4a'))]
        first_songs.append(tempsong_list[0]) # only take the first song of the list


# combine album path and song name into a working path
fullsongpath = [f"{x}/{y}" for x, y in zip(root_list, first_songs, strict=True)] # ensures both lists are equal length


# get artist info
for x in fullsongpath:


    try:
        audio = TinyTag.get(x) # get artist via tag
        artists.append(audio.artist.strip())

    except:
        fallback_artist_path: str = os.path.dirname(os.path.dirname(x)) # get tag via folder of folder name lolol
        artists.append(fallback_artist_path.split("/")[-1]) # remove everything before the last /


# get album info
for x in fullsongpath:


    try:
        audio = TinyTag.get(x) # get album via tag
        albums.append(audio.album.strip())

    except:
        fallback_album_path: str = os.path.dirname(x) # get tag via folder name lolol
        albums.append(fallback_album_path.split("/")[-1]) # remove everything before the last /






df = pd.DataFrame()
df['albumPath'] = root_list
df['image'] = files_list
df['imagePath'] = df['albumPath'] + "/" + df['image']
df['artist'] = artists
df['album'] = albums

df.to_csv('table.csv')




