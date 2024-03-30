
from utils import create, retrieve, update, delete

def main():
    while True:
        print("\nChoose an action:")
        print("1. Create a district")
        print("2. Retrieve a district by ID")
        print("3. Update a district name by ID")
        print("4. Delete a district by ID")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the district name: ")
            create({'name': name})
            print("District added successfully.")
        elif choice == '2':
            id = int(input("Enter the district ID: "))
            district = retrieve(id)
            if district:
                print(f"District details: {district}")
            else:
                print(f"District with ID {id} not found.")
        elif choice == '3':
            id = int(input("Enter the district ID: "))
            name = input("Enter the new district name: ")
            update(id, name)
            print("District updated successfully.")
        elif choice == '4':
            id = int(input("Enter the district ID: "))
            delete(id)
            print("District deleted successfully.")
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
