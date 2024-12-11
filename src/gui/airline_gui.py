import tkinter as tk
from tkinter import messagebox
from record.airline import AirlineRecord


def manage_airline_gui():
    def save_airline():
        """
        Save a new airline record.
        """
        try:
            airline_data = {
                "ID": AirlineRecord.generate_id(),
                "Company Name": company_name_entry.get().strip(),
            }
            AirlineRecord.create(airline_data)
            messagebox.showinfo("Success", "Airline record created!")
            clear_inputs()
        except Exception as e:
            messagebox.showerror("Error", str(e))

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

    def update_airline():
        """
        Update an existing airline record by ID.
        """
        try:
            airline_id = int(airline_id_entry.get().strip())
            new_name = company_name_entry.get().strip()
            if not new_name:
                messagebox.showerror("Error", "Company Name cannot be empty. Please provide a name.")
                return

            if AirlineRecord.update_airline(airline_id, {"Company Name": new_name}):
                messagebox.showinfo("Success", "Airline record updated successfully!")
            else:
                messagebox.showwarning("Not Found", "No airline found with the given ID.")
        except ValueError:
            messagebox.showerror("Error", "Invalid ID. Please enter a numeric value.")

    def search_airline():
        """
        Search for an airline by ID.
        """
        try:
            airline_id = int(search_entry.get().strip())
            result = AirlineRecord.search(airline_id)
            result_text.delete(1.0, tk.END)
            if result:
                result_text.insert(tk.END, f"Airline Found:\n")
                for key, value in result.items():
                    result_text.insert(tk.END, f"{key}: {value}\n")
            else:
                messagebox.showwarning("Not Found", "No airline found with the given ID.")
        except ValueError:
            messagebox.showerror("Error", "Invalid ID. Please enter a numeric value.")

    def clear_inputs():
        """
        Clear all input fields.
        """
        for entry in [airline_id_entry, company_name_entry]:
            entry.delete(0, tk.END)

    def reveal_fields():
        """
        Reveal input fields for managing airline records.
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
        Hide tooltip text when mouse leaves the info icon.
        """
        tooltip.place_forget()

    # Create a new window
    window = tk.Toplevel()
    window.title("Airline Records")
    window.geometry("900x750")
    window.configure(bg="#1C1C1C")

    # Tooltip at Top-Left
    info_icon = tk.Label(window, text="ⓘ", font=("Helvetica", 14, "bold"), bg="#1C1C1C", fg="#3498DB")
    info_icon.place(x=10, y=10)
    info_icon.bind("<Enter>", show_tooltip)
    info_icon.bind("<Leave>", hide_tooltip)

    tooltip = tk.Label(
        window,
        text="Enter airline ID number to search or delete.\nWhen recording a new airline at the bottom of this screen,\nplease confirm the airline name does not already exist.",
        font=("Helvetica", 10),
        bg="#333333",
        fg="white",
        wraplength=300
    )
    tooltip.place_forget()

    # Title
    title_label = tk.Label(window, text="Airline Record Management", font=("Helvetica", 18, "bold"), bg="#1C1C1C", fg="white")
    title_label.place(relx=0.5, y=50, anchor="center")

    # Search Airline by Name
    search_label = tk.Label(window, text="Airline ID:", font=("Helvetica", 12), bg="#1C1C1C", fg="white")
    search_label.place(relx=0.4, y=120, anchor="center")
    search_entry = tk.Entry(window, bg="#333333", fg="white", insertbackground="white")
    search_entry.place(relx=0.6, y=120, anchor="center", width=270)

    search_button = tk.Button(window, text="Search", command=search_airline, font=("Helvetica", 12, "bold"), bg="#F39C12", fg="white", activebackground="#D35400", activeforeground="white", width=12)
    search_button.place(relx=0.5, y=160, anchor="center")

    # Result display
    result_text = tk.Text(window, height=10, width=70, bg="#2E2E2E", fg="white", font=("Courier", 10))
    result_text.place(relx=0.5, y=260, anchor="center")

    # Button to reveal new airline fields
    record_button = tk.Button(window, text="Manage Airlines", command=reveal_fields, font=("Helvetica", 12, "bold"), bg="#3498DB", fg="white", activebackground="#2980B9", activeforeground="white", width=20)
    record_button.place(relx=0.5, y=430, anchor="center")

    # Input fields (hidden initially)
    airline_id_label = tk.Label(window, text="Airline ID:", font=("Helvetica", 12), bg="#1C1C1C", fg="white")
    airline_id_entry = tk.Entry(window, bg="#333333", fg="white", insertbackground="white")

    company_name_label = tk.Label(window, text="Company Name:", font=("Helvetica", 12), bg="#1C1C1C", fg="white")
    company_name_entry = tk.Entry(window, bg="#333333", fg="white", insertbackground="white")

    save_button = tk.Button(window, text="Save", command=save_airline, font=("Helvetica", 12, "bold"), bg="#F39C12", fg="white", activebackground="#D35400", activeforeground="white", width=12)
    update_button = tk.Button(window, text="Update", command=update_airline, font=("Helvetica", 12, "bold"), bg="#F39C12", fg="white", activebackground="#218838", activeforeground="white", width=12)
    delete_button = tk.Button(window, text="Delete", command=delete_airline, font=("Helvetica", 12, "bold"), bg="#F39C12", fg="white", activebackground="#C0392B", activeforeground="white", width=12)

    # save_button.config(state="disabled")
    update_button.place_forget()
    delete_button.place_forget()

    field_widgets = [
        (airline_id_label, airline_id_entry),
        (company_name_label, company_name_entry),
    ]

    # Hide initially by removing from placement
    for label, entry in field_widgets:
        label.place_forget()
        entry.place_forget()

    window.mainloop()
