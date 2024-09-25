def validate_item():
    while True:
        item = input("Enter the name of the item you would like to add (alphabetical characters only): ")
        if item.isalpha():
            return item
        else:
            print("Invalid input. Please enter alphabetical characters only.")

def validate_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity (whole numbers only (e.g. 1, 5)): "))
            return quantity
        except ValueError:
            print("Invalid input. Please enter valid numbers only.")

def validate_price():
    while True:
        try:
            price = float(input("Enter the price per item (numbers only with decimal point (e.g. 1.00, 2.50)): "))
            return price
        except ValueError:
            print("Invalid input. Please enter valid numbers only. (e.g. 1.00)")

def create_grocery_list():
    def print_grocery_list(grocery_list):
        total_cost = 0

        print("\nYour Final Grocery List:")
        print("------------------------")

        for item, quantity, price in grocery_list:
            item_cost = quantity * price
            total_cost += item_cost
            print(f"{item}: Quantity: {quantity}, Price per item: ${price:.2f}, Total item cost: ${item_cost:.2f}")
        
        print(f"\nTotal price of grocery list: ${total_cost:.2f}")
    
    grocery_list = []

    while True:
        item =  validate_item()
        quantity = validate_quantity()
        price = validate_price()

        grocery_list.append([item, quantity, price])

        continue_choice = input("Would you like to add more items? (yes/no): ").lower()
        if continue_choice != 'yes':
            print_grocery_list(grocery_list)
            break

if __name__ == "__main__":
    create_grocery_list()