# 🍔 Talabat Ordering System

A console-based Python program (built with **PyCharm**) that simulates the Talabat food-ordering flow: registration, choosing a restaurant, building a cart, checkout, and printing a receipt.

## 🔄 How It Works

| Step | Feature | Description |
| --- | --- | --- |
| 1 | Registration | Collects name, email (must contain `@` and end with `.com`), phone (exactly 11 digits), address, username, and password |
| 2 | Categories | Displays the main categories: Food, Groceries, Health, Beauty |
| 3 | Restaurants | Lets the user choose a restaurant |
| 4 | Menu | Shows the menu of the selected restaurant |
| 5 | Cart | Adds items with quantities and calculates the total |
| 6 | Summary | Shows the subtotal, delivery fee (20.00 EGP), and service fee (25.50 EGP) |
| 7 | Checkout | Confirms phone and address, then selects a payment method (Visa / Cash) |
| 8 | Receipt | Prints the final order receipt |

## 🍽️ Restaurants

- EL Abd (desserts)
- BLABAN (desserts)
- KANSAS Fried Chicken
- Wahmy Burger

## 🚀 How to Run (PyCharm)

This project was developed and tested using **PyCharm**.

**Requirements:** Python 3 and PyCharm (Community or Professional). No extra libraries are needed.

1. Open **PyCharm**.
2. Go to **File → Open** and select the project folder (`talabat-ordering-system`).
3. If PyCharm asks for an interpreter, choose your installed **Python 3**.
4. Right-click `talabat.py` and choose **Run 'talabat'** (or press `Shift + F10`).
5. Type your inputs in the **Run** window at the bottom and press `Enter` after each one.

### Sample flow
1. Fill in the registration details.
2. Choose a category (e.g. `1` for Food).
3. Choose a restaurant (`1`–`4`).
4. Enter an item number and a quantity. Type `done` when finished.
5. Choose a payment method: `Visa` or `Cash`.
6. Get your receipt.

## 🧠 Python Concepts Used

- Functions and return values
- `while` loops with input validation
- Dictionaries, lists, and tuples
- String formatting with f-strings
- Basic error handling through validation loops

## 👩‍💻 Team Members

| Name | ID | S.N |
| --- | --- | --- |
| Menna Muhammed Ali | 512395135 | 65 |
| Menna Khaled Gamal Reyad | 512395133 | 64 |
| Mennatullah Taha Sayed | 512395121 | 62 |
| Merna Osama Mahmoud | 512395165 | 344 |


## 📜 License

This project was created for educational purposes.
