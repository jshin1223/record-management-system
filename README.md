# Record Management System

The Record Management System is a Python-based desktop application designed for a specialist travel agency to manage three types of records:
1. **Client Records**
2. **Airline Records**
3. **Flight Records**

The system comes with an easy-to-use Graphical User Interface (GUI) to add, modify, search and remove records.

---

## Features

- **Client Records**:
  - Specify and input the name of the client, the address and telephone number of the client.
  - One of the operations anybody can perform is to look for the client records using the ID.

- **Airline Records**:
  - Airline details should also be added as well inclusive of a code and the name of the air company.
  - Airline records search by identification number.

- **Flight Records**:
  - Append flight details to this table, of course such as client ID, airline ID, date, start city and end city.
  - Document file search by Flight ID.

- **Persistent Storage**:
  - Information is stored in JSON for archival purposes in files.
  - Whenever the application is started, it automatically populates records which already exist.

---

## Requirements

This program requires Python 3.8 or higher and the following dependencies:

**tkinter** included in Python installation
**json** – A standard Python library that doesn’t require installation.

---

## Installation

1. **Clone the Repository**:

   git clone <repository_url>
   cd <repository_directory>

2. Ensure data Directory Exists: Make sure that in the src/ folder there is a data/ directory. If not, create it:

mkdir src/data

3. Create JSON Files: Copy the required JSON files with empty content filled out as an array ([]) as their content.

echo "[]" > src/data/clients.json
echo "[]" > src/data/airlines.json
echo "[]" > src/data/flights.json

4. Run the Program: Go to the src/ directory and type:

python main.py

---

## Acknowledgements

* Created for the Software Development in Practice module at University of Liverpool.
* Developed according to the project requirements for properly managing records with a GUI.