import sys
import random
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLabel, QLineEdit, QMessageBox
)
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon

class PasswordGenerator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Generator")
        self.setGeometry(100, 100, 400, 200)
        self.setStyleSheet(open('styles.qss').read())

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.create_length_input()
        self.create_generate_button()
        self.create_password_display()

    def create_length_input(self):
        self.length_label = QLabel("Password Length:")
        self.length_input = QLineEdit()
        self.length_input.setPlaceholderText("Enter length...")
        self.layout.addWidget(self.length_label)
        self.layout.addWidget(self.length_input)

    def create_generate_button(self):
        self.generate_button = QPushButton("Generate Password")
        self.generate_button.clicked.connect(self.generate_password)
        self.layout.addWidget(self.generate_button)

    def create_password_display(self):
        self.password_label = QLabel("Generated Password:")
        self.password_display = QLineEdit()
        self.password_display.setReadOnly(True)
        self.password_display.setPlaceholderText("Password will be displayed here...")
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_display)

    def generate_password(self):
        try:
            length = int(self.length_input.text())
            if length <= 7:
                raise ValueError("Length must be greater than 7")
            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_display.setText(password)
        except ValueError as e:
            self.show_error_message("Invalid Length", str(e))

    def show_error_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec())
