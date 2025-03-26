import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
);
""")

cursor.executemany("""
INSERT INTO countries (title) VALUES (?)
""", [('Кыргызстан',), ('Германия',), ('Китай',)])

cursor.execute("""
CREATE TABLE IF NOT EXISTS cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    area REAL DEFAULT 0,
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES countries(id)
);
""")

cursor.executemany("""
INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)
""", [
    ('Бишкек', 200.0, 1),
    ('Ош', 150.5, 1),
    ('Берлин', 891.8, 2),
    ('Гамбург', 755.3, 2),
    ('Пекин', 16410.5, 3),
    ('Шанхай', 6340.5, 3),
    ('Мюнхен', 310.7, 2)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    city_id INTEGER,
    FOREIGN KEY (city_id) REFERENCES cities(id)
);
""")

cursor.executemany("""
INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)
""", [
    ('Айзада', 'Сатарова', 1),
    ('Тимур', 'Жумабеков', 1),
    ('Анастасия', 'Иванова', 2),
    ('Максим', 'Смирнов', 3),
    ('Надежда', 'Кузнецова', 3),
    ('Кирилл', 'Попов', 4),
    ('Михаил', 'Петров', 4),
    ('Ирина', 'Сидорова', 5),
    ('Ольга', 'Федорова', 5),
    ('Виктор', 'Лебедев', 6),
    ('Евгений', 'Давыдов', 6),
    ('Александра', 'Громова', 7),
    ('Дмитрий', 'Чистяков', 7),
    ('София', 'Ларина', 2)
])


def get_cities():
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()
    return cities


def get_students_by_city(city_id):
    cursor.execute("""
        SELECT students.first_name, students.last_name, countries.title AS country, 
               cities.title AS city, cities.area 
        FROM students 
        JOIN cities ON students.city_id = cities.id
        JOIN countries ON cities.country_id = countries.id
        WHERE cities.id = ?
    """, (city_id,))
    students = cursor.fetchall()
    return students


def main():
    print(
        "Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

    cities = get_cities()
    for city in cities:
        print(f"{city[0]} {city[1]}")

    city_id = int(input("Введите id города: "))
    if city_id == 0:
        print("Выход из программы.")
        return

    students = get_students_by_city(city_id)
    if students:
        print(f"\nУченики в городе {cities[city_id - 1][1]}:")
        for student in students:
            print(f"{student[0]} {student[1]}, {student[2]}, {student[3]}, Площадь города: {student[4]}")
    else:
        print("Нет учеников в этом городе.")

    main()


if __name__ == "__main__":
    main()

conn.close()