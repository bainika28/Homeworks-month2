class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Имя: {self.full_name}")
        print(f"Возраст: {self.age}")
        print(f"Женат/Замужем: {'Да' if self.is_married else 'Нет'}")


class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def calculate_average_mark(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def introduce_myself(self):
        super().introduce_myself()
        print("Оценки:")
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")
        print(f"Средняя оценка: {self.calculate_average_mark():.2f}")


class Teacher(Person):
    base_salary = 30000

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        if self.experience > 3:
            bonus = (self.experience - 3) * 0.05 * self.base_salary
            return self.base_salary + bonus
        return self.base_salary

    def introduce_myself(self):
        super().introduce_myself()
        print(f"Опыт работы: {self.experience} лет")
        print(f"Зарплата: {self.calculate_salary():.2f}")

def create_students():
    student1 = Student("Иван Иванов", 16, False, {"Математика": 5, "История": 4, "Физика": 3})
    student2 = Student("Вася Пупкин", 17, False, {"Математика": 4, "История": 5, "Физика": 4})
    student3 = Student("Евгений Кабачков", 16, False, {"Математика": 3, "История": 3, "Физика": 5})
    return [student1, student2, student3]


teacher = Teacher("Виктор Николаевич", 45, True, 10)
teacher.introduce_myself()

students = create_students()

for student in students:
    student.introduce_myself()