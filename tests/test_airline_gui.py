import sys
import os
import unittest
import tkinter as tk
from unittest.mock import patch, MagicMock

# Ensure the correct path is added
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Now import the manage_airline_gui function from the correct module
from gui.airline_gui import manage_airline_gui

class TestManageAirlineGUI(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()
        manage_airline_gui()

    def tearDown(self):
        self.root.destroy()

    def test_manage_airline_gui_creation(self):
        for window in self.root.winfo_children():
            if isinstance(window, tk.Toplevel):
                self.window = window
                break
        
        airline_id_entry = self.window.nametowidget("airline_id_entry")
        company_name_entry = self.window.nametowidget("company_name_entry")

        self.assertIsInstance(airline_id_entry, tk.Entry)
        self.assertIsInstance(company_name_entry, tk.Entry)

    @patch('gui.airline_gui.AirlineRecord')
    def test_save_airline(self, MockAirlineRecord):
        for window in self.root.winfo_children():
            if isinstance(window, tk.Toplevel):
                self.window = window
                break

        company_name_entry = self.window.nametowidget("company_name_entry")
        company_name_entry.insert(0, "Test Airline")

        MockAirlineRecord.create = MagicMock()

        # Instead of using nametowidget, iterate through children to find the button
        save_button = None
        for child in self.window.winfo_children():
            if isinstance(child, tk.Frame):
                for subchild in child.winfo_children():
                    if subchild.winfo_name() == 'save_button':
                        save_button = subchild
                        break

        if save_button is None:
            self.fail("save_button not found")

        save_button.invoke()

        MockAirlineRecord.create.assert_called_with({
            "ID": MockAirlineRecord.generate_id(),
            "Type": "Airline",
            "Company Name": "Test Airline",
        })

if __name__ == '__main__':
    unittest.main()
