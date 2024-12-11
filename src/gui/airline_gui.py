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

    # Airline ID Label and Entry
    tk.Label(window, text="Airline ID:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    airline_id_entry = tk.Entry(window)
    airline_id_entry.grid(row=1, column=1, padx=10, pady=5)

    # Company Name Label and Entry
    tk.Label(window, text="Company Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    company_name_entry = tk.Entry(window)
    company_name_entry.grid(row=0, column=1, padx=10, pady=5)

    # Add helper messages
    tk.Label(window, text="Input Airline ID to update or delete airline records", font=("Arial", 9), fg="gray").grid(row=3, column=1, padx=10, pady=2, sticky="w")
    tk.Label(window, text="Input company name to save or search airline records", font=("Arial", 9), fg="gray").grid(row=2, column=1, padx=10, pady=2, sticky="w")

    def save_airline():
        """
        Save a new airline record.
        """
        airline_data = {
            "ID": AirlineRecord.generate_id(),  # Generate a unique ID for the airline
            "Type": "Airline",  # Specify the record type
            "Company Name": company_name_entry.get(),  # Get the company name from the entry field
        }
        try:
            AirlineRecord.create(airline_data)
            messagebox.showinfo("Success", "Airline record created!")  # Show success message
        except Exception as e:
            messagebox.showerror("Error", str(e))  # Show error message if saving fails

    def search_airline():
        """
        Search for an airline by company name.
        """
        company_name = company_name_entry.get()
        result = AirlineRecord.search_by_name(company_name)
        if result:
            messagebox.showinfo("Search Result", f"Found: {result}")
        else:
            messagebox.showwarning("Not Found", "No airline found with the given company name.")

    def update_airline():
        """
        Update an existing airline record.
        """
        try:
            if not airline_id_entry.get().strip():
                messagebox.showerror("Error", "Airline ID cannot be empty. Please enter a valid ID.")
                return
            airline_id = int(airline_id_entry.get().strip())
            new_name = company_name_entry.get().strip()

            if not new_name:
                messagebox.showerror("Error", "Company Name cannot be empty. Please provide a name.")
                return

            # Get the current airline record
            current_record = AirlineRecord.search(airline_id)
            if not current_record:
                messagebox.showwarning("Not Found", "No airline found with the given ID.")
                return
            
            # Check if the new name is the same as the existing name
            if current_record["Company Name"].strip().lower() == new_name.lower():
                messagebox.showinfo("No Changes", "No changes detected. The airline name is already up-to-date.")
                return
        
            # Call the update function from AirlineRecord
            if AirlineRecord.update_airline(airline_id, {"Company Name": new_name}):
                messagebox.showinfo("Success", "Airline record updated successfully!")
            else:
                messagebox.showwarning("Not Found", "No airline found with the given ID.")
        except ValueError:
                messagebox.showerror("Error", "Invalid ID. Please enter a numeric value.")

    def delete_airline():
        """
        Delete an airline by its ID.
        """
        try:
            airline_id = int(airline_id_entry.get())
            if AirlineRecord.delete_airline(airline_id):
                messagebox.showinfo("Success", "Airline record deleted successfully!")
            else:
                messagebox.showwarning("Not Found", "No airline found with the given ID.")
        except ValueError:
            messagebox.showerror("Error", "Invalid ID. Please enter a numeric value.")

    # Add a frame for buttons at the bottom
    button_frame = tk.Frame(window)
    button_frame.grid(row=4, column=0, columnspan=2, pady=20)

    # Add buttons to the frame for horizontal alignment
    tk.Button(button_frame, text="Save", command=save_airline).pack(side="left", padx=5)
    tk.Button(button_frame, text="Search", command=search_airline).pack(side="left", padx=5)
    tk.Button(button_frame, text="Update", command=update_airline).pack(side="left", padx=5)
    tk.Button(button_frame, text="Delete", command=delete_airline).pack(side="left", padx=5)
