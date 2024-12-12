"""
This module serves as the entry point for the Record Management System application.

It:
- Configures the Python path to include the project root directory.
- Launches the main GUI of the application.
"""

import sys  # Importing sys to manipulate the Python path
import os  # Importing os to work with file system paths

# Add the project root directory to PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# This ensures Python can locate the `gui` package and other modules in the project.
from gui.main_gui import create_gui  # Import the function to create the main GUI

if __name__ == "__main__":
    """
    If this script is run directly, it opens the GUI for Record Management System.
    """
    print("Launching GUI...")  # Debugging log to indicate the GUI is starting
    create_gui()  # Call the function to create and launch the main GUI