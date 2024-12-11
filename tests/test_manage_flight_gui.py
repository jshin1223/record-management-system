import sys
import os
import unittest
import tkinter as tk
from unittest.mock import patch, MagicMock

# Add the src directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Import the manage_flight_gui function
from src.gui.flight_gui import manage_flight_gui
from src.record.flight import FlightRecord  # Import FlightRecord for mocking

class TestManageFlightGUI(unittest.TestCase):

    def setUp(self):
        """
        Sets up the testing environment by initializing the root Tkinter application and GUI window.
        """
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the root window
        self.window = None
        # Create the GUI window
        manage_flight_gui()
        for window in self.root.winfo_children():
            if isinstance(window, tk.Toplevel):
                self.window = window
                break
        self.assertIsNotNone(self.window, "Failed to create the GUI window.")

    def tearDown(self):
        """
        Tears down the testing environment by destroying the root Tkinter application.
        """
        if self.root:
            self.root.destroy()

    def find_widget(self, parent, widget_name):
        """
        Recursively finds a widget by name within the given parent widget.
        """
        if parent.winfo_name() == widget_name:
            return parent
        for child in parent.winfo_children():
            widget = self.find_widget(child, widget_name)
            if widget:
                return widget
        return None


    @patch('src.gui.flight_gui.FlightRecord')
    def test_save_flight(self, MockFlightRecord):
        """
        Tests the Save functionality by simulating user input and ensuring the backend method is called correctly.
        """
        MockFlightRecord.is_duplicate_flight.return_value = False

        # Fill in the entry fields with test data
        test_data = {
            "client_id_entry": "2",
            "airline_id_entry": "102",
            "date_entry": "2024-12-11 10:01",
            "start_city_entry": "Amsterdam",
            "end_city_entry": "Munich"
        }
        for name, value in test_data.items():
            entry = self.find_widget(self.window, name)
            self.assertIsNotNone(entry, f"Entry widget '{name}' not found.")
            entry.insert(0, value)

        MockFlightRecord.create = MagicMock()

        # Simulate clicking the save button
        save_button = self.find_widget(self.window, "save_button")
        self.assertIsNotNone(save_button, "Save button not found.")
        save_button.invoke()

        # Verify that the backend method was called with the correct data
        MockFlightRecord.create.assert_called_once_with({
            "Flight_ID": MockFlightRecord.generate_id(),
            "Client_ID": 2,
            "Airline_ID": 102,
            "Date/Time": "2024-12-11 10:01",
            "Start City": "Amsterdam",
            "End City": "Munich"
        })

    @patch('src.gui.flight_gui.FlightRecord')
    def test_search_flight(self, MockFlightRecord):
        """
        Tests the Search functionality by simulating user input and ensuring the backend method is called correctly.
        """
        MockFlightRecord.search.return_value = {
            "Flight_ID": 1,
            "Client_ID": 2,
            "Airline_ID": 102,
            "Date/Time": "2024-12-11 10:01",
            "Start City": "Amsterdam",
            "End City": "Munich"
        }

        # Enter a flight ID to search
        flight_id_entry = self.find_widget(self.window, "flight_id_entry")
        self.assertIsNotNone(flight_id_entry, "Flight ID entry not found.")
        flight_id_entry.insert(0, "1")

        # Simulate clicking the search button
        search_button = self.find_widget(self.window, "search_button")
        self.assertIsNotNone(search_button, "Search button not found.")
        search_button.invoke()

        # Verify that the result text box displays the correct data
        result_text = self.find_widget(self.window, "result_text")
        self.assertIsNotNone(result_text, "Result text box not found.")
        self.assertIn("Flight Found:", result_text.get(1.0, tk.END))

    @patch('src.gui.flight_gui.FlightRecord')
    def test_update_flight(self, MockFlightRecord):
        """
        Tests the Update functionality by simulating user input and ensuring the backend method is called correctly.
        """
        MockFlightRecord.update.return_value = True

        # Enter flight ID and updated data
        flight_id_entry = self.find_widget(self.window, "flight_id_entry")
        self.assertIsNotNone(flight_id_entry, "Flight ID entry not found.")
        flight_id_entry.insert(0, "1")

        test_data = {
            "client_id_entry": "2",
            "airline_id_entry": "102",
            "date_entry": "2024-12-11 10:01",
            "start_city_entry": "Amsterdam",
            "end_city_entry": "Munich"
        }
        for name, value in test_data.items():
            entry = self.find_widget(self.window, name)
            self.assertIsNotNone(entry, f"Entry widget '{name}' not found.")
            entry.insert(0, value)

        # Simulate clicking the update button
        update_button = self.find_widget(self.window, "update_button")
        self.assertIsNotNone(update_button, "Update button not found.")
        update_button.invoke()

        # Verify that the backend method was called with the correct data
        MockFlightRecord.update.assert_called_once_with(1, {
            "Client_ID": 2,
            "Airline_ID": 102,
            "Date/Time": "2024-12-11 10:01",
            "Start City": "Amsterdam",
            "End City": "Munich"
        })

    @patch('src.gui.flight_gui.FlightRecord')
    def test_delete_flight(self, MockFlightRecord):
        """
        Tests the Delete functionality by simulating user input and ensuring the backend method is called correctly.
        """
        MockFlightRecord.delete.return_value = True

        # Enter a flight ID to delete
        flight_id_entry = self.find_widget(self.window, "flight_id_entry")
        self.assertIsNotNone(flight_id_entry, "Flight ID entry not found.")
        flight_id_entry.insert(0, "1")

        # Simulate clicking the delete button
        delete_button = self.find_widget(self.window, "delete_button")
        self.assertIsNotNone(delete_button, "Delete button not found.")
        delete_button.invoke()

        # Verify that the backend method was called with the correct ID
        MockFlightRecord.delete.assert_called_once_with(1)


if __name__ == '__main__':
    unittest.main()
