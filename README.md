### Project description

<h3 style="font-size: 16px;">Record Management System</h3>

The Record Management System is a Python-based desktop application designed for a specialist travel agency to manage three types of records:
1. **Client Records**
2. **Airline Records**
3. **Flight Records**

The system comes with an easy-to-use Graphical User Interface (GUI) to add, modify, search and remove records.
<hr style="height:1px; border:none; background-color:#ccc;">

### Installation

No additional installation commands or dependencies are neeeded to run the program. 
<hr style="height:1px; border:none; background-color:#ccc;">

### Execution and Usage

In Terminal

1. **Clone the Repository**:  
   > git clone <repository_url>  
   > cd <repository_directory>

2. **Run the Program**: 
   Go to the src/ directory and type the executable filename to execute.  
   
   > **src> python main.py**
<hr style="height:1px; border:none; background-color:#ccc;">

### Used Technologies

This program requires Python 3.8 or higher and the following dependencies:

**Tkinter**: Included in Python installation.  
**JSON**: A standard data format that doesn’t require installation.
<hr style="height:1px; border:none; background-color:#ccc;">

### Current Features

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
<hr style="height:1px; border:none; background-color:#ccc;">

### Contributors

Thomas Mortimer, Hilya Ligamena Nahole, Nishant Shrivastava, Sung Shin
<hr style="height:1px; border:none; background-color:#ccc;">

### Released under MIT License

Copyright (c) 2024 Thomas Mortimer, Hilya Ligamena Nahole, Nishant Shrivastava, Sung Shin

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.