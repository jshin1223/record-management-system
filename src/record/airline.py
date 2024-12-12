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

        This method overwrites the existing data in the file with the provided records.
        """
        # Open the JSON file in write mode and dump the records
        with open(AIRLINE_FILE, "w") as f:
            json.dump(records, f, indent=4)

    @staticmethod
    def is_duplicate_airline_name(company_name):
        """
        Check for duplicate airline names.

        Args:
            company_name (str): The airline company name to check.

        Returns:
            bool: True if a duplicate exists, False otherwise.

        This method ensures no two airlines have the same company name, irrespective of case sensitivity.
        """
        records = AirlineRecord.load_all()
        return any(record["Company Name"].lower() == company_name.lower() for record in records)

    @staticmethod
    def create(airline_data):
        """
        Create a new airline record with validations that check for pre-existing duplicate records.

        Args:
            airline_data (dict): A dictionary containing airline information, including ID and company name.

        Raises:
            ValueError: If a duplicate company name is detected.
        """
        if AirlineRecord.is_duplicate_airline_name(airline_data["Company Name"]):
            raise ValueError("Duplicate airline name detected.")
        
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

        This method iterates through the list of records to find a matching ID.
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

        This method ensures IDs are incremental and unique, starting from 1.
        """
        # Load existing records
        records = AirlineRecord.load_all()
        # If no records exist, start with ID 1
        if not records:
            return 1
        # Return the maximum existing ID plus one
        return max(record["ID"] for record in records) + 1
    
    @staticmethod
    def search_by_name(company_name):
        """
        Search for an airline by company name.

        Args:
            company_name (str): The name of the airline company to search for.

        Returns:
            dict: The airline record if found, otherwise None.

        This method performs a case-insensitive search for the given company name.
        """
        records = AirlineRecord.load_all()
        for record in records:
            if record["Company Name"].lower() == company_name.lower():
                return record
        return None

    @staticmethod
    def update_airline(airline_id, new_data):
        """
        Update an existing airline record with validations that check for duplicate company names.

        Args:
            airline_id (int): The ID of the airline to update.
            new_data (dict): A dictionary containing updated airline information.

        Returns:
            bool: True if the record was updated, False if not found.

        Raises:
            ValueError: If the updated company name is a duplicate.
        """
        if AirlineRecord.is_duplicate_airline_name(new_data["Company Name"]):
            raise ValueError("Duplicate airline name detected.")
        
        records = AirlineRecord.load_all()
        for record in records:
            if record["ID"] == airline_id:
                record.update(new_data)
                AirlineRecord.save_all(records)
                return True
        return False

    @staticmethod
    def delete_airline(airline_id):
        """
        Delete an airline record by its ID.

        Args:
            airline_id (int): The ID of the airline to delete.

        Returns:
            bool: True if the record was deleted, False if not found.

        This method removes the record with the specified ID from the list and saves the updated list.
        """
        records = AirlineRecord.load_all()
        updated_records = [record for record in records if record["ID"] != airline_id]
        if len(updated_records) < len(records):
            AirlineRecord.save_all(updated_records)
            return True
        return False