from IPython.display import clear_output
def store_input():
    print("""Type 'shop' to begin shopping.
    Type 'cart' to view your cart. 
    Type 'quit' to quit""")

def cart():
    input("Welcome to the Shopping Center. Press any key to continue. ")

    products = []
    done = False

    while not done:
        clear_output()
        
        store_input()

        choice = input("What is your choice? shop | cart | quit: ").lower()
        if choice == "shop":
            back= False
            while not back:     
                item = input("Type in the item you want (or type 'return' to go back): ").lower()
                if item == "return":
                    back = True
                else:
                    continue

            shopping_cart = {
            "item" : item,
            }

            products.append(shopping_cart)

        elif choice == "cart":
            print(shopping_cart)
            for product in products:
                print(product)
        elif choice == "quit":
            confirm = input("Are you sure you want to quit? Y/N: ").lower()
            if confirm == "y":
                print("Thank you, here is your cart")
                print(product)
                done = True
            elif confirm == "n":
                continue
        else:
            print("That is not a valid entry. Please try again.")
            continue
cart()