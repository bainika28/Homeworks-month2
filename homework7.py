import sqlite3

conn = sqlite3.connect("hw.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title TEXT NOT NULL,
    price REAL NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
''')

def add_products():
    products = [
        ("Булочка с маком", 50.0, 10),
        ("Булочка с изюмом", 45.0, 15),
        ("Булочка с корицей", 60.0, 20),
        ("Булочка с орехами", 70.0, 25),
        ("Булочка с вареньем", 55.0, 30),
        ("Круассан классический", 80.0, 12),
        ("Круассан с шоколадом", 90.0, 18),
        ("Круассан с миндалем", 95.0, 14),
        ("Эклер ванильный", 120.0, 10),
        ("Эклер шоколадный", 130.0, 15),
        ("Пончик с глазурью", 40.0, 50),
        ("Пончик с начинкой", 45.0, 45),
        ("Брауни классический", 150.0, 20),
        ("Чизкейк Нью-Йорк", 200.0, 8),
        ("Маффин с черникой", 75.0, 30)
    ]
    cursor.executemany('''
    INSERT INTO products (product_title, price, quantity)
    VALUES (?, ?, ?)
    ''', products)
    conn.commit()

def update_quantity(product_id, new_quantity):
    cursor.execute('''
    UPDATE products
    SET quantity = ?
    WHERE id = ?
    ''', (new_quantity, product_id))
    conn.commit()

def update_price(product_id, new_price):
    cursor.execute('''
    UPDATE products
    SET price = ?
    WHERE id = ?
    ''', (new_price, product_id))
    conn.commit()

def delete_product(product_id):
    cursor.execute('''
    DELETE FROM products
    WHERE id = ?
    ''', (product_id,))
    conn.commit()

def print_all_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    for product in products:
        print(product)

def find_cheap_and_low_stock(limit_price, limit_quantity):
    cursor.execute('''
    SELECT * FROM products
    WHERE price < ? AND quantity > ?
    ''', (limit_price, limit_quantity))
    products = cursor.fetchall()
    for product in products:
        print(product)

def search_product_by_title(search_term):
    cursor.execute('''
    SELECT * FROM products
    WHERE product_title LIKE ?
    ''', ('%' + search_term + '%',))
    products = cursor.fetchall()
    for product in products:
        print(product)

add_products()
update_quantity(3, 20)
update_price(2, 55.0)
delete_product(4)
print_all_products()
find_cheap_and_low_stock(100, 5)
search_product_by_title("Круассан")

conn.close()