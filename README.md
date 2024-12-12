# Record Management System

### Table of Contents
1. [Project Description](#project-description)
2. [Installation](#installation)
3. [Execution and Usage](#execution-and-usage)
4. [Technologies Used](#technologies-used)
5. [Current Features](#current-features)
6. [Contributors](#contributors)
7. [License](#license)

---
### Project description

The Record Management System is a Python-based desktop application designed for a specialist travel agency to manage three types of records:
1. **Client Records**
2. **Airline Records**
3. **Flight Records**

The system comes with an easy-to-use Graphical User Interface (GUI) to add, modify, search and remove records.

---
### Installation

Ensure you have **Python 3.8 or higher** installed on your system. If Python is not installed, download and install it from the [official Python website](https://www.python.org/).

No additional installation commands or dependencies are neeeded to run the program, as required libraries (Tkinter and JSON) are included with the Python standard library.

---
### Execution and Usage

In Terminal

1. **Clone the Repository**:  
   ```bash
   git clone <repository_url>
   cd <repository_directory>

2. **Run the Program**: Navigate to the src/ directory and execute the program:
    ```bash
    python main.py

---
### Technologies Used

**Python 3.8 or higher** was used with the following dependencies:

**Tkinter**: Included in Python installation.  
**JSON**: A standard data format that doesn’t require installation.

---
### Current Features
The Record Management System provides the following capabilities:

- **Client Records**:
  - Add and Save a new client information by inputting the client name, address, and telephone number.
  - Update a client information with the corrected client name, address, and telephone number. 
  - Search the client records by the Client ID.

- **Airline Records**:
  - Add new airline information by entering the airline company name.
  - Search Airline records by Airline ID.

- **Flight Records**:
  - Add new flight information by providing Client ID, Airline ID, Date/Time, Start City, and End City.
  - Update a flight record with the correct Client ID, Airline ID, Date/Time, Start City, and End City.
  - Search for flight records by entering Flight ID.

- **Persistent Storage**:
  - All data is saved in JSON files within the `data` folder.
  - Existing records are automatically loaded when the application starts.

- **Unit Tests**
  - There are three unit test files that check functions in client, airline, and flight records. 

---
### Contributors

Thomas Mortimer, Hilya Ligamena Nahole, Nishant Shrivastava, Sung Shin

---
### License
This project is licensed under the MIT License.

Copyright (c) 2024 Thomas Mortimer, Hilya Ligamena Nahole, Nishant Shrivastava, Sung Shin

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE F---OR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.