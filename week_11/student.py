def get_student():

    print("===== Computer Lab Access =====")

    name = input("Student Name : ")
    student_id = input("Student ID : ")
    registered = input("Registered for today's lab? (Yes/No): ").upper()
    lab_open = input("Is the lab open? (Yes/No): ").upper()
    computer_available = input("Computer Available? (Yes/No): ").upper()

    return name, student_id, registered, lab_open, computer_available
