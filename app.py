# inventory_management.py

def display_inventory(inventory):
    """
    Displays the current inventory, showing each item and its quantity.
    """
    print("\n--- Current Inventory ---")
    if not inventory:
        print("Inventory is empty.")
        return

    for item in inventory:
        print(f"Item: {item['name']}, Quantity: {item['quantity']}")
    print("-------------------------\n")

def update_inventory(inventory):
    """
    Allows the user to add new items, update quantities of existing items,
    or remove items from the inventory.
    """
    print("\n--- Update Inventory ---")
    while True:
        print("Options:")
        print("1. Add/Update Item")
        print("2. Remove Item")
        print("3. Finish Updating")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            item_name = input("Enter item name to add/update: ").strip().capitalize()
            try:
                quantity = int(input(f"Enter quantity for {item_name}: "))
                if quantity < 0:
                    print("Quantity cannot be negative. Please enter a positive number.")
                    continue
            except ValueError:
                print("Invalid quantity. Please enter a number.")
                continue

            found = False
            # Loop through existing items to find a match
            for item in inventory:
                if item['name'] == item_name:
                    item['quantity'] += quantity
                    print(f"Updated quantity for {item_name}. New quantity: {item['quantity']}")
                    found = True
                    break
            if not found:
                # If item not found, add it as a new item
                inventory.append({'name': item_name, 'quantity': quantity})
                print(f"Added new item: {item_name} with quantity {quantity}")

        elif choice == '2':
            item_name = input("Enter item name to remove: ").strip().capitalize()
            found = False
            # Loop through inventory to find and remove the item
            for i, item in enumerate(inventory):
                if item['name'] == item_name:
                    try:
                        remove_quantity = int(input(f"Enter quantity to remove for {item_name} (enter 0 to remove all): "))
                        if remove_quantity < 0:
                            print("Quantity to remove cannot be negative.")
                            continue
                        if remove_quantity >= item['quantity'] or remove_quantity == 0:
                            del inventory[i] # Remove the entire item if quantity to remove is greater or 0
                            print(f"Removed all of {item_name} from inventory.")
                        else:
                            item['quantity'] -= remove_quantity
                            print(f"Removed {remove_quantity} of {item_name}. Remaining: {item['quantity']}")
                        found = True
                        break
                    except ValueError:
                        print("Invalid quantity. Please enter a number.")
                        continue
            if not found:
                print(f"Item '{item_name}' not found in inventory.")

        elif choice == '3':
            print("Finished updating inventory.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    print("-------------------------\n")


def main():
    """
    Main function to run the inventory management system.
    Initializes inventory with example items and provides a menu.
    """
    # Example inventory items
    inventory = [
        {'name': 'Laptop', 'quantity': 10},
        {'name': 'Mouse', 'quantity': 50},
        {'name': 'Keyboard', 'quantity': 30},
        {'name': 'Monitor', 'quantity': 15}
    ]

    while True:
        print("--- Inventory Management System ---")
        print("1. Display Inventory")
        print("2. Update Inventory")
        print("3. Exit")

        main_choice = input("Enter your choice (1/2/3): ").strip()

        if main_choice == '1':
            display_inventory(inventory)
        elif main_choice == '2':
            update_inventory(inventory)
        elif main_choice == '3':
            print("Exiting Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
