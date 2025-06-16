import mysql.connector
from tabulate import tabulate

conn = mysql.connector.connect(
    host='localhost',
    user='root',           
    password='Amit@1087',   
    database='pizza_ordering'
)

cursor = conn.cursor()

def show_menu():
    print("\n------ PIZZA MENU ------")
    cursor.execute("SELECT * FROM pizza_menu")
    menu = cursor.fetchall()
    print(tabulate(menu, headers=["Pizza ID", "Name", "Size", "Price"]))
    return menu

def place_order():
    customer_name = input("Enter customer name: ")
    cursor.execute("INSERT INTO orders (customer_name) VALUES (%s)", (customer_name,))
    order_id = cursor.lastrowid

    while True:
        show_menu()
        pizza_id = int(input("Enter Pizza ID to order: "))
        quantity = int(input("Enter quantity: "))
        cursor.execute("INSERT INTO order_details (order_id, pizza_id, quantity) VALUES (%s, %s, %s)", 
                       (order_id, pizza_id, quantity))
        more = input("Do you want to add more pizza? (yes/no): ")
        if more.lower() != 'yes':
            break

    conn.commit()
    print("Order placed successfully!")

def view_orders():
    cursor.execute("""
        SELECT o.order_id, o.customer_name, o.order_date, 
               pm.pizza_name, pm.size, od.quantity, (pm.price * od.quantity) AS total_price
        FROM orders o
        JOIN order_details od ON o.order_id = od.order_id
        JOIN pizza_menu pm ON od.pizza_id = pm.pizza_id
        ORDER BY o.order_id
    """)
    orders = cursor.fetchall()
    print("\n------ ALL ORDERS ------")
    print(tabulate(orders, headers=["Order ID", "Customer", "Date", "Pizza", "Size", "Qty", "Total Price"]))

def main():
    while True:
        print("\n---- PIZZA ORDERING SYSTEM ----")
        print("1. Show Menu")
        print("2. Place Order")
        print("3. View All Orders")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            show_menu()
        elif choice == '2':
            place_order()
        elif choice == '3':
            view_orders()
        elif choice == '4':
            break
        else:
            print("Invalid choice!")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
