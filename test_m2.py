import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS stores (
        store_id INTEGER PRIMARY KEY,
        title VARCHAR(100) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        code VARCHAR(2) PRIMARY KEY,
        title VARCHAR(150) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        title VARCHAR(250) NOT NULL,
        category_code VARCHAR(2) NOT NULL,
        unit_price FLOAT NOT NULL,
        stock_quantity INTEGER NOT NULL,
        store_id INTEGER NOT NULL,
        FOREIGN KEY (category_code) REFERENCES categories(code),
        FOREIGN KEY (store_id) REFERENCES stores(store_id)
    )
''')

cursor.execute("SELECT COUNT(*) FROM stores")
if cursor.fetchone()[0] == 0:
    cursor.executemany('''
        INSERT INTO stores (store_id, title) VALUES (?, ?)
    ''', [
        (1, 'Asia'),
        (2, 'Globus'),
        (3, 'Spar'),
        (4, 'Narodnyi'),
        (5, 'Mia Home'),
        (6, 'Kanzler')
    ])

cursor.execute("SELECT COUNT(*) FROM categories")
if cursor.fetchone()[0] == 0:
    cursor.executemany('''
        INSERT INTO categories (code, title) VALUES (?, ?)
    ''', [
        ('FD', 'Food products'),
        ('EL', 'Electronics'),
        ('CL', 'Clothes'),
        ('HM', 'Home products'),
        ('ST', 'Stationery')
    ])

cursor.execute("SELECT COUNT(*) FROM products")
if cursor.fetchone()[0] == 0:
    cursor.executemany('''
        INSERT INTO products (id, title, category_code, unit_price, stock_quantity, store_id) 
        VALUES (?, ?, ?, ?, ?, ?)
    ''', [
        (1, 'Chocolate', 'FD', 10.5, 129, 1),
        (2, 'Jeans', 'CL', 120.0, 55, 2),
        (3, 'T-Shirt', 'CL', 20.0, 15, 1),
        (4, 'Laptop', 'EL', 1000.0, 5, 3),
        (5, 'Apple', 'FD', 2.0, 300, 1),
        (6, 'Sofa', 'HM', 500.0, 10, 5),
        (7, 'Notebook', 'ST', 3.5, 200, 6),
        (8, 'Chair', 'HM', 150.0, 20, 4),
        (9, 'Pen', 'ST', 1.2, 500, 6)
    ])

conn.commit()


def get_stores():
    cursor.execute("SELECT store_id, title FROM stores")
    return cursor.fetchall()


def get_products_by_store(store_id):
    cursor.execute("""
        SELECT p.title, c.title, p.unit_price, p.stock_quantity
        FROM products p
        JOIN categories c ON p.category_code = c.code
        WHERE p.store_id = ?
    """, (store_id,))
    return cursor.fetchall()


def main():
    while True:
        print(
            "\nВы можете отобразить список продуктов по выбранному id магазина из перечня ниже, для выхода из программы введите цифру 0:\n")

        stores = get_stores()
        for store in stores:
            print(f"{store[0]}. {store[1]}")

        store_id = input("\nВведите ID магазина (или 0 для выхода): ")

        if store_id == '0':
            print("Выход из программы...")
            break

        if not store_id.isdigit() or int(store_id) not in [s[0] for s in stores]:
            print("Ошибка: Введите корректный ID магазина!")
            continue

        store_id = int(store_id)
        products = get_products_by_store(store_id)

        if products:
            print("\nТовары в магазине:")
            for product in products:
                print(
                    f"\nНазвание продукта: {product[0]}\nКатегория: {product[1]}\nЦена: {product[2]}\nКоличество на складе: {product[3]}")
        else:
            print("В этом магазине нет товаров.")


if __name__ == "__main__":
    main()

conn.close()