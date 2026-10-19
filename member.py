class Member:

    last_member_id = 0

    def __init__(self, last_name, first_name, birth_date, address, contact, member_id=None):

        if member_id is None:
            Member.last_member_id += 1
            self.member_id = Member.last_member_id

        else:
            self.member_id = member_id

            if member_id > Member.last_member_id:
                Member.last_member_id = member_id

        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.address = address
        self.contact = contact

    def change_last_name(self, new_last_name):
        if not new_last_name.isalpha():
            raise ValueError("The last name must contain only letters.")

        self.last_name = new_last_name