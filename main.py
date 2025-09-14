import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QScreen
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
        self.setWindowTitle("Voice Assistant")

        # Add label
        self.label = QLabel("Type text below and click Speak:", self)
        self.label.move(20, 20)
        self.label.resize(300, 30)

        # Add text box
        self.textbox = QTextEdit(self)
        self.textbox.setGeometry(20, 60, self.width() - 40, 200)

        # Add Greet button
        self.greet_button = QPushButton("Greet Me", self)
        self.greet_button.setGeometry(20, 270, 100, 40)
        self.greet_button.clicked.connect(self.speaker.GreetUser)

    def speak_text(self):
        text = self.textbox.toPlainText().strip()
        if text:
            self.speaker.talk(text)  # synchronous (no threading)

# ---------- Run Application ----------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
