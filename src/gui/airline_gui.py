"""
This module contains the GUI for managing airline records on the Record Management System.

It allows users to:
- Insert new records of an airline with a company name.
- Save records using the backend which is implemented within the AirlineRecord class.

Functions:
    manage_airline_gui: Opens the GUI screen for maintaining airline informatiuon.
"""

import tkinter as tk  # Importing tkinter for creating GUI
from tkinter import messagebox  # Importing messagebox for user notifications
from record.airline import AirlineRecord  # Importing backend logic for managing airline records

def manage_airline_gui():
    """
    Open the graphical user interface to manage airline records.

    The GUI allows the user to:
    – Type the name of an airline company.
    - Save the airline record to the data file.
    """
    # Create a new top-level window for managing airline records
    window = tk.Toplevel()
    window.title("Airline Records")  # Set the window title
    window.geometry("600x300")  # Set the window size (width x height)

    # Add a label and entry field for the airline company name
    tk.Label(window, text="Company Name:").grid(row=0, column=0, padx=10, pady=5)  # Label for the company name
    company_name_entry = tk.Entry(window)  # Entry field for user input
    company_name_entry.grid(row=0, column=1, padx=10, pady=5)  # Position the entry field

    def save_airline():
        """
        Save a new airline record.

        Collects user input for the company name, generates a unique ID, 
        and saves the record using the AirlineRecord class.

        If the operation succeeds, shows a success message.
        If an error occurs, displays an error message.
        """
        # Create a dictionary to store airline data
        airline_data = {
            "ID": AirlineRecord.generate_id(),  # Generate a unique ID for the airline
            "Type": "Airline",  # Specify the record type
            "Company Name": company_name_entry.get(),  # Get the company name from the entry field
        }
        try:
            # Save the airline record using backend logic
            AirlineRecord.create(airline_data)
            messagebox.showinfo("Success", "Airline record created!")  # Show success message
        except Exception as e:
            messagebox.showerror("Error", str(e))  # Show error message if saving fails

    # Add a button to save the airline record
    tk.Button(window, text="Save", command=save_airline).grid(row=1, column=0, columnspan=2, pady=10)
    # Position the save button and assign the save_airline function to it
