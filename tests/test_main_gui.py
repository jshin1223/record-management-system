import sys
import os
import unittest
import tkinter as tk
from unittest.mock import patch, MagicMock

# Add the src directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Import the create_gui function
from src.gui.main_gui import create_gui
from src.gui.client_gui import manage_client_gui
from src.gui.airline_gui import manage_airline_gui
from src.gui.flight_gui import manage_flight_gui

class TestMainGUI(unittest.TestCase):
    
    def setUp(self):
        """
        Set up the test environment by initializing the main GUI.
        """
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the root window
        create_gui()
        self.window = None
        for window in self.root.winfo_children():
            if isinstance(window, tk.Toplevel):
                self.window = window
                break
        self.assertIsNotNone(self.window, "Main window not found")

    def tearDown(self):
        """
        Clean up the test environment by destroying the main GUI.
        """
        self.root.destroy()

    def test_main_gui_creation(self):
        """
        Test if the main GUI window and its elements are created successfully.
        """
        self.assertEqual(self.window.title(), "Record Management System")
        self.assertEqual(self.window.geometry(), "800x600")

    def test_menu_creation(self):
        """
        Test if the menu and menu items are created successfully.
        """
        menu = self.window.nametowidget(self.window.winfo_children()[0].winfo_name())
        record_menu = menu.children["!menu"]
        
        self.assertIsInstance(menu, tk.Menu)
        self.assertIsInstance(record_menu, tk.Menu)
        
        self.assertEqual(record_menu.entrycget(0, "label"), "Client Records")
        self.assertEqual(record_menu.entrycget(1, "label"), "Airline Records")
        self.assertEqual(record_menu.entrycget(2, "label"), "Flight Records")

    @patch('gui.client_gui.manage_client_gui')
    @patch('gui.airline_gui.manage_airline_gui')
    @patch('gui.flight_gui.manage_flight_gui')
    def test_menu_actions(self, mock_manage_flight_gui, mock_manage_airline_gui, mock_manage_client_gui):
        """
        Test if the menu items trigger the correct functions.
        """
        menu = self.window.nametowidget(self.window.winfo_children()[0].winfo_name())
        record_menu = menu.children["!menu"]
        
        record_menu.invoke(0)
        mock_manage_client_gui.assert_called_once()
        
        record_menu.invoke(1)
        mock_manage_airline_gui.assert_called_once()
        
        record_menu.invoke(2)
        mock_manage_flight_gui.assert_called_once()


if __name__ == '__main__':
    unittest.main()
