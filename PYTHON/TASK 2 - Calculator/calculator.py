import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QGridLayout, QPushButton, QWidget, QLineEdit
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 300)
        self.setStyleSheet(open('styles.qss').read())

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.create_display()
        self.create_buttons()

    def create_display(self):
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFixedHeight(50)
        self.layout.addWidget(self.display)

    def create_buttons(self):
        buttons = {
            'C': (0, 0), '/': (0, 1), '*': (0, 2), '-': (0, 3),
            '7': (1, 0), '8': (1, 1), '9': (1, 2), '+': (1, 3),
            '4': (2, 0), '5': (2, 1), '6': (2, 2), '=': (2, 3),
            '1': (3, 0), '2': (3, 1), '3': (3, 2), '0': (3, 3),
            '.': (4, 0)
        }

        grid_layout = QGridLayout()
        self.layout.addLayout(grid_layout)

        for btn_text, pos in buttons.items():
            button = self.create_button(btn_text)
            grid_layout.addWidget(button, pos[0], pos[1])

    def create_button(self, text):
        button = QPushButton(text)
        button.setFixedSize(60, 60)
        button.clicked.connect(lambda: self.on_button_click(text))
        return button

    def on_button_click(self, text):
        if text == 'C':
            self.display.clear()
        elif text == '=':
            try:
                expression = self.display.text()
                result = eval(expression)
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText('Error')
        else:
            current_text = self.display.text()
            new_text = current_text + text
            self.display.setText(new_text)

    def keyPressEvent(self, event):
        key = event.key()
        text = None

        if key in range(Qt.Key.Key_0, Qt.Key.Key_9 + 1):
            text = chr(key)
        elif key == Qt.Key.Key_Escape:
            text = 'C'
        elif key in [Qt.Key.Key_Enter, Qt.Key.Key_Return]:
            text = '='
        elif key == Qt.Key.Key_Plus:
            text = '+'
        elif key == Qt.Key.Key_Minus:
            text = '-'
        elif key == Qt.Key.Key_Asterisk:
            text = '*'
        elif key == Qt.Key.Key_Slash:
            text = '/'
        elif key == Qt.Key.Key_Period:
            text = '.'

        if text:
            self.on_button_click(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
