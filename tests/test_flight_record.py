import unittest
import os
import json
from datetime import datetime
import sys
import os

# Add the src directory to the system path dynamically
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from record.flight import FlightRecord  # Import FlightRecord class
from conf.config import FLIGHT_FILE  # Import configuration

# Add the 'src' directory to the Python path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))


class TestFlightRecord(unittest.TestCase):
    """Unit tests for the FlightRecord class."""
    
    def setUp(self):
        """
        Set up the test environment by creating a temporary flight data file.
        """
        self.test_flight_file = FLIGHT_FILE
        # Save original file contents (if any)
        if os.path.exists(self.test_flight_file):
            with open(self.test_flight_file, "r") as f:
                self.original_data = f.read()
        else:
            self.original_data = None

        # Create a temporary JSON file for testing
        self.test_data = [
            {"Flight_ID": 1, "Client_ID": 101, "Airline_ID": 201, "Date/Time": "2023-12-15 12:00", "Start_City": "New York", "End_City": "London"},
            {"Flight_ID": 2, "Client_ID": 102, "Airline_ID": 202, "Date/Time": "2023-12-16 15:30", "Start_City": "Los Angeles", "End_City": "Tokyo"}
        ]
        with open(self.test_flight_file, "w") as f:
            json.dump(self.test_data, f, indent=4)

    def tearDown(self):
        """
        Clean up the test environment by restoring the original file contents.
        """
        if self.original_data is not None:
            with open(self.test_flight_file, "w") as f:
                f.write(self.original_data)
        else:
            os.remove(self.test_flight_file)

    def test_load_all(self):
        """Test loading all flight records."""
        records = FlightRecord.load_all()
        self.assertEqual(len(records), len(self.test_data))
        self.assertEqual(records[0]["Flight_ID"], 1)

    def test_save_all(self):
        """Test saving all flight records."""
        new_record = {"Flight_ID": 3, "Client_ID": 103, "Airline_ID": 203, "Date/Time": "2023-12-20 10:00", "Start_City": "Paris", "End_City": "Berlin"}
        FlightRecord.save_all([new_record])
        with open(self.test_flight_file, "r") as f:
            records = json.load(f)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["Flight_ID"], 3)

    def test_create(self):
        """Test creating a new flight record."""
        new_record = {"Flight_ID": 3, "Client_ID": 103, "Airline_ID": 203, "Date/Time": "2023-12-20 10:00", "Start_City": "Paris", "End_City": "Berlin"}
        FlightRecord.create(new_record)
        records = FlightRecord.load_all()
        self.assertIn(new_record, records)

    def test_search(self):
        """Test searching for a flight record by ID."""
        record = FlightRecord.search(1)
        self.assertIsNotNone(record)
        self.assertEqual(record["Start_City"], "New York")

    def test_generate_id(self):
        """Test generating a unique flight ID."""
        new_id = FlightRecord.generate_id()
        self.assertEqual(new_id, 3)

    def test_is_valid_date_time(self):
        """Test validating the date and time format."""
        self.assertTrue(FlightRecord.is_valid_date_time("2023-12-20 10:00"))
        self.assertFalse(FlightRecord.is_valid_date_time("2023-12-20"))

    def test_update(self):
        """Test updating an existing flight record."""
        updated_data = {"Date/Time": "2023-12-18 18:00", "Start_City": "San Francisco"}
        result = FlightRecord.update(1, updated_data)
        self.assertTrue(result)
        record = FlightRecord.search(1)
        self.assertEqual(record["Date/Time"], "2023-12-18 18:00")
        self.assertEqual(record["Start_City"], "San Francisco")

    def test_delete(self):
        """Test deleting a flight record by ID."""
        result = FlightRecord.delete(1)
        self.assertTrue(result)
        records = FlightRecord.load_all()
        self.assertNotIn({"Flight_ID": 1}, records)

if __name__ == "__main__":
    unittest.main()