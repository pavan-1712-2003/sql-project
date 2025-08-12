import sqlite3
def connect():
    conn = sqlite3.connect("cars.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS car
        ( id INTEGER PRIMARY KEY ,
        make TEXT NOT NULL,
        model varchar,
        year INTEGER,
        price REAL,
        reviews text,
        rating float
        )''')
    conn.close()
    conn.commit()
    
print("crated  a database successfully")

def add_car(make, model, year, price, reviews, rating):
        conn = sqlite3.connect("cars.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM car")
        cursor.execute("INSERT INTO car (make, model, year, price, reviews, rating) VALUES (?, ?, ?, ?, ?, ?)",
                   (make, model, year, price, reviews, rating))
        conn.commit()
print("car added successfully")


def update_model(new_model,car_id):
    conn = sqlite3.connect("cars.db")
    cursor = conn.cursor()
    cursor.execute("update car set model = ? where id = ?", (new_model,car_id))
print("updated a model")


def view_all_cars():
    conn = sqlite3.connect("cars.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM car")
    return cursor.fetchall()
print('showed')
    
def update_review_rating(car_id, new_review, new_rating):
    conn = sqlite3.connect("cars.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE car SET reviews = ?, rating = ? WHERE id = ?",(new_review, new_rating, car_id))
print("Review and rating updated.")

def delete_car(car_id):
    conn = sqlite3.connect("cars.db")
    cursor = conn.cursor()
    cursor.excute(" delete from car where id = ?")
    conn.commit()
    conn.close()


def menu():
    connect()

    while True:
        print("\nCar Database Menu")
        print("1. Add car")
        print("2. Update car model")
        print("3. View all cars")
        print("4. Update review & rating")
        print("5. Delete car")
        print("6. Exit")

        my_choice = input("Enter a number (1-6): ")

        if my_choice == '1':
            make = input("Make: ")
            model = input("Model: ")
            year = int(input("Year: "))
            price = float(input("Price: "))
            review = input("Review: ")
            rating = float(input("Rating (out of 5): "))
            add_car(make, model, year, price, review, rating)

        elif my_choice == '2':
            car_id = int(input("Enter Car ID to update: "))
            new_model = input("Enter new model: ")
            update_model(car_id, new_model)

        elif my_choice == '3':
             cars = view_all_cars()
             for car in cars:
                print(f"[ID: {car[0]}] {car[1]} {car[2]} ({car[3]}) - ₹{car[4]:,.2f}")
                print(f"    Rating: {car[6]}/5")
                print(f"    Review: {car[5]}\n")

        elif my_choice == '4':
            car_id = int(input("Enter Car ID to update: "))
            new_review = input("New Review: ")
            new_rating = float(input("New Rating: "))
            update_review_rating(car_id, new_review, new_rating)

        elif my_choice == '5':
            car_id = int(input("Enter Car ID to delete: "))
            delete_car(car_id)

        elif my_choice == '6':
            print("Goodbye")
            break

        else:
          print("Invalid choice. Try again.")
    menu()
