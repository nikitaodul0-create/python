from ticket import create_ticket
from display import display_ticket


def main():

    # Create a new ticket
    name, student_id, issue, location, priority = create_ticket()

    # Display the completed ticket
    display_ticket(
        name,
        student_id,
        issue,
        location,
        priority
    )


if __name__ == "__main__":
    main()
