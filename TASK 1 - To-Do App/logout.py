from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton

class LogoutPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        logout_button = QPushButton("Logout")
        logout_button.clicked.connect(self.logout)
        layout.addWidget(logout_button)

        self.setLayout(layout)

    def logout(self):
        self.parent.show_login_page()
