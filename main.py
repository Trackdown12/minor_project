import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QScreen,QFont,QIcon
from PyQt5.QtWidgets import QLabel, QPushButton, QTextEdit
from VOICE import *
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.speaker = speak()

        # Get screen size
        screen = app.primaryScreen()
        size = screen.size()
        screen_width = size.width()
        screen_height = size.height()

        # Set window size to half of screen
        self.setGeometry(
            screen_width // 4, 
            screen_height // 4, 
            screen_width // 2, 
            screen_height // 2
        )
        self.setWindowTitle("InstagramSpamDetector")
        # Set Instagram icon (make sure you have a .ico or .png file)
        self.setWindowIcon(QIcon("Instagram icon.png"))  # path to your icon


        # Add label
        self.label = QLabel("Greetings User check the spam ", self)
        self.label.move(20, 20)
        self.label.resize(300, 30)
        
        # Using QFont
        font = QFont("Arial", 14)      # font family Arial, size 14
        font.setBold(True)              # make it bold
        self.label.setFont(font)

        # Optional: color using setStyleSheet
        self.label.setStyleSheet("color: blue;")

        # Add text box
        self.textbox = QTextEdit(self)
        self.textbox.setGeometry(60, 60, 500,50)

        # Add Greet button
        self.greet_button = QPushButton("Greet Me", self)
        self.greet_button.setGeometry(20, 270, 100, 40)
        self.greet_button.clicked.connect(self.speaker.GreetUser)

# ---------- Run Application ----------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
