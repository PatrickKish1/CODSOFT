import csv
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFormLayout, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtCore import Qt, QSize
import os

class SignupPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.signup_label = QLabel("Sign Up", self)
        self.signup_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.signup_label)

        self.signup_form_layout = QFormLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")
        self.name_input.setFixedSize(QSize(250, 35))
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.email_input.setFixedSize(QSize(250, 35))
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setFixedSize(QSize(250, 35))
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.signup_button = QPushButton("Sign Up")
        self.signup_button.setFixedSize(QSize(140, 32))
        self.signup_button.clicked.connect(self.signup_user)
        self.back_button = QPushButton("Back")
        self.back_button.setFixedSize(QSize(140, 32))
        self.back_button.clicked.connect(self.show_login_page)

        self.signup_form_layout.addRow("Name:", self.name_input)
        self.signup_form_layout.addRow("Email:", self.email_input)
        self.signup_form_layout.addRow("Password:", self.password_input)
        self.signup_form_layout.addRow("", self.signup_button)
        self.signup_form_layout.addRow("", self.back_button)

        self.layout.addLayout(self.signup_form_layout)
        self.setLayout(self.layout)

    def signup_user(self):
        name = self.name_input.text()
        email = self.email_input.text()
        password = self.password_input.text()

        if name and email and password:
            if self.add_user(name, email, password):
                QMessageBox.information(self, "Signup Successful", "User registered successfully.")
                self.show_login_page()
            else:
                QMessageBox.warning(self, "Signup Failed", "User already exists.")
        else:
            QMessageBox.warning(self, "Signup Failed", "Please fill in all fields.")

    def show_login_page(self):
        self.parent.show_login_page()

    def add_user(self, name, email, password):
        if not os.path.exists('users.csv'):
            with open('users.csv', mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['name', 'email', 'password'])
                writer.writeheader()

        with open('users.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['email'] == email:
                    return False

        with open('users.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'email', 'password'])
            writer.writerow({'name': name, 'email': email, 'password': password})
        return True
