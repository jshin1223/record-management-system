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
import re  # Regular expression for validation
from src.conf.config import CLIENT_FILE  # Import configuration for the client data file path

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
    def is_duplicate_phone(phone_number):
        """
        Check for duplicate phone numbers in client records.

        Args:
            phone_number (str): The phone number to check.

        Returns:
            bool: True if a duplicate exists, False otherwise.
        """
        records = ClientRecord.load_all()
        return any(record["Phone Number"] == phone_number for record in records)

    @staticmethod
    def is_valid_phone(phone_number):
        """
        Validate the format of the phone number.

        Args:
            phone_number (str): The phone number to validate.

        Returns:
            bool: True if the phone number format is valid, False otherwise.
        """
        pattern = r"^\d{1,3}-\d{1,3}-\d{4,10}$"
        return bool(re.match(pattern, phone_number))

    @staticmethod
    def create(client_data):
        """
        Create a new client record with validations that check pre-existing duplicate records. 

        Args:
            client_data (dict): A dictionary containing client information, including ID, name, and address.
        """
        if not ClientRecord.is_valid_phone(client_data["Phone Number"]):
            raise ValueError("Invalid phone number format. Follow CountryCode-AreaCode-Number (e.g., 1-773-5435432).")
        if ClientRecord.is_duplicate_phone(client_data["Phone Number"]):
            raise ValueError("Duplicate phone number detected.")

        # Load existing records
        records = ClientRecord.load_all()
        # Append the new record to the list
        records.append(client_data)
        # Save the updated records list
        ClientRecord.save_all(records)


    @staticmethod
    def delete(client_id):
        """
        Delete a client record by ID.

        Args:
            client_id (int): The ID of the client to delete.

        Returns:
            bool: True if the record was deleted, False if not found.
        """
        records = ClientRecord.load_all()
        updated_records = [record for record in records if record["ID"] != client_id]
        if len(records) == len(updated_records):
            return False  # No record was deleted
        ClientRecord.save_all(updated_records)
        return True

    @staticmethod
    def update(client_id, updated_data):
        """
        Update a client record by ID with validations that check pre-existing duplicate records.

        Args:
            client_id (int): The ID of the client to update.
            updated_data (dict): The updated data for the client.

        Returns:
            bool: True if the record was updated, False if not found.
        """
        if not ClientRecord.is_valid_phone(updated_data["Phone Number"]):
            raise ValueError("Invalid phone number format. Follow CountryCode-AreaCode-Number (e.g., 1-773-5435432).")
        # if ClientRecord.is_duplicate_phone(updated_data["Phone Number"]):
        #     raise ValueError("Duplicate phone number detected.")
        
        records = ClientRecord.load_all()
        for record in records:
            if record["ID"] == client_id:
                record.update(updated_data)
                ClientRecord.save_all(records)
                return True
        return False

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