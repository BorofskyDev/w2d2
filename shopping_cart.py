from IPython.display import clear_output


def store_input():
    print("""Type 'shop' to begin shopping.
    Type 'cart' to view your cart. 
    Type 'delete' to delete an item.
    Type 'quit' to quit""")


def cart():
    input("Welcome to the Shopping Center. Press any key to continue. ")

    products = []
    done = False
    shopping_cart = []

    while not done:
        clear_output()

        store_input()

        choice = input("What is your choice? shop | delete | cart | quit: ").lower()
        if choice == "shop":
            confirm = "Y"
            while confirm == "Y":
                item = input("Type in the item you want (or type 'return' to go back): ").title()
                shopping_cart.append(item)
                confirm = input("Type 'Y' to add another product or type 'N' to return to the main menu: ").upper()
                if confirm == "Y":
                    pass
                elif confirm == "N":
                    pass
                else:
                    print("This is not a valid selection. Please enter 'Y' or 'N'")
        elif choice == "delete":
            confirm = "Y"
            while confirm == "Y":
                print(shopping_cart)
                item=input("What would you like to delete? ").title()
                confirm=input("Please confirm you want to delete " + item + ". Type 'Y' to confirm or 'N' to decline: ").upper
                if confirm == "Y":
                    if item not in shopping_cart:
                        print("This is not a valid item in your cart.")
                    else:
                        shopping_cart.remove(item)
                        print(item + " has been removed.")
                elif confirm == "N":
                    print(item + " has NOT been removed.")
                else: 
                    print("That is not a valid selection.")
                    confirm="N"

        elif choice == "cart":
            print(shopping_cart)
        elif choice == "quit":
            confirm = input("Are you sure you want to quit? Y/N: ").lower()
            if confirm == "y":
                print("Thank you, here is your cart")
                print(shopping_cart)
                done = True
            elif confirm == "n":
                continue
        else:
            print("That is not a valid entry. Please try again.")
            continue


cart()
