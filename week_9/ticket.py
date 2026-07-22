def create_ticket():

    print("=== IT Helpdesk Ticket ===")

    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    issue = input("Enter issue: ")
    location = input("Enter location: ")

    print("\nPriority Level")
    print("1. High")
    print("2. Medium")
    print("3. Low")

    choice = input("Choose priority (1-3): ")

    if choice == "1":
        priority = "High"
    elif choice == "2":
        priority = "Medium"
    else:
        priority = "Low"

    return name, student_id, issue, location, priority
