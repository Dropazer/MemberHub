from datetime import date
from address import Address
from contact import Contact
from member import Member


class Cli:

    def __init__(self, member_management, persistence):
        # Store references to member management and persistence
        self.member_management = member_management
        self.persistence = persistence

    def menu_print(self):
        # Display the main menu and return the user's input
        print()
        print("===== MemberHub =====")
        print()
        print("1. Show members")
        print("2. Add member")
        print("3. Search member")
        print("4. Edit member")
        print("5. Delete member")
        print("6. Sort members")
        print("7. Exit program")
        print()

        user_input = input("Please select an option: ")
        print()

        return user_input

    def start(self):
        # Repeat the menu until the user exits the program
        while True:
            choice = self.menu_print()

            if choice == "1":
                # Display all members
                print("Displaying members:")

                for member in self.member_management.members:
                    print(
                        f"{member.member_id}: "
                        f"{member.first_name} {member.last_name}"
                    )

            elif choice == "2":
                # Collect information for a new member
                print("===== Add new member =====")

                last_name = input("Last name: ")

                # Reject invalid names and return to the menu
                if not last_name.isalpha():
                    print("Please enter a valid last name.")
                    continue

                first_name = input("First name: ")

                if not first_name.isalpha():
                    print("Please enter a valid first name.")
                    continue

                birth_date = input("Date of birth (YYYY-MM-DD): ")

                # Convert input to a date and handle invalid values
                try:
                    birth_date = date.fromisoformat(birth_date)
                except ValueError:
                    print("Please enter a valid date of birth.")
                    continue

                street = input("Street: ")
                postal_code = input("Postal code: ")
                city = input("City: ")
                email = input("Email address: ")
                phone = input("Phone number: ")

                # Create address and contact objects
                address = Address(street, postal_code, city)
                contact = Contact(email, phone)

                # Create a member with the entered information
                member = Member(
                    last_name,
                    first_name,
                    birth_date,
                    address,
                    contact
                )

                # Add the member and save the updated list
                self.member_management.add_member(member)

                self.persistence.save_members(
                    self.member_management.members
                )

                print("Member added successfully.")

            elif choice == "3":
                # Search for a member by last name
                last_name = input("Enter last name: ")

                member = self.member_management.find_member_by_name(last_name)

                if member is None:
                    print("No member found with this last name.")
                else:
                    print(
                        f"{member.member_id}: "
                        f"{member.first_name} {member.last_name}"
                    )

            elif choice == "4":
                
                # Read and validate the member ID
                try:
                    member_id = int(input("Member ID: "))
                except ValueError:
                    print("Please enter a valid member ID.")
                    continue

                # Check whether the member exists
                member = self.member_management.find_member_by_id(member_id)

                if member is None:
                    print("Member not found.")
                else:
                    print(f"Current member: {member.first_name} {member.last_name}")
                    
                    new_last_name = input("New last name: ")

                    if not new_last_name.isalpha():
                        print("The last name must contain only letters.")
                        continue

                    # Update the last name and save the changes
                    self.member_management.edit_member(
                        member_id, new_last_name
                    )

                    self.persistence.save_members(
                        self.member_management.members
                    )

                    print("Member updated successfully.")

            elif choice == "5":
                # Read and validate the member ID
                try:
                    member_id = int(input("Member ID: "))
                except ValueError:
                    print("Please enter a valid member ID.")
                    continue

                # Find the member before deleting it
                member = self.member_management.find_member_by_id(member_id)

                if member is None:
                    print("Member not found.")
                else:
                    # Remove the member and save the updated list
                    self.member_management.remove_member(member_id)

                    self.persistence.save_members(
                        self.member_management.members
                    )

                    print(f"Member {member.first_name} {member.last_name} deleted.")

            elif choice == "6":
                # Sort members alphabetically by last name
                self.member_management.sort_members()

                # Display the sorted list
                for member in self.member_management.members:
                    print(
                        f"{member.member_id}: "
                        f"{member.last_name} {member.first_name}"
                    )

            elif choice == "7":
                # Exit the menu loop
                print("Exiting program.")
                break

            else:
                # Handle invalid menu selections
                print("Invalid selection.")

            print()