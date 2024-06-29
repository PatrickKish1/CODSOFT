import sys
import random
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLabel,
    QTableWidget, QTableWidgetItem, QMessageBox
)
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon

class RPSGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rock-Paper-Scissors Game")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet(open('styles.qss').read())

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Create buttons
        self.buttons_layout = QHBoxLayout()
        self.layout.addLayout(self.buttons_layout)

        self.rock_button = self.create_button(r"./rock_icon.ico")
        self.paper_button = self.create_button(r"./paperHand.ico")
        self.scissors_button = self.create_button(r"./scissors.ico")

        self.buttons_layout.addWidget(self.rock_button)
        self.buttons_layout.addWidget(self.paper_button)
        self.buttons_layout.addWidget(self.scissors_button)

        self.result_label = QLabel()
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.result_label)

        # Create table for score tracking
        self.score_table = QTableWidget(0, 3)
        self.score_table.setHorizontalHeaderLabels(["Player Score", "Computer Score", "Game Round"])
        self.layout.addWidget(self.score_table)

        # Set column widths
        self.score_table.setColumnWidth(0, 150)
        self.score_table.setColumnWidth(1, 150)
        self.score_table.setColumnWidth(2, 150)

        self.score_user = 0
        self.score_computer = 0
        self.game_round = 1
        self.max_score = 5

    def create_button(self, icon_path):
        button = QPushButton()
        button.setMinimumSize(QSize(150, 100))
        button.setIcon(QIcon(icon_path))
        button.setIconSize(QSize(50, 50))
        button.clicked.connect(lambda: self.play(icon_path.split('.')[0]))
        return button

    def play(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            result = "You win! 👍🎉"
            self.score_user += 1
        else:
            result = "You lose! 👎❌"
            self.score_computer += 1

        self.result_label.setText(result)
        self.check_game_end()

    def check_game_end(self):
        if self.score_user >= self.max_score or self.score_computer >= self.max_score:
            if self.score_user >= self.max_score:
                message = "You win! 🎉👍"
                button_text = "New Game"
            else:
                message = "You lost! ❌👎"
                button_text = "Try Again"

            msg_box = QMessageBox()
            msg_box.setText(message)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.setDefaultButton(QMessageBox.StandardButton.Ok)
            msg_box.button(QMessageBox.StandardButton.Ok).setText(button_text)
            msg_box.setStyleSheet("font-size: 16px;")
            msg_box.exec()

            self.update_table()
            self.reset_game()

    def update_table(self):
        row_position = self.score_table.rowCount()
        self.score_table.insertRow(row_position)
        self.score_table.setItem(row_position, 0, QTableWidgetItem(str(self.score_user)))
        self.score_table.setItem(row_position, 1, QTableWidgetItem(str(self.score_computer)))
        self.score_table.setItem(row_position, 2, QTableWidgetItem(f"Game {self.game_round}"))

    def reset_game(self):
        self.score_user = 0
        self.score_computer = 0
        self.game_round += 1
        self.result_label.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RPSGame()
    window.show()
    sys.exit(app.exec())
