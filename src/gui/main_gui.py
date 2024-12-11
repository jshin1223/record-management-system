"""
This module builds the first part of the graphical user interface (GUI) for the Record Management System.

It provides a menu to navigate between:
- Client Records
- Airline Records
- Flight Records
"""

import tkinter as tk
from tkinter import ttk
from gui.client_gui import manage_client_gui
from gui.airline_gui import manage_airline_gui
from gui.flight_gui import manage_flight_gui


def create_button_with_shadow(canvas, x, y, text, command):
    """
    Create a button with a shadow effect on the canvas.

    Args:
        canvas (tk.Canvas): Canvas to draw the button on.
        x, y (int): Center coordinates for the button.
        text (str): Button text.
        command (function): Function to execute on button click.
    """
    shadow_offset = 3

    # Create shadow rectangle
    shadow = canvas.create_rectangle(
        x - 150 + shadow_offset, y - 25 + shadow_offset,
        x + 150 + shadow_offset, y + 25 + shadow_offset,
        fill="#2E2E2E", outline=""
    )

    # Create main button rectangle
    button = canvas.create_rectangle(
        x - 150, y - 25, x + 150, y + 25,
        fill="#F39C12", outline="#E67E22", width=2
    )

    # Add text
    text_id = canvas.create_text(
        x, y, text=text, font=("Helvetica", 16, "bold"),
        fill="white"
    )

    # Bind click event
    for element in [button, text_id]:
        canvas.tag_bind(element, "<Button-1>", lambda event: command())


def create_gui():
    """
    Opens the main GUI of the Record Management System.
    """
    # Create the main application window
    root = tk.Tk()
    root.title("Record Management System")
    root.geometry("800x600")
    root.configure(bg="#1C1C1C")

    # Create a canvas for shadows and buttons
    canvas = tk.Canvas(root, width=800, height=600, bg="#1C1C1C", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # Title Label with Shadow
    canvas.create_text(
        402, 102, text="Record Management System",
        font=("Helvetica", 28, "bold"),
        fill="#2E2E2E"  # Shadow color
    )
    canvas.create_text(
        400, 100, text="Record Management System",
        font=("Helvetica", 28, "bold"),
        fill="#F7CA18"
    )

    # Buttons with Shadows
    create_button_with_shadow(canvas, 400, 200, "Client Records", manage_client_gui)
    create_button_with_shadow(canvas, 400, 300, "Airline Records", manage_airline_gui)
    create_button_with_shadow(canvas, 400, 400, "Flight Records", manage_flight_gui)

    # Footer with Shadow
    canvas.create_text(
        402, 552, text="© 2024 Airline Record Management System",
        font=("Helvetica", 10),
        fill="#2E2E2E"
    )
    canvas.create_text(
        400, 550, text="© 2024 Airline Record Management System",
        font=("Helvetica", 10),
        fill="#BDC3C7"
    )

    # Start the main event loop for the application
    root.mainloop()


# Run the GUI if the script is executed directly
if __name__ == "__main__":
    create_gui()
