# Week 2 Tutorial 2

## Scenario

A person is allowed to enter the movie theater if:
- The person is 13 years old or older OR is accompanied by an adult.
- The person must have a valid ticket.

## Conditions

Age Condition:
- Age ≥ 13

Adult Condition:
- Accompanied by an adult

Ticket Condition:
- Has a valid ticket

## Logical Expression

(age >= 13 OR accompanied by an adult) AND has a valid ticket

## Examples

1. Age: 15, Valid Ticket: Yes
   Result: Allowed

2. Age: 10, Accompanied by Adult: Yes, Valid Ticket: Yes
   Result: Allowed

3. Age: 10, Accompanied by Adult: No, Valid Ticket: Yes
   Result: Not Allowed

4. Age: 18, Valid Ticket: No
   Result: Not Allowed
