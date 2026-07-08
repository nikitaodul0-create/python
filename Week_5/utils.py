# Function to calculate total bill

def calculate_total(coffee, tea, sandwich):

    coffee_price = 8.50
    tea_price = 6.00
    sandwich_price = 12.00

    total = (coffee * coffee_price) + (tea * tea_price) + (sandwich * sandwich_price)

    return total



# Function to print receipt

def print_receipt(customer, coffee, tea, sandwich, total):

    print("\n===== RECEIPT =====")
    print("Customer :", customer)
    print("Coffee   :", coffee)
    print("Tea      :", tea)
    print("Sandwich :", sandwich)
    print("-------------------")
    print("Total = RM", total)
