from cli import Cli
from persistence import Persistence
from member_management import MemberManagement


def main():
    # Create persistence and member management objects
    persistence = Persistence()
    member_management = MemberManagement()

    # Load saved members when the program starts
    member_management.members = persistence.load_members()

    # Create and start the CLI
    cli = Cli(member_management, persistence)
    cli.start()


# Run the program only when this file is executed directly
if __name__ == "__main__":
    main()