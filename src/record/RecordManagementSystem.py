import json
import os
from datetime import datetime


class RecordManagementSystem:
    def __init__(self):
        self.client_records = []
        self.airline_records = []
        self.flight_records = []

        self.load_data()

    # Load data from files
    def load_data(self):
        if os.path.exists('client_records.json'):
            with open('client_records.json', 'r') as f:
                self.client_records = json.load(f)

        if os.path.exists('airline_records.json'):
            with open('airline_records.json', 'r') as f:
                self.airline_records = json.load(f)

        if os.path.exists('flight_records.json'):
            with open('flight_records.json', 'r') as f:
                self.flight_records = json.load(f)

    # Save data to files
    def save_data(self):
        with open('client_records.json', 'w') as f:
            json.dump(self.client_records, f, indent=4)

        with open('airline_records.json', 'w') as f:
            json.dump(self.airline_records, f, indent=4)

        with open('flight_records.json', 'w') as f:
            json.dump(self.flight_records, f, indent=4)

    # Create client record
    def create_client_record(self):
        client_id = len(self.client_records) + 1
        name = input("Enter client's name: ")
        address1 = input("Enter address line 1: ")
        address2 = input("Enter address line 2: ")
        address3 = input("Enter address line 3: ")
        city = input("Enter city: ")
        state = input("Enter state: ")
        zip_code = input("Enter zip code: ")
        country = input("Enter country: ")
        phone = input("Enter phone number: ")

        new_client = {
            "ID": client_id,
            "Type": "Client",
            "Name": name,
            "Address Line 1": address1,
            "Address Line 2": address2,
            "Address Line 3": address3,
            "City": city,
            "State": state,
            "Zip Code": zip_code,
            "Country": country,
            "Phone Number": phone
        }

        self.client_records.append(new_client)
        print("Client record created successfully.")

    # Create airline record
    def create_airline_record(self):
        airline_id = len(self.airline_records) + 1
        company_name = input("Enter airline company name: ")

        new_airline = {
            "ID": airline_id,
            "Type": "Airline",
            "Company Name": company_name
        }

        self.airline_records.append(new_airline)
        print("Airline record created successfully.")

    # Create flight record
    def create_flight_record(self):
        client_id = int(input("Enter Client ID for flight record: "))
        airline_id = int(input("Enter Airline ID for flight record: "))
        date = input("Enter flight date (YYYY-MM-DD HH:MM): ")
        start_city = input("Enter start city: ")
        end_city = input("Enter end city: ")

        flight_date = datetime.strptime(date, "%Y-%m-%d %H:%M")

        new_flight = {
            "Client_ID": client_id,
            "Airline_ID": airline_id,
            "Date": flight_date,
            "Start City": start_city,
            "End City": end_city
        }

        self.flight_records.append(new_flight)
        print("Flight record created successfully.")

    # Delete a client record
    def delete_client_record(self):
        client_id = int(input("Enter Client ID to delete: "))
        self.client_records = [client for client in self.client_records if client["ID"] != client_id]
        print("Client record deleted successfully.")

    # Delete an airline record
    def delete_airline_record(self):
        airline_id = int(input("Enter Airline ID to delete: "))
        self.airline_records = [airline for airline in self.airline_records if airline["ID"] != airline_id]
        print("Airline record deleted successfully.")

    # Delete a flight record
    def delete_flight_record(self):
        flight_id = int(input("Enter Flight ID to delete: "))
        self.flight_records = [flight for flight in self.flight_records if flight["Client_ID"] != flight_id]
        print("Flight record deleted successfully.")

    # Search and display client record
    def search_client_record(self):
        client_id = int(input("Enter Client ID to search: "))
        for client in self.client_records:
            if client["ID"] == client_id:
                print(client)

    # Search and display airline record
    def search_airline_record(self):
        airline_id = int(input("Enter Airline ID to search: "))
        for airline in self.airline_records:
            if airline["ID"] == airline_id:
                print(airline)

    # Search and display flight record
    def search_flight_record(self):
        client_id = int(input("Enter Client ID to search: "))
        for flight in self.flight_records:
            if flight["Client_ID"] == client_id:
                print(flight)

    # Main menu
    def main_menu(self):
        while True:
            print("\n--- Record Management System ---")
            print("1. Create Client Record")
            print("2. Create Airline Record")
            print("3. Create Flight Record")
            print("4. Delete Client Record")
            print("5. Delete Airline Record")
            print("6. Delete Flight Record")
            print("7. Search Client Record")
            print("8. Search Airline Record")
            print("9. Search Flight Record")
            print("10. Exit")
            
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_client_record()
            elif choice == '2':
                self.create_airline_record()
            elif choice == '3':
                self.create_flight_record()
            elif choice == '4':
                self.delete_client_record()
            elif choice == '5':
                self.delete_airline_record()
            elif choice == '6':
                self.delete_flight_record()
            elif choice == '7':
                self.search_client_record()
            elif choice == '8':
                self.search_airline_record()
            elif choice == '9':
                self.search_flight_record()
            elif choice == '10':
                self.save_data()
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again.")


# Run the system
if __name__ == "__main__":
    system = RecordManagementSystem()
    system.main_menu()
