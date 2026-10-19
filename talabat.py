#registration:menna muhammed ali
print("\twelcome to talabat")
def registration():
    n = input("Enter your full name: ")
    def is_valid_email(email):
        return email.endswith(".com") and "@" in email
    while True:
        e = input("Enter your email address: ")
        if is_valid_email(e):
            break
        else:
            print("Invalid email address. Please ensure it contains '@' and ends with '.com'.")
    while True:
        p = input("Enter your phone number: ")
        if len(p) == 11 and p.isdigit():
            break
        else:
            print("Invalid phone number. Please enter exactly 11 digits.")
    a = input("Enter your address: ")
    u = input("Enter username: ")
    s = input("Enter password: ")
    print("\nRegistration successful!")
    return {
        "name": n,
        "email": e,
        "phone": p,
        "address": a,
        "username": u,
        "password": s
    }
user_data = registration()

#process 2:menna taha
def display_categories():
    print("""
        Main Categories
        1. Food
        2. Groceries
        3. Health
        4. Beauty
        0. Exit
    """)

display_categories()
category = int(input("Choose a Category from (1, 2, 3, 4) or 0 for Exit: "))

#process 3:menna muhammed ali
def choose_restaurant_and_menu():
    def restaurants():
        print("""
        1. EL Abd
        2. BLABAN
        3. KANSAS Fried Chicken
        4. Wahmy Burger
        """)
    restaurants()
    while True:
        op = int(input("\nChoose an option from 1, 2, 3, 4: "))
        if op in [1, 2, 3, 4]:
            return op
        else:
            print("Please enter an option from 1, 2, 3, 4 ")

#process 4: merna osama
def display_menu(op):
    menu_items = {
        'EL Abd': {
            1: 'Caramel Cinnamon Roll: 8.00',
            2: 'Plain Basbousa: 4.00',
            3: 'Crispy Ball: 3.50',
            4: 'Konafa Rolls Box: 6.00'
        },
        'BLABAN': {
            5: 'Koshari Nutella: 7.00',
            6: 'Dubai Crepe: 9.00',
            7: 'Cheese Bomb: 6.65',
            8: 'Chocolate Rice: 2.00'
        },
        'KANSAS': {
            9: 'Big Cola: 10.00',
            10: 'Chicken Sandwich: 15.00',
            11: 'Fries Wrap: 5.00',
            12: 'Classic Box: 7.99'
        },
        'Wahmy': {
            13: 'Ranch Burger: 175.00',
            14: 'Special Burger: 180.00',
            15: 'Classic Burger: 160.00',
            16: 'BBQ Burger: 190.00'
        }
    }

    restaurant_names = {
        1: 'EL Abd',
        2: 'BLABAN',
        3: 'KANSAS',
        4: 'Wahmy',
    }

    if op in restaurant_names:
        print(f"\nMenu for {restaurant_names[op]}:")
        for key, value in menu_items[restaurant_names[op]].items():
            print(f"{key}: {value}")
    else:
        print("Invalid option. Please choose a valid restaurant.")

#process 5: menna khaled
def add_to_cart(cart, item, price, quantity):
    cart.append((item, price, quantity))
    return cart
def calculate_total(cart):
    total = 0
    for item, price, quantity in cart:
        total += price * quantity
    return total
def main():
    menu_items_dict = {
        1: ('Caramel Cinnamon Roll', 8.00),
        2: ('Plain Basbousa', 4.00),
        3: ('Crispy Ball', 3.50),
        4: ('Konafa Rolls Box', 6.00),
        5: ('Koshari Nutella', 7.00),
        6: ('Dubai Crepe', 9.00),
        7: ('Cheese Bomb', 6.65),
        8: ('Chocolate Rice', 2.00),
        9: ('Big Cola', 10.00),
        10: ('Chicken Sandwich', 15.00),
        11: ('Fries Wrap', 5.00),
        12: ('Classic Box', 7.99),
        13: ('Ranch Burger', 175.00),
        14: ('Special Burger', 180.00),
        15: ('Classic Burger', 160.00),
        16: ('BBQ Burger', 190.00)
    }
    shopping_cart = []
    while True:
        restaurant_option = choose_restaurant_and_menu()
        display_menu(restaurant_option)
        while True:
            item_number = input("Please select your preferred item by its number (or type 'done' to finish): ")
            if item_number.lower() == 'done':
                break
            item_number = int(item_number)
            if item_number in menu_items_dict:
                item, price = menu_items_dict[item_number]
                quantity = int(input(f"Enter the quantity for {item}: "))
                add_to_cart(shopping_cart, item, price, quantity)
            else:
                print("Item not found in the menu.")
        break

    print("\nThank you for using Talabat!")
    print("\nShopping Cart Summary:")
    for item, price, quantity in shopping_cart:
        print(f"{item}: {quantity} x {price} = {quantity * price}")

#process 6:merna osama
    print("\nYour Cart:")
    total = 0
    for item, price, quantity in shopping_cart:
        print(f"{item} - {price:.2f} EGP x {quantity}")
        total += price * quantity

    print(f"Subtotal: {total:.2f} EGP")
    delivery_fee = 20.00
    service_fee = 25.50
    total_amount = total + delivery_fee + service_fee

    print(f"Delivery Fee: {delivery_fee:.2f} EGP")
    print(f"Service Fee: {service_fee:.2f} EGP")
    print(f"Total Amount: {total_amount:.2f} EGP\n")

    payment_method = checkout(user_data)

    place_order(shopping_cart, user_data['address'], user_data['phone'], delivery_fee, service_fee, payment_method)

#process 7: menna taha
def checkout(user_data):
    print("\n    Checkout    ")
    print(f"User Phone Number: {user_data['phone']}")
    print(f"User Address: {user_data['address']}\n")

    while True:
        payment_method = input("Choose a payment method (Visa/Cash): ")
        if payment_method.lower() in ["visa", "cash"]:
            print("Payment method selected: ", payment_method)
            print("Thank you for your order! It will be delivered shortly.")
            return payment_method
        else:
            print("Invalid payment method. Please choose 'Visa' or 'Cash'.")

#process 8:menna khaled
def place_order(cart, address, phone, delivery_fee, service_fee, payment_method):
    print("\n--- Order Receipt ---")
    print("Address:", address)
    print("Phone:", phone)
    print("\nOrder Items:")

    subtotal = calculate_total(cart)
    for item, price, quantity in cart:
        item_total = price * quantity
        print(f"- {item}: {price:.2f} EGP x {quantity} = {item_total:.2f} EGP")

    print(f"\nSubtotal: {subtotal:.2f} EGP")
    print(f"Delivery Fee: {delivery_fee:.2f} EGP")
    print(f"Service Fee: {service_fee:.2f} EGP")

    total_amount = subtotal + delivery_fee + service_fee
    print(f"Total Amount: {total_amount:.2f} EGP")
    print(f"Payment Method: {payment_method}")

    print("\nThank you for your order!\nIt will be delivered within 30 minutes.")
main()
