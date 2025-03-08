
import sys
import os
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *

class MainWindow:
    def __init__(self, game):
        self.game = game
        self.app = QApplication(sys.argv)
        self.start_button = None
        self.main_window = None

    def run_ui(self):
        self.main_window = QtWidgets.QWidget()
        # self.main_window.setGeometry(120, 133, 1300, 700)
        self.main_window.setFixedSize(1700, 820)
        self.main_window.setWindowTitle('Cup Head')
        self.main_window.setObjectName('Hi')
        self.main_window.setWindowIcon(QtGui.QIcon("gameConcept\\icon.png"))
        bg_img = """
        #Hi{
        background-image: url(gameConcept/trungUI.jpg);
        background-repeat: no-repeat;
        background-position: center;
        }
        """
        self.main_window.setStyleSheet(bg_img)
        self.start_button = QtWidgets.QPushButton('S T A R T', self.main_window)
        self.start_button.resize(148, 140)
        self.start_button.move(809, 452)
        self.start_button.setStyleSheet(
                """QPushButton{
                background-color:#003d2e;
                color:white ;
                border:3px solid white;
                border-radius:64; font:22px
                }
                QPushButton:hover{
                background-color:#86234f;
                color:#fffff;
                border:4px solid white;
                }""")
        self.base_button = QtWidgets.QPushButton('Base', self.main_window)
        self.base_button.resize(130, 130)
        self.base_button.move(503, 462)
        self.base_button.setStyleSheet("""QPushButton{
                                       background-color:#003d2e; color:white ;border:3px solid white;
                                       border-radius:64; font:22px
                                       }
                QPushButton:hover{
                background-color:#86234f;
                color:#fffff;
                border:4px solid white;
                }
                                       """)
        
        self.top_button = QtWidgets.QPushButton('top', self.main_window)
        self.top_button.resize(130, 130)
        self.top_button.move(1134, 462)
        self.top_button.setStyleSheet("""QPushButton{
                                       background-color:#003d2e; color:white ;border:3px solid white;
                                       border-radius:64; font:22px
                                       }
                QPushButton:hover{
                background-color:#86234f;
                color:#fffff;
                border:4px solid white;
                }
                                       """)
        self.start_button.clicked.connect(lambda: [self.game.run_game(), self.main_window.hide()])
        self.base_button.clicked.connect(lambda: self.base_window())
        self.top_button.clicked.connect(lambda: self.top_window())
        self.main_window.show()
        self.app.exec_()

    def base_window(self):
        self.baseWindow = QtWidgets.QWidget()
        # self.baseWindow.setGeometry(429, 83, 881, 881)
        self.baseWindow.setFixedSize(881, 881)
        self.baseWindow.setWindowTitle('Base')
        self.baseWindow.setObjectName('i')
        self.baseWindow.setWindowIcon(QtGui.QIcon("gameConcept\\icon.png"))
        bg_img2 = """
                #i{
                background-image: url(gameConcept/cupmughead.png);
                background-repeat: no-repeat;
                background-position: center;
                }
                """
        self.baseWindow.setStyleSheet(bg_img2)

        # Add the missing buttons
        self.choice1_button = QtWidgets.QPushButton('', self.baseWindow)
        self.choice1_button.resize(450, 630)
        self.choice1_button.move(0, 253)
        self.choice1_button.setStyleSheet("""
            QPushButton{
            background:rgba(121,121,121, 0.5);
            color:#fff; 
            font-size:24px; 
            font-weight:500; 
            border:0px;
                }
                QPushButton:hover{
                background:none;
                color:#fff;
                border:10px solid #ffffff;
                border-radius:8px ;
                }
                """)

        self.choice2_button = QtWidgets.QPushButton('', self.baseWindow)
        self.choice2_button.resize(430, 629)
        self.choice2_button.move(450, 253)
        self.choice2_button.setStyleSheet("""
                QPushButton{
            background:rgba(121,121,121, 0.5);
            color:#fff; 
            font-weight:500; 
            border:0px;
                }
                QPushButton:hover{
                background:none;
                color:#fff;
                border:10px solid #ffffff;
                border-radius:8px ;
                }
                """)

        shadow = QtWidgets.QPushButton('', self.baseWindow)
        shadow.resize(889, 253)
        shadow.move(0, 0)
        shadow.setStyleSheet("""
            background:rgba(121,121,121, 0.5);
            color:#fff; 
            border:0px;
                        """)

        # Connect buttons to functions
        self.choice1_button.clicked.connect(lambda: [self.baseWindow.destroy(), self.game.run_game('cup_head')])
        self.choice2_button.clicked.connect(lambda: [self.baseWindow.destroy(), self.game.run_game('mugHead')])

        # Finally, show the window
        self.baseWindow.show()

    def top_window(self):
        # Create top window and set title and geometry
        self.top_window = QtWidgets.QWidget()
        self.top_window.setWindowTitle("Highest Score")
        self.top_window.setFixedSize(600, 600)
        
        # Set layout for the top window
        self.top_window.layout = QVBoxLayout()

        # Create score label
        self.top_window.score_label = QLabel("Highest Score: Loading...", self.top_window)
        self.top_window.score_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.top_window.layout.addWidget(self.top_window.score_label)
        self.top_window.setWindowIcon(QtGui.QIcon("gameConcept\\icon.png"))
        self.top_window.setObjectName('i')
        top_menu_score_img = """
                #i{
                background-image: url("gameConcept/top_menu_highest_score.png");
                background-repeat: no-repeat;
                background-position: center;
                }
                """
        self.top_window.setStyleSheet(top_menu_score_img)

        # Set the layout to the top window
        self.top_window.setLayout(self.top_window.layout)
        
        # Load the high score when the window is displayed
        self.load_high_score()

        self.top_window.show()

    def load_high_score(self):
        """Load and display the highest score."""
        if os.path.exists("high_score.txt"):
            with open("high_score.txt", "r") as file:
                score = file.read().strip()
                self.top_window.score_label.setText(f"Highest Score: {score}")
        else:
            self.top_window.score_label.setText("Highest Score: 0")
        self.top_window.score_label.setAlignment(QtCore.Qt.AlignCenter)
        self.top_window.score_label.setStyleSheet("font-size: 24px; font-weight: bold; color: black;")

