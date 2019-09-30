class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        self.item_name = str(item_name)
        self.item_price = int(item_price)
        self.item_quantity = int(item_quantity)
        self.item_description = str(item_description)
    
    def print_item_cost(self):
        print("{0} {1} @ ${2} = ${3}".format(self.item_name, self.item_quantity, self.item_price, (self.item_price * self.item_quantity)))
    
    def print_item_description(self):
        print("{0}: {1}".format(self.item_name, self.item_description))

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = str(customer_name)
        self.current_date = str(current_date)
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for entry in self.cart_items:
            if entry.item_name == item_name:
                self.cart_items.remove(entry)
                break
        else:
            print("Item not found in cart. Nothing removed.")
    
    def modify_item(self, item):
        for entry in self.cart_items:
            if entry.item_name == item.item_name:
                index = self.cart_items.index(entry)
                self.cart_items[index].item_quantity = item.item_quantity
                break
        else:
            print("Item not found in cart. Nothing modified.")
    
    def get_num_items_in_cart(self):
        num = 0
        for item in self.cart_items:
            num += item.item_quantity
        return num

    def get_cost_of_cart(self):
        cost = 0
        for item in self.cart_items:
            cost += (item.item_price * item.item_quantity)
        return cost
    
    def print_total(self):
        print("{0}'s Shopping Cart - {1}".format(self.customer_name, self.current_date))
        print("Number of Items: " + str(self.get_num_items_in_cart()))
        print()
        if len(self.cart_items) > 0:
            for item in self.cart_items:
                print("{0} {1} @ ${2} = ${3}".format(item.item_name, item.item_quantity, item.item_price, (item.item_price * item.item_quantity)))
        else:
            print("SHOPPING CART IS EMPTY")
        print()
        print("Total: $" + str(self.get_cost_of_cart()))
    
    def print_descriptions(self):
        print("{0}'s Shopping Cart - {1}".format(self.customer_name, self.current_date))
        print()
        print("Item Descriptions")
        for item in self.cart_items:
            print("{0}: {1}".format(item.item_name, item.item_description))

def print_menu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    print()

if __name__ == "__main__":
    name = input("Enter customer's name:\n")
    date = input("Enter today's date:\n")
    print()
    print("Customer name: " + name)
    print("Today's date: " + date)
    print()

    cart = ShoppingCart(name, date)

    print_menu()

    while True:
        option = input("Choose an option:\n")

        if option == "a":
            print("ADD ITEM TO CART")
            item = ItemToPurchase()

            item.item_name = input("Enter the item name:\n")
            item.item_description = input("Enter the item description:\n")
            item.item_price = int(input("Enter the item price:\n"))
            item.item_quantity = int(input("Enter the item quantity:\n"))
            ShoppingCart.add_item(cart, item)
            print()
            print_menu()
        elif option == "r":
            print("REMOVE ITEM FROM CART")
            item = input("Enter name of item to remove:\n")
            ShoppingCart.remove_item(cart, item)
            print()
            print_menu()
        elif option == "c":
            print("CHANGE ITEM QUANTITY")
            item = ItemToPurchase()
            item.item_name = input("Enter the item name:\n")
            item.item_quantity = int(input("Enter the new quantity:\n"))
            ShoppingCart.modify_item(cart, item)
            print()
            print_menu()
        elif option == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            ShoppingCart.print_descriptions(cart)
            print()
            print_menu()
        elif option == "o":
            print("OUTPUT SHOPPING CART")
            ShoppingCart.print_total(cart)
            print()
            print_menu()
        elif option == "q":
            break
        else:
            option = input("Choose an option:\n")