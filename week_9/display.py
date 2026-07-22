def display_ticket(name, student_id, issue, location, priority):

    if priority == "High":
        technician = "Ahmad"
    elif priority == "Medium":
        technician = "Siti"
    else:
        technician = "Ali"

    print("\n========== HELPDESK TICKET ==========")
    print(f"Student Name : {name}")
    print(f"Student ID   : {student_id}")
    print(f"Issue        : {issue}")
    print(f"Location     : {location}")
    print(f"Priority     : {priority}")
    print(f"Technician   : {technician}")
    print("Status       : Pending")
    print("====================================")
