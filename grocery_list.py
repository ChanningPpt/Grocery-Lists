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
            quantity = int(input("Enter the quantity (numbers only): "))
            return quantity
        except ValueError:
            print("Invalid input. Please enter valid numbers only.")

grocery_list = []

while True:
    item = validate_item()
    quantity = validate_quantity()

    grocery_list.append([item, quantity])

    continue_choice = input("Would you like to add more items? (yes/no): ").lower()
    if continue_choice != 'yes':
        print("\nYour Final Grocery List:")
        print("------------------------")
        for item, quantity in grocery_list:
            print(f"{item}: {quantity}")
        break