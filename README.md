# YEET
a pyside6 based program that has the user guess the artist and album name based on the album cover, using data sourced from a offline music collection. a supplementary script constructs a csv database of the music on the computer.

abstract: program chooses a random album from my music collection and displays the album art (only choose song files that have album art). beneath the image, there are two buttons: "reveal artist", and "reveal "album", where upon pressing them, the information appears in a label widget between the image and the buttons. I will use this program to see how many artistnames or albumnames i can remember just by looking at the art.

<div align="center">
<img width="560" height="663" alt="image" src="https://github.com/user-attachments/assets/54e50150-1103-4adb-8411-9b70eac4f291" />
</div>

## scouter.py
This script uses os.walk() to look through my music folder and look for folders that have both an image file and an audio file in a folder, and saving various info about that into a csv table. Each row in this csv represents an album/EP in the music collection. From this data the musicGuesser.py will grab its info. This script needs to be run first to construct a table.csv before launching the actual musicGuesser.py file.
<img width="1222" height="671" alt="image" src="https://github.com/user-attachments/assets/3efaca1c-a194-4c7a-bad1-5a8dbbbabb7c" />


## musicGuesser.py
This is the main file. It will show a pyside6 GUI, showing an image, and having the user attempt to remember the artist name and album name. To see if remembred correctly, user can reveal the artist/album labels. Additional functionality like opening the file location to check out the files, and being able to click the image to have it play a random song from that directory with the default music player on the computer.
