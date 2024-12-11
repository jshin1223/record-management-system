"""
This module builds the first part of the graphical user interface (GUI) for the Record Management System.

It provides a menu to navigate between:
- Client Records
- Airline Records
- Flight Records

Functions:
    create_gui: Opens the main window for records management.
"""

import tkinter as tk  # Importing tkinter for creating GUI components
from gui.client_gui import manage_client_gui  # Import the client management GUI
from gui.airline_gui import manage_airline_gui  # Import the airline management GUI
from gui.flight_gui import manage_flight_gui  # Import the flight management GUI

def create_gui():
    """
    Opens the main GUI of the Record Management System.

    The main GUI:
    - Contains a drop down menu for three kinds of record management sections.
    - Provides navigation to the Client, Airline, and Flight Record Management windows.
    """
    # Create the main application window
    root = tk.Tk()
    root.title("Record Management System")  # Set the window title
    root.geometry("800x600")  # Set the window size (width x height)

    # Create a menu bar for navigation
    menu = tk.Menu(root)  # Create a Menu widget
    root.config(menu=menu)  # Configure the root window to use the menu

    # Add a "Records" menu to the menu bar
    record_menu = tk.Menu(menu)  # Create a submenu for records
    menu.add_cascade(label="Records", menu=record_menu)  # Add the submenu to the menu bar

    # Add menu items to navigate to specific record management windows
    record_menu.add_command(label="Client Records", command=manage_client_gui)  # Open Client Records GUI
    record_menu.add_command(label="Airline Records", command=manage_airline_gui)  # Open Airline Records GUI
    record_menu.add_command(label="Flight Records", command=manage_flight_gui)  # Open Flight Records GUI

    # Start the main event loop for the application
    root.mainloop()

# Run the GUI if the script is executed directly
if __name__ == "__main__":
    create_gui()