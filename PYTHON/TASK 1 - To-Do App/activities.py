import pandas as pd
import os
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel, QMessageBox, 
                             QTableWidget, QTableWidgetItem, QHeaderView, QHBoxLayout, QCheckBox)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QColor
from users import UsersPage  # Import the UsersPage to access current_user

class ActivitiesPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        # Username Label
        top_layout = QHBoxLayout()
        self.username_label = QLabel("", self)
        self.username_label.setAlignment(Qt.AlignmentFlag.AlignRight)  # Align to the right
        top_layout.addWidget(self.username_label)

        self.logout_button = QPushButton("Logout")
        self.logout_button.setFixedSize(QSize(100, 30))
        self.logout_button.clicked.connect(self.logout)
        top_layout.addWidget(self.logout_button)
        
        self.layout.addLayout(top_layout)

        self.activities_label = QLabel("Add New Activity", self)
        self.activities_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.activities_label)

        # Activities Table
        self.activities_table = QTableWidget()
        self.activities_table.setColumnCount(5)  # Added columns for checkbox and delete button
        self.activities_table.setHorizontalHeaderLabels(["Activity", "Date", "Time", "Completed", "Delete"])
        self.activities_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.activities_table.verticalHeader().setVisible(False)
        self.activities_table.setAlternatingRowColors(True)
        self.activities_table.setStyleSheet("QTableWidget { border: 2px solid #f709ff; border-radius: 5px; }")
        self.activities_table.verticalHeader().setDefaultSectionSize(50)  # Adjust row height to 50 pixels
        self.layout.addWidget(self.activities_table)

        self.form_layout = QFormLayout()
        self.activity_input = QLineEdit()
        self.activity_input.setPlaceholderText("Activity Name")
        self.date_input = QLineEdit()
        self.date_input.setPlaceholderText("Date (YYYY-MM-DD)")
        self.time_input = QLineEdit()
        self.time_input.setPlaceholderText("Time (HH:MM)")

        self.save_button = QPushButton("Save Activity")
        self.save_button.setFixedSize(QSize(140, 32))
        self.save_button.clicked.connect(self.save_activity)

        # Center the Save Activity button
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.save_button)
        button_layout.addStretch()

        self.form_layout.addRow("Activity Name:", self.activity_input)
        self.form_layout.addRow("Date:", self.date_input)
        self.form_layout.addRow("Time:", self.time_input)
        self.form_layout.addRow("", button_layout)

        self.layout.addLayout(self.form_layout)
        self.setLayout(self.layout)

    def load_activities(self):
        current_user = self.parent.users_page.current_user
        if not current_user:
            QMessageBox.warning(self, "Error", "No user logged in.")
            return

        file_path = 'activities.xlsx'
        if os.path.exists(file_path):
            df = pd.read_excel(file_path)
            user_activities = df[df['User'] == current_user]

            self.activities_table.setRowCount(user_activities.shape[0])
            for i, row in user_activities.iterrows():
                activity_item = QTableWidgetItem(row['Activity'])
                date_item = QTableWidgetItem(str(row['Date']))
                time_item = QTableWidgetItem(row['Time'])
                completed_item = QTableWidgetItem()
                completed_item.setCheckState(Qt.CheckState.Checked if row.get('Completed', False) else Qt.CheckState.Unchecked)
                delete_button = QPushButton("Delete")
                delete_button.setFixedSize(QSize(70, 30))
                delete_button.clicked.connect(lambda _, idx=i: self.delete_activity(idx))

                # Set the font color for each item
                activity_item.setForeground(QColor("#333"))
                date_item.setForeground(QColor("#333"))
                time_item.setForeground(QColor("#333"))

                self.activities_table.setItem(i, 0, activity_item)
                self.activities_table.setItem(i, 1, date_item)
                self.activities_table.setItem(i, 2, time_item)
                self.activities_table.setItem(i, 3, completed_item)
                self.activities_table.setCellWidget(i, 4, delete_button)

        self.username_label.setText(f"Logged in as: {current_user}")

    def save_activity(self):
        activity_name = self.activity_input.text()
        date = self.date_input.text()
        time = self.time_input.text()
        user = self.parent.users_page.current_user

        if activity_name and date and time and user:
            self.add_activity_to_excel(activity_name, date, time, user)
            QMessageBox.information(self, "Activity Saved", "Activity added successfully.")
            self.load_activities()
            self.clear_inputs()
        else:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")

    def add_activity_to_excel(self, activity, date, time, user):
        file_path = 'activities.xlsx'
        data = {'Activity': [activity], 'Date': [date], 'Time': [time], 'User': [user], 'Completed': [False]}
        df = pd.DataFrame(data)

        if not os.path.exists(file_path):
            df.to_excel(file_path, index=False)
        else:
            existing_df = pd.read_excel(file_path)
            updated_df = pd.concat([existing_df, df], ignore_index=True)
            updated_df.to_excel(file_path, index=False)

    def clear_inputs(self):
        self.activity_input.clear()
        self.date_input.clear()
        self.time_input.clear()

    def logout(self):
        self.parent.users_page.current_user = None
        self.parent.show_login_page()

    def delete_activity(self, row):
        file_path = 'activities.xlsx'
        if os.path.exists(file_path):
            df = pd.read_excel(file_path)
            current_user = self.parent.users_page.current_user
            user_activities = df[df['User'] == current_user]
            user_activities = user_activities.drop(user_activities.index[row])
            df = df[df['User'] != current_user]
            df = pd.concat([df, user_activities], ignore_index=True)
            df.to_excel(file_path, index=False)
            self.load_activities()
            QMessageBox.information(self, "Activity Deleted", "Activity deleted successfully.")
