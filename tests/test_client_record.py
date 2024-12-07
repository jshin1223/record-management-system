import unittest
import os
import json
from src.record.client import ClientRecord  # Adjust based on where your ClientRecord class is located
from src.conf.config import CLIENT_FILE  # Adjust the import based on the actual file path

class TestClientRecord(unittest.TestCase):
    """Unit tests for the ClientRecord class."""

    def setUp(self):
        """
        Set up the test environment by creating a temporary client data file.
        """
        self.test_client_file = CLIENT_FILE
        # Save original file contents (if any)
        if os.path.exists(self.test_client_file):
            with open(self.test_client_file, "r") as f:
                self.original_data = f.read()
        else:
            self.original_data = None

        # Create a temporary JSON file for testing
        self.test_data = [
            {"ID": 1, "Name": "John Doe", "Phone Number": "1-773-5435432"},
            {"ID": 2, "Name": "Jane Smith", "Phone Number": "1-312-6546543"}
        ]
        with open(self.test_client_file, "w") as f:
            json.dump(self.test_data, f, indent=4)

    def tearDown(self):
        """
        Clean up the test environment by restoring the original file contents.
        """
        if self.original_data is not None:
            with open(self.test_client_file, "w") as f:
                f.write(self.original_data)
        else:
            os.remove(self.test_client_file)

    def test_load_all(self):
        """Test loading all client records."""
        records = ClientRecord.load_all()
        self.assertEqual(len(records), len(self.test_data))
        self.assertEqual(records[0]["Name"], "John Doe")

    def test_save_all(self):
        """Test saving all client records."""
        new_record = {"ID": 3, "Name": "Alice Brown", "Phone Number": "1-773-1112222"}
        ClientRecord.save_all([new_record])
        with open(self.test_client_file, "r") as f:
            records = json.load(f)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["Name"], "Alice Brown")

    def test_create(self):
        """Test creating a new client record."""
        new_record = {"ID": 3, "Name": "Alice Brown", "Phone Number": "1-773-1112222"}
        ClientRecord.create(new_record)
        records = ClientRecord.load_all()
        self.assertIn(new_record, records)

    def test_search(self):
        """Test searching for a client record by ID."""
        record = ClientRecord.search(1)
        self.assertIsNotNone(record)
        self.assertEqual(record["Name"], "John Doe")

    def test_generate_id(self):
        """Test generating a unique client ID."""
        new_id = ClientRecord.generate_id()
        self.assertEqual(new_id, 3)

    def test_is_valid_phone(self):
        """Test validating the phone number format."""
        self.assertTrue(ClientRecord.is_valid_phone("1-773-5435432"))
        self.assertFalse(ClientRecord.is_valid_phone("17735435432"))

    def test_update(self):
        """Test updating an existing client record."""
        updated_data = {"Name": "Johnathan Doe", "Phone Number": "1-773-9998888"}
        result = ClientRecord.update(1, updated_data)
        self.assertTrue(result)
        record = ClientRecord.search(1)
        self.assertEqual(record["Name"], "Johnathan Doe")
        self.assertEqual(record["Phone Number"], "1-773-9998888")

    def test_delete(self):
        """Test deleting a client record by ID."""
        result = ClientRecord.delete(1)
        self.assertTrue(result)
        records = ClientRecord.load_all()
        self.assertNotIn({"ID": 1, "Name": "John Doe", "Phone Number": "1-773-5435432"}, records)

    def test_is_duplicate_phone(self):
        """Test checking for duplicate phone numbers."""
        self.assertTrue(ClientRecord.is_duplicate_phone("1-773-5435432"))
        self.assertFalse(ClientRecord.is_duplicate_phone("1-773-1112222"))

    def test_create_with_invalid_phone(self):
        """Test creating a client record with an invalid phone number."""
        invalid_record = {"ID": 4, "Name": "Bob Martin", "Phone Number": "17735435432"}
        with self.assertRaises(ValueError):
            ClientRecord.create(invalid_record)

    def test_create_with_duplicate_phone(self):
        """Test creating a client record with a duplicate phone number."""
        duplicate_record = {"ID": 4, "Name": "Bob Martin", "Phone Number": "1-773-5435432"}
        with self.assertRaises(ValueError):
            ClientRecord.create(duplicate_record)

if __name__ == "__main__":
    unittest.main()
