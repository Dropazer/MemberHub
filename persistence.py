import json
from datetime import date
from address import Address
from contact import Contact
from member import Member


class Persistence:

    # Convert member objects into dictionaries and save them as JSON
    def save_members(self, members):

        members_list = []

        for member in members:

            member_data = {
                "member_id": member.member_id,
                "last_name": member.last_name,
                "first_name": member.first_name,
                "birth_date": str(member.birth_date),
                "address": {
                    "street": member.address.street,
                    "postal_code": member.address.postal_code,
                    "city": member.address.city
                },
                "contact": {
                    "email": member.contact.email,
                    "phone": member.contact.phone
                }
            }

            members_list.append(member_data)

        with open("Persistence/members.json", "w", encoding="utf-8") as file:
            json.dump(members_list, file, indent=4, ensure_ascii=False, sort_keys=True)

    # Load JSON data and create member objects
    def load_members(self):

        try:
            with open("Persistence/members.json", "r", encoding="utf-8") as file:
                members_data = json.load(file)

        except FileNotFoundError:
            return []

        members = []

        for member_data in members_data:

            address = Address(
                member_data["address"]["street"],
                member_data["address"]["postal_code"],
                member_data["address"]["city"]
            )

            contact = Contact(
                member_data["contact"]["email"],
                member_data["contact"]["phone"]
            )

            birth_date = date.fromisoformat(
                member_data["birth_date"]
            )

            member = Member(
                member_data["last_name"],
                member_data["first_name"],
                birth_date,
                address,
                contact,
                member_id=member_data["member_id"]
            )

            members.append(member)

        return members