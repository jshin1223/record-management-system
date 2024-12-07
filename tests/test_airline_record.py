import unittest
import os
import json
import sys

from src.conf.config import AIRLINE_FILE  # Adjust this import to match the correct file location
from src.record.airline import AirlineRecord  # Adjust this import to match the correct file location

class TestAirlineRecord(unittest.TestCase):
    """Unit tests for the AirlineRecord class."""

    def setUp(self):
        """
        Set up the test environment by creating a temporary airline data file.
        """
        self.test_airline_file = AIRLINE_FILE
        # Save original file contents (if any)
        if os.path.exists(self.test_airline_file):
            with open(self.test_airline_file, "r") as f:
                self.original_data = f.read()
        else:
            self.original_data = None

        # Create a temporary JSON file for testing
        self.test_data = [
            {"ID": 1, "Company Name": "Airline One", "Country": "Country A"},
            {"ID": 2, "Company Name": "Airline Two", "Country": "Country B"}
        ]
        with open(self.test_airline_file, "w") as f:
            json.dump(self.test_data, f, indent=4)

    def tearDown(self):
        """
        Clean up the test environment by restoring the original file contents.
        """
        if self.original_data is not None:
            with open(self.test_airline_file, "w") as f:
                f.write(self.original_data)
        else:
            os.remove(self.test_airline_file)

    def test_load_all(self):
        """Test loading all airline records."""
        records = AirlineRecord.load_all()
        self.assertEqual(len(records), len(self.test_data))
        self.assertEqual(records[0]["Company Name"], "Airline One")

    def test_save_all(self):
        """Test saving all airline records."""
        new_record = {"ID": 3, "Company Name": "Airline Three", "Country": "Country C"}
        AirlineRecord.save_all([new_record])
        with open(self.test_airline_file, "r") as f:
            records = json.load(f)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["Company Name"], "Airline Three")

    def test_create(self):
        """Test creating a new airline record."""
        new_record = {"ID": 3, "Company Name": "Airline Three", "Country": "Country C"}
        AirlineRecord.create(new_record)
        records = AirlineRecord.load_all()
        self.assertIn(new_record, records)

    def test_search(self):
        """Test searching for an airline record by ID."""
        record = AirlineRecord.search(1)
        self.assertIsNotNone(record)
        self.assertEqual(record["Company Name"], "Airline One")

    def test_generate_id(self):
        """Test generating a unique airline ID."""
        new_id = AirlineRecord.generate_id()
        self.assertEqual(new_id, 3)

    def test_is_duplicate_airline_name(self):
        """Test checking for duplicate airline names."""
        duplicate_name = "Airline One"
        result = AirlineRecord.is_duplicate_airline_name(duplicate_name)
        self.assertTrue(result)

    def test_update_airline(self):
        """Test updating an existing airline record."""
        updated_data = {"Company Name": "Updated Airline One", "Country": "Updated Country"}
        result = AirlineRecord.update_airline(1, updated_data)
        self.assertTrue(result)
        record = AirlineRecord.search(1)
        self.assertEqual(record["Company Name"], "Updated Airline One")
        self.assertEqual(record["Country"], "Updated Country")

    def test_delete_airline(self):
        """Test deleting an airline record by ID."""
        result = AirlineRecord.delete_airline(1)
        self.assertTrue(result)
        records = AirlineRecord.load_all()
        self.assertNotIn({"ID": 1, "Company Name": "Airline One", "Country": "Country A"}, records)

if __name__ == "__main__":
    unittest.main()
