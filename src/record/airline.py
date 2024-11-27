"""
This module provides the backend logic for managing airline records in the Record Management System.

It allows users to:
- Load all airline records from a JSON file.
- Save airline records to the JSON file.
- Create new airline records.
- Search for airline records by ID.
- Generate unique IDs for new airline records.

Classes:
    AirlineRecord: A class containing static methods for managing airline records.
"""

import json  # Importing JSON module for reading and writing JSON files
from conf.config import AIRLINE_FILE  # Import configuration for the airline data file path

class AirlineRecord:
    """
    A class to handle operations related to airline records, such as loading, saving, creating, and searching.
    """

    @staticmethod
    def load_all():
        """
        Load all airline records from the JSON file.

        If the file is missing or contains invalid data, return an empty list.

        Returns:
            list: A list of dictionaries representing all airline records.
        """
        try:
            # Open the JSON file in read mode and load the records
            with open(AIRLINE_FILE, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file is missing or invalid, return an empty list
            return []

    @staticmethod
    def save_all(records):
        """
        Save all airline records to the JSON file.

        Args:
            records (list): A list of dictionaries representing airline records to save.
        """
        # Open the JSON file in write mode and dump the records
        with open(AIRLINE_FILE, "w") as f:
            json.dump(records, f, indent=4)

    @staticmethod
    def create(airline_data):
        """
        Create a new airline record and save it.

        Args:
            airline_data (dict): A dictionary containing airline information, including ID and company name.
        """
        # Load existing records
        records = AirlineRecord.load_all()
        # Append the new record to the list
        records.append(airline_data)
        # Save the updated records list
        AirlineRecord.save_all(records)

    @staticmethod
    def search(airline_id):
        """
        Search for an airline by its unique ID.

        Args:
            airline_id (int): The ID of the airline to search for.

        Returns:
            dict: The airline record if found, otherwise None.
        """
        # Load existing records
        records = AirlineRecord.load_all()
        # Iterate through records to find a match
        for record in records:
            if record["ID"] == airline_id:
                return record
        # Return None if no matching record is found
        return None

    @staticmethod
    def generate_id():
        """
        Generate a unique ID for a new airline.

        Returns:
            int: A unique ID for the new airline record.
        """
        # Load existing records
        records = AirlineRecord.load_all()
        # If no records exist, start with ID 1
        if not records:
            return 1
        # Return the maximum existing ID plus one
        return max(record["ID"] for record in records) + 1