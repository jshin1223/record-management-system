"""
This module provides the backend logic for managing flight records in the Record Management System.

It allows users to:
- Load all flight records from a JSON file.
- Save flight records to the JSON file.
- Create new flight records.
- Search for flight records by ID.
- Generate unique IDs for new flight records.

Classes:
    FlightRecord: A class containing static methods for managing flight records.
"""

import json  # Importing JSON module for reading and writing JSON files
from conf.config import FLIGHT_FILE  # Import configuration for the flight data file path

class FlightRecord:
    """
    A class to handle operations related to flight records, such as loading, saving, creating, and searching.
    """

    @staticmethod
    def load_all():
        """
        Load all flight records from the JSON file.

        If the file is missing or contains invalid data, return an empty list.

        Returns:
            list: A list of dictionaries representing all flight records.
        """
        try:
            # Open the JSON file in read mode and load the records
            with open(FLIGHT_FILE, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file is missing or invalid, return an empty list
            return []

    @staticmethod
    def save_all(records):
        """
        Save all flight records to the JSON file.

        Args:
            records (list): A list of dictionaries representing flight records to save.
        """
        # Open the JSON file in write mode and dump the records
        with open(FLIGHT_FILE, "w") as f:
            json.dump(records, f, indent=4)

    @staticmethod
    def create(flight_data):
        """
        Create a new flight record and save it.

        Args:
            flight_data (dict): A dictionary containing flight information, such as client ID, airline ID, date, start city, and end city.
        """
        # Load existing records
        records = FlightRecord.load_all()
        # Append the new record to the list
        records.append(flight_data)
        # Save the updated records list
        FlightRecord.save_all(records)

    @staticmethod
    def search(flight_id):
        """
        Search for a flight by its unique ID.

        Args:
            flight_id (int): The ID of the flight to search for.

        Returns:
            dict: The flight record if found, otherwise None.
        """
        # Load existing records
        records = FlightRecord.load_all()
        # Iterate through records to find a match
        for record in records:
            if record.get("Flight_ID") == flight_id:
                return record
        # Return None if no matching record is found
        return None

    @staticmethod
    def generate_id():
        """
        Generate a unique ID for a new flight record.

        Returns:
            int: A unique flight ID.
        """
        # Load existing records
        records = FlightRecord.load_all()
        # If no records exist, start with ID 1
        if not records:
            return 1
        # Return the maximum existing ID plus one
        return max(record.get("Flight_ID", 0) for record in records) + 1
    
    @staticmethod
    def update(flight_id, updated_data):
        """
        Update an existing flight record.

        Args:
            flight_id (int): The ID of the flight to update.
            updated_data (dict): A dictionary containing the updated flight information.

        Returns:
            bool: True if the record was updated, False if no matching record was found.
        """
        records = FlightRecord.load_all()
        for record in records:
            if record.get("Flight_ID") == flight_id:
                record.update(updated_data)
                FlightRecord.save_all(records)
                return True
        return False

    @staticmethod
    def delete(flight_id):
        """
        Delete a flight record by its ID.

        Args:
            flight_id (int): The ID of the flight to delete.

        Returns:
            bool: True if the record was deleted, False if no matching record was found.
        """
        records = FlightRecord.load_all()
        updated_records = [record for record in records if record.get("Flight_ID") != flight_id]
        if len(records) != len(updated_records):
            FlightRecord.save_all(updated_records)
            return True
        return False