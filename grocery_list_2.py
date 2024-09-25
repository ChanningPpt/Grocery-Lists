grocery_list = []

while True:
    item = input("Enter the name of the item you would like to add (alphabetical characters only): ")
    if item.isalpha() == False:
        print("Invalid input. Please enter alphabetical characters only.")
        continue

    quantity = input(f"Enter the quantity of {item} (numbers only): ")
    if quantity.isdigit() == False:
        print("Invalid input. Please enter valid numbers only.")
        continue

    grocery_list.append([item, int(quantity)])

    continue_choice = input("Would you like to add more items? (yes/no): ").lower()
    if continue_choice != 'yes':
        break

print("\nYour Final Grocery List:")
for item, quantity in grocery_list:
    print(f"{item}: {quantity}")