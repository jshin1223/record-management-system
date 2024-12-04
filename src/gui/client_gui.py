"""
This module contains the GUI for maintaining client records in Record Management System.

It allows users to:
- Insert new entries in a client register with details like client s name, the address and phone number.
- Look for a specific client when you need to know their record identification number.
- Display search results.

Functions:
    manage_client_gui: Opens the GUI screen for working with client informatiuon.
"""

import tkinter as tk  # Importing tkinter for creating GUI components
from tkinter import messagebox  # Importing messagebox for displaying success or error messages
from record.client import ClientRecord  # Importing backend logic for managing client records

def manage_client_gui():
    """
    Starts the GUI window for creating client record.

    The GUI allows the user to:
    - Enter client details, for instance, name and address and phone number.
    - Store the details of the client into the data file.
    - Use the ID and find a client then show the returned record.
    """
    # Create a new top-level window for managing client records
    window = tk.Toplevel()
    window.title("Client Records")  # Set the window title
    window.geometry("600x650")  # Set the window size (width x height)

    # Add labels and entry fields for client data input
    tk.Label(window, text="Name:").grid(row=0, column=0, padx=10, pady=5)  # Label for Name
    name_entry = tk.Entry(window)  # Entry field for Name
    name_entry.grid(row=0, column=1, padx=10, pady=5)  # Position the entry field

    tk.Label(window, text="Address Line 1:").grid(row=1, column=0, padx=10, pady=5)  # Label for Address Line 1
    address1_entry = tk.Entry(window)  # Entry field for Address Line 1
    address1_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(window, text="Address Line 2:").grid(row=2, column=0, padx=10, pady=5)  # Label for Address Line 2
    address2_entry = tk.Entry(window)  # Entry field for Address Line 2
    address2_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(window, text="Address Line 3:").grid(row=3, column=0, padx=10, pady=5)  # Label for Address Line 3
    address3_entry = tk.Entry(window)  # Entry field for Address Line 3
    address3_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(window, text="City:").grid(row=4, column=0, padx=10, pady=5)  # Label for City
    city_entry = tk.Entry(window)  # Entry field for City
    city_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(window, text="State:").grid(row=5, column=0, padx=10, pady=5)  # Label for State
    state_entry = tk.Entry(window)  # Entry field for State
    state_entry.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(window, text="Zip Code:").grid(row=6, column=0, padx=10, pady=5)  # Label for Zip Code
    zip_entry = tk.Entry(window)  # Entry field for Zip Code
    zip_entry.grid(row=6, column=1, padx=10, pady=5)

    tk.Label(window, text="Country:").grid(row=7, column=0, padx=10, pady=5)  # Label for Country
    country_entry = tk.Entry(window)  # Entry field for Country
    country_entry.grid(row=7, column=1, padx=10, pady=5)

    tk.Label(window, text="Phone Number:").grid(row=8, column=0, padx=10, pady=5)  # Label for Phone Number
    phone_entry = tk.Entry(window)  # Entry field for Phone Number
    phone_entry.grid(row=8, column=1, padx=10, pady=5)

    # Helper message below the Phone Number field
    tk.Label(window, text="Follow the format CountryCode-AreaCode-Number (e.g., 1-773-5435432)", 
         font=("Arial", 9), fg="gray").grid(row=9, column=0, columnspan=2, padx=10, pady=2)

    # Textbox for displaying search results
    result_text = tk.Text(window, height=8, width=50)  # Multi-line textbox for displaying search results
    result_text.grid(row=10, column=0, columnspan=2, padx=10, pady=5)

    def save_client():
        """
        Save a new client record.

        Takes the data entered by the user on the entry fields, creates a new record ID.
        and writes the record to the file using ClientRecord class.

        if the operation is successful display success message.
        If an error happens, outputs an error message.
        """
        # Create a dictionary to store client data
        client_data = {
            "ID": ClientRecord.generate_id(),  # Generate a unique ID for the client
            "Type": "Client",  # Specify the record type
            "Name": name_entry.get(),  # Get the name from the entry field
            "Address Line 1": address1_entry.get(),  # Get Address Line 1
            "Address Line 2": address2_entry.get(),  # Get Address Line 2
            "Address Line 3": address3_entry.get(),  # Get Address Line 3
            "City": city_entry.get(),  # Get City
            "State": state_entry.get(),  # Get State
            "Zip Code": zip_entry.get(),  # Get Zip Code
            "Country": country_entry.get(),  # Get Country
            "Phone Number": phone_entry.get(),  # Get Phone Number
        }
        try:
            # Save the client record using backend logic
            ClientRecord.create(client_data)
            messagebox.showinfo("Success", "Client record created!")  # Show success message
        except Exception as e:
            messagebox.showerror("Error", str(e))  # Show error message if saving fails

    def search_client():
        """
        Search for a client by ID.

        Pulls the original client ID of the record from the search entry field and looks for the record.
        The value is shown in the result textbox.

        If no record is found, shows a “Not Found” message.
        """
        try:
            client_id = int(search_entry.get())  # Get the client ID from the search field
            record = ClientRecord.search(client_id)  # Search for the client record by ID
            if record:
                result_text.delete(1.0, tk.END)  # Clear the textbox
                result_text.insert(tk.END, f"Client Found:\n{record}")  # Display the record
            else:
                messagebox.showinfo("Not Found", "No client found with the given ID.")  # Show not found message
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric ID.")  # Handle invalid input

  # Delete client
    def delete_client():
        try:
            client_id = int(search_entry.get())
            if ClientRecord.delete(client_id):
                messagebox.showinfo("Success", "Client record deleted!")
            else:
                messagebox.showinfo("Not Found", "No client found with the given ID.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric ID.")

    # Update client
    def update_client():
        try:
            # Ensure the search_entry value is retrieved correctly
            if not search_entry.get().strip():
                messagebox.showerror("Error", "Client ID cannot be empty. Please provide a valid ID.")
                return
            
            client_id = search_entry.get().strip()
            print(f"Debug: Client ID retrieved from search_entry: {client_id}")  # Debug print

            client_id = int(client_id)  # Retrieve Client ID and convert to integer
            print(f"Debug: Client ID after conversion to integer: {client_id}")  # Debug print

            client_id = int(search_entry.get().strip())  # Retrieve Client ID
            updated_data = {
                "Name": name_entry.get().strip(),
                "Address Line 1": address1_entry.get().strip(),
                "Address Line 2": address2_entry.get().strip(),
                "Address Line 3": address3_entry.get().strip(),
                "City": city_entry.get().strip(),
                "State": state_entry.get().strip(),
                "Zip Code": zip_entry.get().strip(),
                "Country": country_entry.get().strip(),
                "Phone Number": phone_entry.get().strip(),
            }

            print(f"Debug: Updated data to be sent to backend: {updated_data}")  # Debug print

            # Perform update operation
            if ClientRecord.update(client_id, updated_data):
                messagebox.showinfo("Success", "Client record updated!")
            else:
                messagebox.showinfo("Not Found", "No client found with the given ID.")
        except ValueError as ve:
                # Specific ValueError from the backend should show its error message
                if "Invalid phone number format" in str(ve):
                    messagebox.showerror("Error", str(ve))  # Show specific backend error
                else:
                    messagebox.showerror("Error", "Please enter a valid numeric ID.")  # Generic error
        except Exception as e:
            # Handle any other unforeseen exceptions
            messagebox.showerror("Error", str(e))

    # Add a label and entry field for searching client records by ID
    tk.Label(window, text="Client ID:", anchor="e").grid(row=11, column=0, padx=(20, 5), pady=5, sticky="e")  # Adjusted padx and alignment
    search_entry = tk.Entry(window, justify="center")  # Entry field for search input
    search_entry.grid(row=11, column=1, padx=5, pady=5, sticky="w")  # Kept the search box aligned

    # Add a helper message below the Client ID
    tk.Label(window, text="Input Client ID to search, update, or delete client records", 
         font=("Arial", 9), fg="gray", anchor="center").grid(row=13, column=0, columnspan=2, pady=5)

    # Delete, Update, and Search Buttons are placed at the botrom of the window (aligned horizontally in the same row). 
    button_frame = tk.Frame(window)  # Create a frame to hold the buttons
    button_frame.grid(row=912, column=0, columnspan=3, pady=10)  # Place the frame in the grid

    tk.Button(button_frame, text="Save", command=save_client).grid(row=9, column=1, padx=10, pady=10) # Save Button
    tk.Button(button_frame, text="Search", command=search_client).grid(row=9, column=2, padx=10, pady=10)  # Search Button
    tk.Button(button_frame, text="Update", command=update_client).grid(row=9, column=3, padx=10, pady=10)  # Update Button
    tk.Button(button_frame, text="Delete", command=delete_client).grid(row=9, column=4, padx=10, pady=10)  # Delete Button


    
    


