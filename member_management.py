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

    # Remove a member
    def remove_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                return

    # Change a member's last name
    def edit_member(self, member_id, new_last_name):
        member = self.find_member_by_id(member_id)

        if member is not None:
            member.last_name = new_last_name

    # Sort members by last name
    def sort_members(self):
        self.members.sort(key=lambda member: member.last_name)

    # Find a member by last name
    def find_member_by_name(self, last_name):
        for member in self.members:
            if member.last_name.lower() == last_name.lower():
                return member

        return None