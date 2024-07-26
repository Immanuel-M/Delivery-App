import datetime

#Parent Class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

#Implementing Inheritence from the Parent Class
class Fruit(Product):
    def __init__(self, name, price):
        #Inherting all info from Parent
        super().__init__(name, price)

#Additional Class, Child of Parent (Inheritence)
class Meat(Product):
    def __init__(self, name, price):
        super().__init__(name, price)

#Additional Class, Child of Parent (Inheritence)
class HouseholdItem(Product):
    def __init__(self, name, price):
        super().__init__(name, price)

#Seperate individual class (Parent)
class Order:
    def __init__(self):
        self.cart = []

    #Method/Function for adding to cart
    def add_to_cart(self, product, quantity):
        self.cart.append((product, quantity))

    #Method/Function for displaying cart contents
    def display_cart(self):
        print("\nYour cart contains:")
        for product, quantity in self.cart:
            print(f"- {quantity} x {product.name} at ${product.price:.2f} each")

    #Method for total
    def calculate_total(self, tax_rate):
        subtotal = sum(quantity * product.price for product, quantity in self.cart)
        tax = subtotal * tax_rate
        total = subtotal + tax
        return subtotal, tax, total

#Main class to call. Implemented in Main program
class DeliveryApp:
    def __init__(self):
        self.order = Order()
        self.delivery_details = {}
        self.tax_rate = 0.0725 #Implement Current CA Tax Rate
        self.products = {
            "Fruit": [Fruit("Apples",1.50), Fruit("Bananas",0.50), Fruit("Oranges",0.75), Fruit( "Grapes",2.00)],
            "Meat": [Meat("Beef",5.00), Meat("Chicken",3.00), Meat("Pork",4.00), Meat("Sausage",6.00)],
            "House Items": [HouseholdItem("Toiletries",3.00), HouseholdItem("Cleaning Products",2.50), HouseholdItem("Cleaning Rags",1.00),
                           HouseholdItem("Paper Towels", 1.50)]
        }
        

    #Method for main menu
    def main_menu(self):
        print("\nPlease Select an option from the main menu below:")
        print("1) Fruit")
        print("2) Meats")
        print("3) Basic House Hold Items")
        print("4) Done selecting all items")
        print("0) Exit Program")
    
    #Method/function for Household items
    def list_products(self, category):
        products = self.products[category]
        #for loop to display item and price
        for i in range(len(products)):
            print(f"{i + 1}) {products[i].name} - ${products[i].price:.2f} each")

        choice = int(input("choice: "))
        quantity = int(input("Enter quantity: "))
        
        #Condition to add to cart once item and quantity chosen
        if 1 <= choice <= len(products):
            selected_product = products[choice -1]
            self.order.add_to_cart(selected_product, quantity)
            print(f"{quantity} x {selected_product.name} selected and added to cart.")
        else:
            print("Invalid selection. Please try again.")

    
    #Delivery Options
    def delivery_options(self):
        print("\nDelivery Options, Date, and Time:")
        while True:
            #Condition for calling class instance
            self.delivery_details['date'] = input("Enter delivery date (MM-DD-YYYY): ")
            print("*Please note that we do NOT deliver on major holidays*")
            try:
                #Date format. Y must be capitol
                datetime.datetime.strptime(self.delivery_details['date'], '%m-%d-%Y')
                break
            #Exception Error
            except ValueError:
                print("Invalid date format. Please try again.")

        while True:  
            #Time format. User MUST include the colon.
            self.delivery_details['time'] = input("Enter delivery time (HH:MM): ")
            try:
                datetime.datetime.strptime(self.delivery_details['time'], '%H:%M')
                break
            #Exception Error
            except ValueError:
                print("Invalid time format. Please try again.")


        #Delivery Location Method
    def get_delivery_location(self):
        self.delivery_details['location'] = input("Where would you like us to drop off your items? (ex. porch, door-mat): ")

        #Summary to display 
    def display_summary(self):
        print('\nOrder Summary:')
        self.order.display_cart()
        #Unpacking Tuple. Necessary as 3 variables assigned to one task
        subtotal, tax, total = self.order.calculate_total(self.tax_rate)
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Tax: ${tax:.2f}")
        print(f"Total: ${total:.2f}")
        print(f"Delivery Date: {self.delivery_details['date']}")
        print(f"Delivery Time: {self.delivery_details['time']}")
        print(f"Delivery Location: {self.delivery_details['location']}")

        #Output Order Summary to Text file
    def save_summary(self):
        with open("order_receipt.txt", "w") as file:
            file.write("Order Receipt:\n")
            for product, quantity, in self.order.cart:
                file.write(f" - {quantity} x{product.name} at ${product.price:.2f} each\n")
            #Unpacking Tuple. Necessary as 3 variables assigned to one task
            subtotal, tax, total = self.order.calculate_total(self.tax_rate)
            #Info to be written into document (Reciept)
            file.write(f"Subtotal: ${subtotal:.2f}\n")
            file.write(f"Tax: ${tax:.2f}\n")
            file.write(f"Total: ${total:.2f}\n")
            file.write(f"Delivery Date: {self.delivery_details['date']}\n")
            file.write(f"Delivery Time: {self.delivery_details['time']}\n")
            file.write(f"Delivery Location: {self.delivery_details['location']}\n")
            file.write(f"\n***Thank you for shopping with us! We appreciate your business!***\n")

    #Start Menu. Setting if/else conditions
    def start(self):
        self.greeting()
        while True:
            self.main_menu()
            user_choice = int(input("choice: "))
            print("\n")
            if user_choice == 0:
                print("Thanks for using the App. See you in the future.")
                return
            elif user_choice == 1:
                self.list_products("Fruit")
            elif user_choice == 2:
                self.list_products("Meat")
            elif user_choice == 3:
                self.list_products("House Items")
            elif user_choice == 4:
                break
            else:
                print("Invalid choice, please try again.\n")
        
        self.delivery_options()
        self.get_delivery_location()
        self.display_summary()
        self.save_summary()

#Main Greeting to display when running app
    def greeting(self):
        print("\n\tWelcome to the Pick - Up App!")
        print("---------------------------------------------")
        print("\tSponsored by Morris Technologies\n")
        
#Really wanted to implement the TkCalendar, but ran out of time. I'll update this program in the future.