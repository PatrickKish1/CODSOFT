import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QRect
from users import UsersPage
from activities import ActivitiesPage
from signup import SignupPage
from logout import LogoutPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('To-Do List Application')
        self.setWindowIcon(QIcon(r'./listIcon.ico'))
        self.setGeometry(100, 100, 750, 500)

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.users_page = UsersPage(self)
        self.activities_page = ActivitiesPage(self)
        self.signup_page = SignupPage(self)
        self.logout_page = LogoutPage(self)

        self.central_widget.addWidget(self.users_page)
        self.central_widget.addWidget(self.activities_page)
        self.central_widget.addWidget(self.signup_page)
        self.central_widget.addWidget(self.logout_page)

        self.show_login_page()

    def show_login_page(self):
        self.central_widget.setCurrentWidget(self.users_page)

    def show_activities_page(self):
        self.central_widget.setCurrentWidget(self.activities_page)
        self.activities_page.load_activities()

    def show_signup_page(self):
        self.central_widget.setCurrentWidget(self.signup_page)

    def show_logout_page(self):
        self.central_widget.setCurrentWidget(self.logout_page)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open("styles.qss", "r") as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
