"""
This module contains the GUI for the Record Management System for managing flight records.

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
    window.geometry("600x500")  # Set the window size (width x height)

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

    def search_flight():
        """
        Search for a flight by ID and display the result.
        """
        try:
            flight_id = int(flight_id_entry.get())
            record = FlightRecord.search(flight_id)
            if record:
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, f"Flight Found:\n{record}")
            else:
                messagebox.showinfo("Not Found", "No flight found with the given ID.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric ID.")

    def update_flight():
        """
        Update an existing flight record.
        """
        try:
            flight_id = int(flight_id_entry.get())
            updated_data = {
                "Client_ID": int(client_id_entry.get()),
                "Airline_ID": int(airline_id_entry.get()),
                "Date/Time": date_entry.get(),
                "Start City": start_city_entry.get(),
                "End City": end_city_entry.get(),
            }
            if FlightRecord.update(flight_id, updated_data):
                messagebox.showinfo("Success", "Flight record updated!")
            else:
                messagebox.showinfo("Not Found", "No flight found with the given ID.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numeric IDs for Flight ID, Client ID, and Airline ID.")

    def delete_flight():
        """
        Delete a flight record by ID.
        """
        try:
            flight_id = int(flight_id_entry.get())
            if FlightRecord.delete(flight_id):
                messagebox.showinfo("Success", "Flight record deleted!")
            else:
                messagebox.showinfo("Not Found", "No flight found with the given ID.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric ID.")

    # Textbox for displaying search results
    result_text = tk.Text(window, height=8, width=50)
    result_text.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

    # Flight ID Label and Entry
    tk.Label(window, text="Flight ID:").grid(row=7, column=0, padx=10, pady=5, sticky="e")
    flight_id_entry = tk.Entry(window)
    flight_id_entry.grid(row=7, column=1, padx=10, pady=5, sticky="w")

    # Helper message below Flight ID
    tk.Label(window, text="Input Flight ID to search, update, or delete", font=("Arial", 9), fg="gray").grid(row=8, column=0, columnspan=2, pady=2, sticky="n")

    # Add buttons for search, update, and delete
    button_frame = tk.Frame(window)
    button_frame.grid(row=9, column=0, columnspan=2, pady=10)

    tk.Button(button_frame, text="Save", command=save_flight).pack(side="left", padx=5)
    tk.Button(button_frame, text="Search", command=search_flight).pack(side="left", padx=5)
    tk.Button(button_frame, text="Update", command=update_flight).pack(side="left", padx=5)
    tk.Button(button_frame, text="Delete", command=delete_flight).pack(side="left", padx=5)