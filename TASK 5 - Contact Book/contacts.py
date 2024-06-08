import pandas as pd
import os
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel, QMessageBox, 
                             QTableWidget, QTableWidgetItem, QHeaderView, QHBoxLayout, QCheckBox)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QColor
from users import UsersPage  # Import the UsersPage to access current_user

class ContactsPage(QWidget):
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
        self.logout_button.setFixedSize(QSize(100, 40))
        self.logout_button.clicked.connect(self.logout)
        top_layout.addWidget(self.logout_button)
        
        self.layout.addLayout(top_layout)

        self.contact_name_label = QLabel("Add New Contact", self)
        self.contact_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.contact_name_label)

        # Contact Table
        self.contact_name_table = QTableWidget()
        self.contact_name_table.setColumnCount(5)  # Added columns for checkbox and delete button
        self.contact_name_table.setHorizontalHeaderLabels(["Name", "Email", "Phone", "Address"])
        self.contact_name_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.contact_name_table.verticalHeader().setVisible(False)
        self.contact_name_table.setAlternatingRowColors(True)
        self.contact_name_table.setStyleSheet("QTableWidget { border: 2px solid #f709ff; border-radius: 5px; }")
        self.contact_name_table.verticalHeader().setDefaultSectionSize(50)  # Adjust row height to 50 pixels
        self.layout.addWidget(self.contact_name_table)

        self.form_layout = QFormLayout()

        self.contact_name_input = QLineEdit()
        self.contact_name_input.setFixedSize(QSize(500, 40))
        self.contact_name_input.setPlaceholderText("Enter contact name")

        self.email_input = QLineEdit()
        self.email_input.setFixedSize(QSize(500, 40))
        self.email_input.setPlaceholderText("Enter email address")

        self.phone_input = QLineEdit()
        self.phone_input.setFixedSize(QSize(500, 40))
        self.phone_input.setPlaceholderText("Enter phone number")

        self.address_input = QLineEdit()
        self.address_input.setFixedSize(QSize(500, 40))
        self.address_input.setPlaceholderText("Enter address")

        self.save_button = QPushButton("Save Contact")
        self.save_button.setFixedSize(QSize(140, 40))
        self.save_button.clicked.connect(self.save_contact)

        # Center the Save Activity button
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.save_button)
        button_layout.addStretch()

        self.form_layout.addRow("Contact Name:", self.contact_name_input)
        self.form_layout.addRow("Email:", self.email_input)
        self.form_layout.addRow("Phone Number:", self.phone_input)
        self.form_layout.addRow("Address:", self.address_input)
        self.form_layout.addRow("", button_layout)

        self.layout.addLayout(self.form_layout)
        self.setLayout(self.layout)

    def load_contacts(self):
        current_user = self.parent.users_page.current_user
        if not current_user:
            QMessageBox.warning(self, "Error", "No user logged in.")
            return

        file_path = 'contacts.xlsx'
        if os.path.exists(file_path):
            df = pd.read_excel(file_path)
            user_activities = df[df['Current User'] == current_user]

            self.contact_name_table.setRowCount(user_activities.shape[0])
            for i, row in user_activities.iterrows():
                contact_name_item = QTableWidgetItem(row['Name'])
                email_item = QTableWidgetItem(str(row['Email']))
                phone_item = QTableWidgetItem(str(row['Phone']))
                address_item = QTableWidgetItem(row['Address'])
                # completed_item = QTableWidgetItem()
                # completed_item.setCheckState(Qt.CheckState.Checked if row.get('Completed', False) else Qt.CheckState.Unchecked)
                delete_button = QPushButton("Delete")
                delete_button.setFixedSize(QSize(85, 35))
                delete_button.clicked.connect(lambda _, idx=i: self.delete_contact(idx))

                # Set the font color for each item
                contact_name_item.setForeground(QColor("#24c"))
                email_item.setForeground(QColor("#24c"))
                phone_item.setForeground(QColor("#24c"))
                address_item.setForeground(QColor("#24c"))

                self.contact_name_table.setItem(i, 0, contact_name_item)
                self.contact_name_table.setItem(i, 1, email_item)
                self.contact_name_table.setItem(i, 2, phone_item)
                self.contact_name_table.setItem(i, 3, address_item)
                self.contact_name_table.setCellWidget(i, 4, delete_button)

        self.username_label.setText(f"Logged in as: {current_user}")

    def save_contact(self):
        contact_name = self.contact_name_input.text()
        email = self.email_input.text()
        phone = self.phone_input.text()
        address = self.address_input.text()
        user = self.parent.users_page.current_user

        if contact_name and email and phone and address and user:
            self.add_contact_to_excel(contact_name, email, phone, address, user)
            QMessageBox.information(self, "Contact Saved", "Contact added successfully.")
            self.load_contacts()
            self.clear_inputs()
        else:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")

    def add_contact_to_excel(self, contact_name, email, phone, address, user):
        file_path = 'contacts.xlsx'
        data = {'Name': [contact_name], 'Email': [email], 'Phone': [phone], 'Address': [address], 'Current User': [user]}
        df = pd.DataFrame(data)

        if not os.path.exists(file_path):
            df.to_excel(file_path, index=False)
        else:
            existing_df = pd.read_excel(file_path)
            updated_df = pd.concat([existing_df, df], ignore_index=True)
            updated_df.to_excel(file_path, index=False)

    def clear_inputs(self):
        self.contact_name_input.clear()
        self.email_input.clear()
        self.phone_input.clear()
        self.address_input.clear()

    def logout(self):
        self.parent.users_page.current_user = None
        self.parent.show_login_page()

    def delete_contact(self, row):
        file_path = 'contacts.xlsx'
        if os.path.exists(file_path):
            df = pd.read_excel(file_path)
            current_user = self.parent.users_page.current_user
            user_activities = df[df['Current User'] == current_user]
            user_activities = user_activities.drop(user_activities.index[row])
            df = df[df['Current User'] != current_user]
            df = pd.concat([df, user_activities], ignore_index=True)
            df.to_excel(file_path, index=False)
            self.load_contacts()
            QMessageBox.information(self, "Contact Deleted", "Contact deleted successfully.")
