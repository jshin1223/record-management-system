import sys
import os
import unittest
import tkinter as tk
from unittest.mock import patch, MagicMock

# Add the src directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Import the manage_client_gui function
from gui.client_gui import manage_client_gui
from record.client import ClientRecord  # Import ClientRecord for mocking


class TestManageClientGUI(unittest.TestCase):
    
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the root window
        manage_client_gui()

    def tearDown(self):
        self.root.destroy()

    def find_widget(self, parent, widget_name):
        for child in parent.winfo_children():
            if child.winfo_name() == widget_name:
                return child
            # Recursively search in child widgets
            found = self.find_widget(child, widget_name)
            if found:
                return found
        return None

    def test_manage_client_gui_creation(self):
        for window in self.root.winfo_children():
            if isinstance(window, tk.Toplevel):
                self.window = window
                break

        # Check if the main window and all entry fields are created
        self.assertIsInstance(self.window, tk.Toplevel)
        
        # Debugging: Print all child widgets and their names
        print("All child widgets of the window:")
        for child in self.window.winfo_children():
            print(child.winfo_name(), type(child))
        
        self.assertIsInstance(self.find_widget(self.window, "name_entry"), tk.Entry)
        self.assertIsInstance(self.find_widget(self.window, "address1_entry"), tk.Entry)
        self.assertIsInstance(self.find_widget(self.window, "address2_entry"), tk.Entry)
        self.assertIsInstance(self.find_widget(self.window, "address3_entry"), tk.Entry)
        self.assertIsInstance(self.find_widget(self.window, "city_entry"), tk.Entry)
        self.assertIsInstance(self.find_widget(self.window, "state_entry"), tk.Entry)
        self.assertIsInstance(self.find_widget(self.window, "zip_entry"), tk.Entry)
        self.assertIsInstance(self.find_widget(self.window, "country_entry"), tk.Entry)
        self.assertIsInstance(self.find_widget(self.window, "phone_entry"), tk.Entry)

    @patch('gui.client_gui.ClientRecord')
    def test_save_client(self, MockClientRecord):
        for window in self.root.winfo_children():
            if isinstance(window, tk.Toplevel):
                self.window = window
                break

        # Access the entry fields and insert test data
        entries = {
            "name_entry": "Test Client",
            "address1_entry": "123 Test St",
            "address2_entry": "Suite 100",
            "address3_entry": "Building 4",
            "city_entry": "Test City",
            "state_entry": "Test State",
            "zip_entry": "12345",
            "country_entry": "Test Country",
            "phone_entry": "1-123-4567890"
        }
        
        for entry_name, entry_value in entries.items():
            entry_widget = self.find_widget(self.window, entry_name)
            self.assertIsNotNone(entry_widget, f"Widget named {entry_name} not found.")
            entry_widget.insert(0, entry_value)

        MockClientRecord.create = MagicMock()

        # Debugging: Print all child widgets of the button frame
        for child in self.window.winfo_children():
            if isinstance(child, tk.Frame):
                print("Child widgets of the button frame:")
                for subchild in child.winfo_children():
                    print(subchild.winfo_name(), type(subchild))
        
        # Find and click the save button
        save_button = self.find_widget(self.window, "save_button")
        self.assertIsNotNone(save_button, "Save button not found.")
        save_button.invoke()

        # Verify that the create method was called with the correct data
        MockClientRecord.create.assert_called_with({
            "ID": MockClientRecord.generate_id(),
            "Type": "Client",
            "Name": "Test Client",
            "Address Line 1": "123 Test St",
            "Address Line 2": "Suite 100",
            "Address Line 3": "Building 4",
            "City": "Test City",
            "State": "Test State",
            "Zip Code": "12345",
            "Country": "Test Country",
            "Phone Number": "1-123-4567890"
        })

    @patch('gui.client_gui.ClientRecord')
    def test_search_client(self, MockClientRecord):
        for window in self.root.winfo_children():
            if isinstance(window, tk.Toplevel):
                self.window = window
                break

        # Debugging: Print all child widgets and their names
        print("All child widgets of the window:")
        for child in self.window.winfo_children():
            print(child.winfo_name(), type(child))
        
        # Debugging: Print the children of the frame to confirm search_entry location
        for child in self.window.winfo_children():
            if isinstance(child, tk.Frame):
                print("Child widgets of the frame:")
                for subchild in child.winfo_children():
                    print(subchild.winfo_name(), type(subchild))

        search_entry = self.find_widget(self.window, "search_entry")
        self.assertIsNotNone(search_entry, "Search entry not found.")
        search_entry.insert(0, "1")

        MockClientRecord.search.return_value = {
            "ID": 1,
            "Name": "Test Client",
            "Address Line 1": "123 Test St"
        }

        search_button = self.find_widget(self.window, "search_button")
        self.assertIsNotNone(search_button, "Search button not found.")
        search_button.invoke()

        # Check if the result is displayed correctly
        result_text = self.find_widget(self.window, "result_text")
        self.assertIsNotNone(result_text, "Result text box not found.")
        self.assertIn("Client Found:\n{'ID': 1, 'Name': 'Test Client', 'Address Line 1': '123 Test St'}", result_text.get(1.0, tk.END))


if __name__ == '__main__':
    unittest.main()
