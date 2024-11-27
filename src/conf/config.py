"""
This module configures file paths and settings for the Record Management System.

It provides:
- Paths for storing client, airline, and flight data in JSON files.
- GUI settings such as window title and size.
- Debugging options to print paths for verification.

Attributes:
    BASE_DIR (str): The directory containing this config file.
    DATA_DIR (str): The directory where data files are stored.
    CLIENT_FILE (str): Path to the file storing client records.
    AIRLINE_FILE (str): Path to the file storing airline records.
    FLIGHT_FILE (str): Path to the file storing flight records.
    WINDOW_TITLE (str): Title of the application window.
    WINDOW_SIZE (str): Size of the application window (width x height).
"""

import os  # We need Python’s os module for managing file paths.

# Get the absolute path of the directory containing this file (config.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the path to the data directory, relative to BASE_DIR
DATA_DIR = os.path.join(BASE_DIR, "../data")

# Define the file path for storing client records
CLIENT_FILE = os.path.join(DATA_DIR, "clients.json")

# Define the file path for storing airline records
AIRLINE_FILE = os.path.join(DATA_DIR, "airlines.json")

# Define the file path for storing flight records
FLIGHT_FILE = os.path.join(DATA_DIR, "flights.json")

# GUI settings
# Title of the application window
WINDOW_TITLE = "Record Management System"

# Size of the application window (width x height)
WINDOW_SIZE = "800x600"

# Debugging: Print all paths if the script is run directly
if __name__ == "__main__":
    print("BASE_DIR:", BASE_DIR)  # Debug: Print the base directory path
    print("DATA_DIR:", DATA_DIR)  # Debug: Print the data directory path
    print("CLIENT_FILE:", CLIENT_FILE)  # Debug: Print the client file path
    print("AIRLINE_FILE:", AIRLINE_FILE)  # Debug: Print the airline file path
    print("FLIGHT_FILE:", FLIGHT_FILE)  # Debug: Print the flight file path
