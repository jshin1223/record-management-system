import tkinter as tk
from tkinter import messagebox
from record.client import ClientRecord


def manage_client_gui():
    """
    Launch the GUI for managing client records.

    The GUI allows users to:
    - Save new client records
    - Update existing client records
    - Delete client records
    - Search for client records by ID
    """

    def save_client():
        """
        Save a new client record.

        Collects client data from input fields, validates it,
        and saves it using the backend logic.
        """
        try:
            client_data = {
                "ID": ClientRecord.generate_id(),
                "Name": name_entry.get(),
                "Address Line 1": address1_entry.get(),
                "Address Line 2": address2_entry.get(),
                "Address Line 3": address3_entry.get(),
                "City": city_entry.get(),
                "State": state_entry.get(),
                "Zip Code": zip_entry.get(),
                "Country": country_entry.get(),
                "Phone Number": phone_entry.get(),
            }
            # Save the client record
            ClientRecord.create(client_data)
            messagebox.showinfo("Success", "Client record created!")
            clear_inputs()  # Clear the input fields after saving
        except ValueError as ve:
            # Display specific error messages from the backend
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            # Catch all other exceptions
            messagebox.showerror("Error", str(e))

    def delete_client():
        """
        Delete a client record by ID.

        Retrieves the client ID from the input field and attempts
        to delete the corresponding record.
        """
        try:
            client_id = int(search_entry.get())
            if ClientRecord.delete(client_id):
                messagebox.showinfo("Success", "Client record deleted!")
            else:
                messagebox.showinfo("Not Found", "No client found with the given ID.")
        except ValueError:
            # Error when client ID is not valid
            messagebox.showerror("Invalid Input", "Please enter a valid numeric Client ID.")

    def update_client():
        """
        Update an existing client record.

        Collects the updated data from input fields, validates it,
        and updates the client record using the provided ID.
        """
        try:
            client_id = int(search_entry.get())
            updated_data = {
                "Name": name_entry.get(),
                "Address Line 1": address1_entry.get(),
                "Address Line 2": address2_entry.get(),
                "Address Line 3": address3_entry.get(),
                "City": city_entry.get(),
                "State": state_entry.get(),
                "Zip Code": zip_entry.get(),
                "Country": country_entry.get(),
                "Phone Number": phone_entry.get(),
            }
            if ClientRecord.update(client_id, updated_data):
                messagebox.showinfo("Success", "Client record updated!")
            else:
                messagebox.showinfo("Not Found", "No client found with the given ID.")
        except ValueError as ve:
            # Display specific error messages from the backend (e.g., invalid phone number)
            if "Invalid phone number format" in str(ve):
                messagebox.showerror("Error", str(ve))
            else:
                messagebox.showerror("Error", "Please enter a valid numeric Client ID.")
        except Exception as e:
            # Handle any other unforeseen exceptions
            messagebox.showerror("Error", str(e))

    def search_client():
        """
        Search for a client by ID and display the result.

        Retrieves the client ID from the input field and displays
        the corresponding record in the result box.
        """
        try:
            client_id = int(search_entry.get())
            record = ClientRecord.search(client_id)
            result_text.delete(1.0, tk.END)  # Clear previous search results
            if record:
                # Display the found client record
                result_text.insert(tk.END, f"Client Found:\n")
                for key, value in record.items():
                    result_text.insert(tk.END, f"{key}: {value}\n")
            else:
                # No record found
                messagebox.showinfo("Not Found", "No client found with the given ID.")
        except ValueError:
            # Error when client ID is not valid
            messagebox.showerror("Invalid Input", "Please enter a valid numeric Client ID.")

    def clear_inputs():
        """
        Clear all input fields.

        Resets the input fields for a new operation.
        """
        for entry in [
            name_entry, address1_entry, address2_entry, address3_entry,
            city_entry, state_entry, zip_entry, country_entry, phone_entry, search_entry
        ]:
            entry.delete(0, tk.END)

    def reveal_fields():
        """
        Reveal input fields for managing client records.

        Shows the input fields and action buttons for managing clients.
        """
        y_offset = 480
        for label, entry in field_widgets:
            label.place(relx=0.35, y=y_offset, anchor="center", width=350)
            entry.place(relx=0.65, y=y_offset, anchor="center", width=250)
            y_offset += 40
        save_button.place(relx=0.25, y=y_offset, anchor="center")
        update_button.place(relx=0.5, y=y_offset, anchor="center")
        delete_button.place(relx=0.75, y=y_offset, anchor="center")

    def show_tooltip(event):
        """
        Display tooltip text when the user hovers over the info icon.
        """
        tooltip.place(x=10, y=40)

    def hide_tooltip(event):
        """
        Hide the tooltip when the mouse leaves the info icon.
        """
        tooltip.place_forget()

    # Create a new window for client management
    window = tk.Toplevel()
    window.title("Client Records")
    window.geometry("900x900")
    window.configure(bg="#1C1C1C")

    # Tooltip for additional information
    info_icon = tk.Label(window, text="ⓘ", font=("Helvetica", 14, "bold"), bg="#1C1C1C", fg="#3498DB")
    info_icon.place(x=10, y=10)
    info_icon.bind("<Enter>", show_tooltip)
    info_icon.bind("<Leave>", hide_tooltip)

    tooltip = tk.Label(window, text="Enter client ID number to search or delete.\nWhen recording a new client at the bottom of this screen,\nplease confirm the duplicate client with the same phone number does not already exist.",
                       font=("Helvetica", 10), bg="#333333", fg="white", wraplength=300)
    tooltip.place_forget()

    # Title of the application
    title_label = tk.Label(window, text="Client Record Management", font=("Helvetica", 18, "bold"), bg="#1C1C1C", fg="white")
    title_label.place(relx=0.5, y=50, anchor="center")

    # Input fields and buttons
    search_label = tk.Label(window, text="Client ID:", font=("Helvetica", 12), bg="#1C1C1C", fg="white")
    search_label.place(relx=0.4, y=120, anchor="center")
    search_entry = tk.Entry(window, bg="#333333", fg="white", insertbackground="white")
    search_entry.place(relx=0.6, y=120, anchor="center", width=250)

    search_button = tk.Button(window, text="Search", command=search_client, font=("Helvetica", 12, "bold"), bg="#F39C12", fg="white", activebackground="#D35400", activeforeground="white", width=12)
    search_button.place(relx=0.5, y=160, anchor="center")

    result_text = tk.Text(window, height=10, width=70, bg="#2E2E2E", fg="white", font=("Courier", 10))
    result_text.place(relx=0.5, y=260, anchor="center")

    record_button = tk.Button(window, text="Manage Clients", command=reveal_fields, font=("Helvetica", 12, "bold"), bg="#3498DB", fg="white", activebackground="#2980B9", activeforeground="white", width=20)
    record_button.place(relx=0.5, y=430, anchor="center")

    # Input fields (hidden initially)
    name_label = tk.Label(window, text="Name:", font=("Helvetica", 12), bg="#1C1C1C", fg="white")
    name_entry = tk.Entry(window, bg="#333333", fg="white", insertbackground="white")

    address1_label = tk.Label(window, text="Address Line 1:", font=("Helvetica", 12), bg="#1C1C1C", fg="white")
    address1_entry = tk.Entry(window, bg="#333333", fg="white", insertbackground="white")

    address2_label = tk.Label(window, text="Address Line 2:", font=("Helvetica", 12), bg="#1C1C1C", fg="white")
    address2_entry = tk.Entry(window, bg="#333333", fg="white", insertbackground="white")

    address3_label = tk.Label(window, text="Address Line 3:", font=("Helvetica", 12), bg="#1C1C1C", fg="white")
    address3_entry = tk.Entry(window, bg="#333333", fg="white", insertbackground="white")

    city_label = tk.Label(window, text="City:", font=("Helvetica", 12), bg="#1C1C1C", fg="white")
    city_entry = tk.Entry(window, bg="#333333", fg="white", insertbackground="white")

    state_label = tk.Label(window, text="State:", font=("Helvetica", 12), bg="#1C1C1C", fg="white")
    state_entry = tk.Entry(window, bg="#333333", fg="white", insertbackground="white")

    zip_label = tk.Label(window, text="Zip Code:", font=("Helvetica", 12), bg="#1C1C1C", fg="white")
    zip_entry = tk.Entry(window, bg="#333333", fg="white", insertbackground="white")

    country_label = tk.Label(window, text="Country:", font=("Helvetica", 12), bg="#1C1C1C", fg="white")
    country_entry = tk.Entry(window, bg="#333333", fg="white", insertbackground="white")

    phone_label = tk.Label(window, text="Phone Number:", font=("Helvetica", 12), bg="#1C1C1C", fg="white")
    phone_entry = tk.Entry(window, bg="#333333", fg="white", insertbackground="white")

    save_button = tk.Button(window, text="Save", command=save_client, font=("Helvetica", 12, "bold"), bg="#F39C12", fg="white", activebackground="#D35400", activeforeground="white", width=12)
    update_button = tk.Button(window, text="Update", command=update_client, font=("Helvetica", 12, "bold"), bg="#F39C12", fg="white", activebackground="#1C7A30", activeforeground="white", width=12)
    delete_button = tk.Button(window, text="Delete", command=delete_client, font=("Helvetica", 12, "bold"), bg="#F39C12", fg="white", activebackground="#A93226", activeforeground="white", width=12)

    update_button.place_forget()
    delete_button.place_forget()

    field_widgets = [
        (name_label, name_entry),
        (address1_label, address1_entry),
        (address2_label, address2_entry),
        (address3_label, address3_entry),
        (city_label, city_entry),
        (state_label, state_entry),
        (zip_label, zip_entry),
        (country_label, country_entry),
        (phone_label, phone_entry),
    ]

    for label, entry in field_widgets:
        label.place_forget()
        entry.place_forget()

    window.mainloop()