class MemberManagement:

    def __init__(self):
        self.members = []

    # Add a member
    def add_member(self, member):
        self.members.append(member)

    # Find a member by ID
    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member

        return None

    # Find a member by last name
    def find_member_by_name(self, last_name):
        for member in self.members:
            if member.last_name.lower() == last_name.lower():
                return member

        return None

    # Remove a member
    def remove_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                return
    
    # Change name of a member
    def edit_member_name(self, member_id, new_last_name):
        member = self.find_member_by_id(member_id)

        if member is not None:
            member.last_name = new_last_name

    # Change email of a member
    def edit_member_email(self, member_id, new_email):
        member = self.find_member_by_id(member_id)

        if member is not None:
            member.contact.email = new_email

    # Change phone number of a member
    def edit_member_phone(self, member_id, new_phone):
        member = self.find_member_by_id(member_id)

        if member is not None:
            member.contact.phone = new_phone

    # Change city and postal code of a member
    def edit_member_location(self, member_id, new_postal_code, new_city):
        member = self.find_member_by_id(member_id)

        if member is not None:
            member.address.city = new_city
            member.address.postal_code = new_postal_code

    # Change street of a member 
    def edit_member_street(self, member_id, new_street):
        member = self.find_member_by_id(member_id)

        if member is not None:
            member.address.street = new_street

    # Sort members by last name
    def sort_members(self):
        self.members.sort(key=lambda member: member.last_name)