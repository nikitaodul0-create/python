def check_access(registered, lab_open, computer_available):

    if registered == "YES" and lab_open == "YES" and computer_available == "YES":
        return "Access Granted"
    
    return "Access Denied"


def get_reason(registered, lab_open, computer_available):

    if registered == "NO":
        return "Student is not registered"

    elif lab_open == "NO":
        return "Computer lab is closed"

    elif computer_available == "NO":
        return "No available computer"

    return ""
