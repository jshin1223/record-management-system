"""
This module contains the GUI forf the Record Management System for managing flight records.

It allows users to:
- Add new flight records with client ID, airline ID, flight date and starting and ending cities.
- Use the FlightRecord class to continue the storage of flight records.

Functions:
    manage_flight_gui: Opens the GUI screen for managing flight informatiuon.
"""

import tkinter as tk  # Importing tkinter for creating GUI components
from tkinter import messagebox  # Importing messagebox for displaying success or error messages
from record.flight import FlightRecord  # Importing backend logic for managing flight records

def manage_flight_gui():
    """
    Launches the GUI window for managing flight records.

    The GUI allows the user to:
    - Input flight details such as client ID, airline ID, date, start city, and end city.
    - Save the flight record to the data file.
    """
    # Create a new top-level window for managing flight records
    window = tk.Toplevel()
    window.title("Flight Records")  # Set the window title
    window.geometry("600x400")  # Set the window size (width x height)

    # Add labels and entry fields for flight data input
    tk.Label(window, text="Client ID:").grid(row=0, column=0, padx=10, pady=5)  # Label for Client ID
    client_id_entry = tk.Entry(window)  # Entry field for Client ID
    client_id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(window, text="Airline ID:").grid(row=1, column=0, padx=10, pady=5)  # Label for Airline ID
    airline_id_entry = tk.Entry(window)  # Entry field for Airline ID
    airline_id_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(window, text="Date and Time (YYYY-MM-DD HH:MM):").grid(row=2, column=0, padx=10, pady=5)  # Label for Date
    date_entry = tk.Entry(window)  # Entry field for Date
    date_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(window, text="Start City:").grid(row=3, column=0, padx=10, pady=5)  # Label for Start City
    start_city_entry = tk.Entry(window)  # Entry field for Start City
    start_city_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(window, text="End City:").grid(row=4, column=0, padx=10, pady=5)  # Label for End City
    end_city_entry = tk.Entry(window)  # Entry field for End City
    end_city_entry.grid(row=4, column=1, padx=10, pady=5)

    def save_flight():
        """
        Save a new flight record.

        Reads user input from the entry fields, creates flight unique ID.
        and saves the record using the FlightRecord class.

        If the operation executes well, shows a success message.
        If there is an error then shows an error message.
        """
        # Create a dictionary to store flight data
        flight_data = {
            "Flight_ID": FlightRecord.generate_id(),  # Generate a unique ID for the flight
            "Client_ID": int(client_id_entry.get()),  # Get the Client ID from the entry field
            "Airline_ID": int(airline_id_entry.get()),  # Get the Airline ID from the entry field
            "Date/Time": date_entry.get(),  # Get the Date from the entry field
            "Start City": start_city_entry.get(),  # Get the Start City from the entry field
            "End City": end_city_entry.get(),  # Get the End City from the entry field
        }
        try:
            # Save the flight record using backend logic
            FlightRecord.create(flight_data)
            messagebox.showinfo("Success", "Flight record created!")  # Show success message
        except Exception as e:
            messagebox.showerror("Error", str(e))  # Show error message if saving fails

    # Add a button to save the flight record
    tk.Button(window, text="Save", command=save_flight).grid(row=5, column=0, columnspan=2, pady=10)
    # Position the save button and assign the save_flight function to it
