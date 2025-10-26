import sys
import os
import subprocess
from PySide6 import QtWidgets, QtCore, QtGui
import pandas as pd
import random

database = "/home/misha/Documents/python/pyside6_musicImageGuesser/table.csv"


class MusicGuesser(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QtGui.QIcon("/home/misha/Documents/python/pyside6_musicImageGuesser/icon.png"))

        self.initial_D()
        self.choose_n_cruise_initial()

        self.setWindowTitle("music guesser 3000!!")
        self.resize(550, 600)
        self.move(650,150)

        vbox = QtWidgets.QVBoxLayout()
        self.setLayout(vbox)


        # QHbox for artist n album label
        row0 = QtWidgets.QHBoxLayout()
        vbox.addLayout(row0)

        # artist n label font stuff
        toplabels = QtGui.QFont()
        toplabels.setPointSize(18)
        toplabels.setBold(True)
        toplabels.setItalic(True)
        

        # artist label
        self.artist_label = QtWidgets.QLabel(self.artist_name)
        self.artist_label.setAlignment(QtCore.Qt.AlignCenter)
        self.artist_label.setFont(toplabels)
        self.artist_label.setStyleSheet("color: purple;")
        row0.addWidget(self.artist_label)

        # inbetween empty label so that the aligns of artist and album labels dont yeet to the edge
        # self.bar_seperator = QtWidgets.QLabel("")
        # self.bar_seperator.setAlignment(QtCore.Qt.AlignCenter)
        # row0.addWidget(self.bar_seperator)

        # album label
        self.album_label = QtWidgets.QLabel(self.album_name)
        self.album_label.setAlignment(QtCore.Qt.AlignCenter)
        self.album_label.setFont(toplabels)
        self.album_label.setStyleSheet("color: yellow;")
        row0.addWidget(self.album_label)

        
        class ClickableLabel(QtWidgets.QLabel): #custom QLabel subclass to include signal for clicked.event for label which usually doesnt exist
            clicked = QtCore.Signal()  # Custom signal

            def mousePressEvent(self, event):
                if event.button() == QtCore.Qt.LeftButton:
                    self.clicked.emit()
                super().mousePressEvent(event)  # Keep default behavior (e.g., drag)


        # image
        self.image = ClickableLabel()
        self.pixmap = QtGui.QPixmap(self.Image_with_path).scaled(500, 500)
        self.image.setPixmap(self.pixmap)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        vbox.addWidget(self.image)
        self.image.clicked.connect(self.image_click)

        
        # manybutton row 1
        row1 = QtWidgets.QHBoxLayout()
        vbox.addLayout(row1)

        self.artist_button = QtWidgets.QPushButton("reveal artist")
        self.artist_button.setStyleSheet('background-color: green; color:yellow; border: 2px solid green;border-radius: 6px;font-size: 22px;font-family: MathJax_Typewriter;')
        row1.addWidget(self.artist_button)
        self.artist_button.clicked.connect(self.revelio_artist)

        self.album_button = QtWidgets.QPushButton("reveal album")
        self.album_button.setStyleSheet('background-color: green; color:yellow; border: 2px solid green;border-radius: 6px;font-size: 22px;font-family: MathJax_Typewriter;')
        row1.addWidget(self.album_button)
        self.album_button.clicked.connect(self.revelio_album)



        # manybutton row 2
        row2 = QtWidgets.QHBoxLayout()
        vbox.addLayout(row2)

        self.random_button = QtWidgets.QPushButton("random")
        self.random_button.setStyleSheet('background-color: purple; color:black; border: 2px solid purple; border-radius: 6px;font-size: 22px;font-family: MathJax_Typewriter;')
        self.random_button.clicked.connect(self.choose_n_cruise_after)
        row2.addWidget(self.random_button)


        self.open_filepath_button = QtWidgets.QPushButton("open in file manager")
        self.open_filepath_button.setStyleSheet('background-color: purple; color:black; border: 2px solid purple; border-radius: 6px;font-size: 22px;font-family: MathJax_Typewriter;')
        self.open_filepath_button.clicked.connect(self.open_filepath)
        row2.addWidget(self.open_filepath_button)

        

        
        self.hide_yo_kids_hide_yo_wives()

    def open_filepath(self):
        subprocess.call(["xdg-open", self.album_path])

    def image_click(self):
        dirContent = os.listdir(self.album_path)
        ls: list = [item for item in dirContent if item.lower().endswith(('.mp3', '.flac', '.opus', '.wav', '.m4a'))]
        print(ls,"\n")
        randSong: str = random.choice(ls)
        randSongPath: str = self.album_path + "/" + randSong
        print(randSongPath)
        subprocess.call(["xdg-open", randSongPath])


    def initial_D(self): #startup procedures, scan csv file, find out number of rows, display info

        self.df = pd.read_csv(database)

        print("scanning database length...")
        self.amount_of_rows = int(len(self.df)) #amount of rows in df
        
        print(f"{self.amount_of_rows} total rows in database.")


    def revelio_artist(self): # reveal artist button function
        self.artist_label.setHidden(False)

    def revelio_album(self): # reveal album button function
        self.album_label.setHidden(False)


    def hide_yo_kids_hide_yo_wives(self): 
        self.artist_label.setHidden(True)
        self.album_label.setHidden(True)

    def choose_n_cruise_initial(self): # chooses random row from df, turns it into a dict 

        random_pick_number = random.randint(0, self.amount_of_rows) # pick random number between 1 and max row number

        print(f"picked entry #{random_pick_number}")
        chosen_data = self.df.iloc[random_pick_number].to_dict() # data entry of chosen number row as dict
        print(chosen_data)

        self.artist_name = chosen_data["artist"]
        self.album_name = chosen_data["album"]

        self.album_path = chosen_data["albumPath"]
        self.image_name = chosen_data["image"]
        self.Image_with_path = self.album_path + "/" + self.image_name



    def choose_n_cruise_after(self): # chooses random row from df, turns it into a dict 

        random_pick_number = random.randint(0, self.amount_of_rows) # pick random number between 1 and max row number

        print(f"picked entry #{random_pick_number}")
        chosen_data = self.df.iloc[random_pick_number].to_dict() # data entry of chosen number row as dict
        print(chosen_data)

        self.artist_name = chosen_data["artist"]
        self.album_name = chosen_data["album"]

        self.album_path = chosen_data["albumPath"]
        self.image_name = chosen_data["image"]
        self.Image_with_path = self.album_path + "/" + self.image_name


        self.temp_pixmap = QtGui.QPixmap(self.Image_with_path).scaled(500, 500)
        self.image.setPixmap(self.temp_pixmap)

        self.artist_label.setText(self.artist_name)
        self.album_label.setText(self.album_name)

        self.hide_yo_kids_hide_yo_wives()



if __name__== "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MusicGuesser()
    window.show()
    sys.exit(app.exec())