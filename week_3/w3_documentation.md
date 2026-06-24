# Week 3 Documentation

## Inputs

- Quiz 1 mark
- Quiz 2 mark
- Quiz 3 mark
- Continue choice (Y/N)

- ## Process

1. Enter three quiz marks.
2. Calculate the average mark.
3. Display the average.
4. Determine whether the student passes or fails.
5. Ask the user whether to continue.

6. ## Outputs

- Average mark
- Pass message
- Fail message
- Program Ended

- ## Pseudocode

START

Set choice = "y"

WHILE choice == "y"

    Input quiz 1 mark
    Input quiz 2 mark
    Input quiz 3 mark

    Calculate average

    Display average

    IF average >= 50
        Display "Pass"
    ELSE
        Display "Fail"

    Ask user if they want to continue

END WHILE

Display "Program Ended"

STOP

## Algorithm Structure

### Sequence

- Input quiz marks
- Calculate average
- Display average

### Selection

IF average >= 50
    Pass
ELSE
    Fail

### Iteration

WHILE choice == "y"
