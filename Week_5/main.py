from utils import calculate_total, print_receipt


# Get customer information

customer = input("Customer name: ")

coffee = int(input("Coffee quantity: "))

tea = int(input("Tea quantity: "))

sandwich = int(input("Sandwich quantity: "))


# Calculate bill

total = calculate_total(coffee, tea, sandwich)


# Display receipt

print_receipt(customer, coffee, tea, sandwich, total)
