import tkinter as tk
from tkinter import messagebox
from record.flight import FlightRecord


def manage_flight_gui():
    """
    Launch the GUI for managing flight records.

    The GUI allows users to:
    - Save new flight records
    - Update existing flight records
    - Delete flight records
    - Search for flight records by ID
    """

    def save_flight():
        """
        Save a new flight record.

        Collects flight data from input fields, validates it, and saves it using the backend logic.
        Ensures that duplicate flights with the same Client ID, Airline ID, and Date/Time are not created.
        """
        try:
            flight_data = {
                "Flight_ID": FlightRecord.generate_id(),
                "Client_ID": int(client_id_entry.get()),
                "Airline_ID": int(airline_id_entry.get()),
                "Date/Time": date_entry.get(),
                "Start City": start_city_entry.get(),
                "End City": end_city_entry.get(),
            }

            # Check for duplicate flight records
            if FlightRecord.is_duplicate_flight(
                flight_data["Client_ID"], flight_data["Airline_ID"], flight_data["Date/Time"]
            ):
                messagebox.showerror("Error", "Duplicate flight record detected.")
                return

            # Save the flight record
            FlightRecord.create(flight_data)
            messagebox.showinfo("Success", "Flight record created successfully!")
            clear_inputs()  # Clear the input fields after saving
        except ValueError as ve:
            # Check for specific backend validation errors
            if "Invalid date and time format" in str(ve):
                messagebox.showerror("Error", str(ve))  # Display date/time format errors
            else:
                messagebox.showerror("Error", "Please enter valid numeric Flight ID.")
        except Exception as e:
            # Catch all other exceptions
            messagebox.showerror("Error", str(e))

    def delete_flight():
        """
        Delete a flight record by ID.

        Retrieves the flight ID from the input field and attempts to delete the corresponding record.
        """
        try:
            flight_id = int(flight_id_entry.get())
            if FlightRecord.delete(flight_id):
                messagebox.showinfo("Success", "Flight record deleted!")
            else:
                messagebox.showinfo("Not Found", "No flight found with the given ID.")
        except ValueError:
            # Error when flight ID is not valid
            messagebox.showerror("Invalid Input", "Please enter a valid numeric Flight ID.")

    def update_flight():
        """
        Update an existing flight record.

        Collects updated flight data from input fields, validates it, and updates the record using the provided ID.
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
            # Update the flight record
            if FlightRecord.update(flight_id, updated_data):
                messagebox.showinfo("Success", "Flight record updated!")
            else:
                messagebox.showinfo("Not Found", "No flight found with the given ID.")
        except ValueError as ve:
            # Display specific error messages from the backend
            if "Invalid date and time format" in str(ve):
                messagebox.showerror("Error", str(ve))
            else:
                messagebox.showerror("Error", "Please enter valid numeric Flight ID.")
        except Exception as e:
            # Catch all other exceptions
            messagebox.showerror("Error", str(e))

    def search_flight():
        """
        Search for a flight by ID and display the result.

        Retrieves the flight ID from the input field and displays the corresponding record in the result box.
        """
        try:
            flight_id = int(flight_id_entry.get())
            record = FlightRecord.search(flight_id)
            result_text.delete(1.0, tk.END)  # Clear previous search results
            if record:
                # Display the found flight record
                result_text.insert(tk.END, f"Flight Found:\n")
                for key, value in record.items():
                    result_text.insert(tk.END, f"{key}: {value}\n")
            else:
                # No record found
                messagebox.showinfo("Not Found", "No flight found with the given ID.")
        except ValueError:
            # Error when flight ID is not valid
            messagebox.showerror("Invalid Input", "Please enter a valid numeric Flight ID.")

    def clear_inputs():
        """
        Clear all input fields.

        Resets the input fields for a new operation.
        """
        for entry in [client_id_entry, airline_id_entry, date_entry, start_city_entry, end_city_entry, flight_id_entry]:
            entry.delete(0, tk.END)

    def reveal_fields():
        """
        Reveal input fields for managing flight records.

        Shows the input fields and action buttons for managing flights.
        """
        y_offset = 480
        for label, entry in field_widgets:
            label.place(relx=0.35, y=y_offset, anchor="center", width=350)
            entry.place(relx=0.65, y=y_offset, anchor="center", width=250)
            y_offset += 40
        save_button.place(relx=0.3, y=y_offset, anchor="center")
        update_button.place(relx=0.5, y=y_offset, anchor="center")
        delete_button.place(relx=0.7, y=y_offset, anchor="center")

    def show_tooltip(event):
        """
        Display tooltip text when hovering over the info icon.
        """
        tooltip.place(x=10, y=40)

    def hide_tooltip(event):
        """
        Hide tooltip text when the mouse leaves the info icon.
        """
        tooltip.place_forget()

    # Create a new window for flight management
    window = tk.Toplevel()
    window.title("Flight Records")
    window.geometry("900x750")
    window.configure(bg="#1C1C1C")

    # Tooltip for additional information
    info_icon = tk.Label(window, text="ⓘ", font=("Helvetica", 14, "bold"), bg="#1C1C1C", fg="#3498DB")
    info_icon.place(x=10, y=10)
    info_icon.bind("<Enter>", show_tooltip)
    info_icon.bind("<Leave>", hide_tooltip)

    tooltip = tk.Label(window, text="Enter flight ID number to search or delete.\nWhen recording a new flight at the bottom of this screen,\nplease confirm the duplicate flight record with the same client ID, airline ID, and date/time does not already exist.",
                       font=("Helvetica", 10), bg="#333333", fg="white", wraplength=300)
    tooltip.place_forget()

    # Title of the application
    title_label = tk.Label(window, text="Flight Record Management", font=("Helvetica", 18, "bold"), bg="#1C1C1C", fg="white")
    title_label.place(relx=0.5, y=50, anchor="center")

    # Input fields and buttons
    flight_id_label = tk.Label(window, text="Flight ID:", font=("Helvetica", 12), bg="#1C1C1C", fg="white")
    flight_id_label.place(relx=0.4, y=120, anchor="center")
    flight_id_entry = tk.Entry(window, bg="#333333", fg="white", insertbackground="white")
    flight_id_entry.place(relx=0.6, y=120, anchor="center", width=250)

    search_button = tk.Button(window, text="Search", command=search_flight, font=("Helvetica", 12, "bold"), bg="#F39C12", fg="white", activebackground="#D35400", activeforeground="white", width=12)
    search_button.place(relx=0.5, y=160, anchor="center")

    result_text = tk.Text(window, height=10, width=70, bg="#2E2E2E", fg="white", font=("Courier", 10))
    result_text.place(relx=0.5, y=260, anchor="center")

    record_button = tk.Button(window, text="Manage Flights", command=reveal_fields, font=("Helvetica", 12, "bold"), bg="#3498DB", fg="white", activebackground="#2980B9", activeforeground="white", width=20)
    record_button.place(relx=0.5, y=430, anchor="center")

    # Input fields (hidden initially)
    client_id_label = tk.Label(window, text="Client ID:", font=("Helvetica", 12), bg="#1C1C1C", fg="white")
    client_id_entry = tk.Entry(window, bg="#333333", fg="white", insertbackground="white")

    airline_id_label = tk.Label(window, text="Airline ID:", font=("Helvetica", 12), bg="#1C1C1C", fg="white")
    airline_id_entry = tk.Entry(window, bg="#333333", fg="white", insertbackground="white")

    date_label = tk.Label(window, text="Date and Time\n(YYYY-MM-DD HH:MM):", font=("Helvetica", 12), bg="#1C1C1C", fg="white")
    date_entry = tk.Entry(window, bg="#333333", fg="white", insertbackground="white")

    start_city_label = tk.Label(window, text="Start City:", font=("Helvetica", 12), bg="#1C1C1C", fg="white")
    start_city_entry = tk.Entry(window, bg="#333333", fg="white", insertbackground="white")

    end_city_label = tk.Label(window, text="End City:", font=("Helvetica", 12), bg="#1C1C1C", fg="white")
    end_city_entry = tk.Entry(window, bg="#333333", fg="white", insertbackground="white")

    save_button = tk.Button(window, text="Save", command=save_flight, font=("Helvetica", 12, "bold"), bg="#F39C12", fg="white", activebackground="#D35400", activeforeground="white", width=12)
    update_button = tk.Button(window, text="Update", command=update_flight, font=("Helvetica", 12, "bold"), bg="#F39C12", fg="white", activebackground="#D35400", activeforeground="white", width=12)
    delete_button = tk.Button(window, text="Delete", command=delete_flight, font=("Helvetica", 12, "bold"), bg="#F39C12", fg="white", activebackground="#D35400", activeforeground="white", width=12)

    update_button.place_forget()
    delete_button.place_forget()

    # List of label-entry pairs
    field_widgets = [
        (client_id_label, client_id_entry),
        (airline_id_label, airline_id_entry),
        (date_label, date_entry),
        (start_city_label, start_city_entry),
        (end_city_label, end_city_entry),
    ]

    # Hide initially by removing from placement
    for label, entry in field_widgets:
        label.place_forget()
        entry.place_forget()

    window.mainloop()