"""
This module provides the backend logic for managing client records in the Record Management System.

It allows users to:
- Load all client records from a JSON file.
- Save client records to the JSON file.
- Create new client records.
- Search for client records by ID.
- Generate unique IDs for new client records.

Classes:
    ClientRecord: A class containing static methods for managing client records.
"""

import json  # Importing JSON module for reading and writing JSON files
from conf.config import CLIENT_FILE  # Import configuration for the client data file path

class ClientRecord:
    """
    A class to handle operations related to client records, such as loading, saving, creating, and searching.
    """

    @staticmethod
    def load_all():
        """
        Load all client records from the JSON file.

        If the file is missing or contains invalid data, return an empty list.

        Returns:
            list: A list of dictionaries representing all client records.
        """
        try:
            # Open the JSON file in read mode and load the records
            with open(CLIENT_FILE, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file is missing or invalid, return an empty list
            return []

    @staticmethod
    def save_all(records):
        """
        Save all client records to the JSON file.

        Args:
            records (list): A list of dictionaries representing client records to save.
        """
        # Open the JSON file in write mode and dump the records
        with open(CLIENT_FILE, "w") as f:
            json.dump(records, f, indent=4)

    @staticmethod
    def create(client_data):
        """
        Create a new client record and save it.

        Args:
            client_data (dict): A dictionary containing client information, including ID, name, and address.
        """
        # Load existing records
        records = ClientRecord.load_all()
        # Append the new record to the list
        records.append(client_data)
        # Save the updated records list
        ClientRecord.save_all(records)

    @staticmethod
    def search(client_id):
        """
        Search for a client by its unique ID.

        Args:
            client_id (int): The ID of the client to search for.

        Returns:
            dict: The client record if found, otherwise None.
        """
        # Load existing records
        records = ClientRecord.load_all()
        # Iterate through records to find a match
        for record in records:
            if record["ID"] == client_id:
                return record
        # Return None if no matching record is found
        return None

    @staticmethod
    def generate_id():
        """
        Generate a unique ID for a new client.

        Returns:
            int: A unique ID for the new client record.
        """
        # Load existing records
        records = ClientRecord.load_all()
        # If no records exist, start with ID 1
        if not records:
            return 1
        # Return the maximum existing ID plus one
        return max(record["ID"] for record in records) + 1