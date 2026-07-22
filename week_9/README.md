# IT Helpdesk Ticket Registration System

## Project Description

This Python program allows users to register an IT Helpdesk ticket by entering student details and selecting a priority level. The system automatically assigns a technician based on the selected priority and displays the completed ticket.

## Files

- `main.py` – Runs the program.
- `ticket.py` – Collects user input.
- `display.py` – Displays the ticket and assigns a technician.
- `README.md` – Project documentation.

## Requirements

- Python 3.x

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run:

```bash
python main.py
```

## Example Output

```
=== IT Helpdesk Ticket ===

Enter student name: Nikita
Enter student ID: 123456
Enter issue: WiFi not working
Enter location: Lab 101

Priority Level
1. High
2. Medium
3. Low
Choose priority (1-3): 1

========== HELPDESK TICKET ==========
Student Name : Nikita
Student ID   : 123456
Issue        : WiFi not working
Location     : Lab 101
Priority     : High
Technician   : Ahmad
Status       : Pending
====================================
```
