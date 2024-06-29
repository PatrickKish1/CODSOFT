import csv
import os
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel, QMessageBox, QHBoxLayout
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap
from signup import SignupPage

class UsersPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.current_user = None  # Store the current user
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.login_page_image = QPixmap(r'./contacts.png')

        self.login_label = QLabel(self)
        self.login_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.login_label.setPixmap(self.login_page_image)
        self.layout.addWidget(self.login_label)

        self.login_form_layout = QFormLayout()
        self.email_input = QLineEdit()
        self.email_input.setFixedSize(QSize(300, 40))  # Fixed size for email input
        self.email_input.setPlaceholderText("Email")
        self.password_input = QLineEdit()
        self.password_input.setFixedSize(QSize(300, 40))  # Fixed size for password input
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)  # Mask the password input

        # Horizontal layout for buttons
        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setSpacing(20)  # Set spacing between buttons (in pixels)

        self.login_button = QPushButton("Login")
        self.login_button.setFixedSize(QSize(140, 40))  # Fixed size for login button
        self.login_button.clicked.connect(self.login_user)
        self.signup_button = QPushButton("Sign Up")
        self.signup_button.setFixedSize(QSize(140, 40))  # Fixed size for signup button
        self.signup_button.clicked.connect(self.parent.show_signup_page)  # Connect to show_signup_page

        self.buttons_layout.addWidget(self.login_button)
        self.buttons_layout.addWidget(self.signup_button)

        self.login_form_layout.addRow("Email:", self.email_input)
        self.login_form_layout.addRow("Password:", self.password_input)
        self.login_form_layout.addRow("", self.buttons_layout)  # Add buttons layout to form layout

        self.layout.addLayout(self.login_form_layout)
        self.setLayout(self.layout)

    def login_user(self):
        email = self.email_input.text()
        password = self.password_input.text()

        if self.validate_user(email, password):
            self.current_user = email  # Set current user on successful login
            self.parent.show_contacts_page()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid email or password entered.")

    def validate_user(self, email, password):
        if not os.path.exists('users.csv'):
            return False
        with open('users.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['email'] == email and row['password'] == password:
                    return True
        return False
