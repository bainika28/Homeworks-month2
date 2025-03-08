class Figure:
    unit = "cm"

    def __init__(self):
        pass

    def calculate_area(self):
        raise NotImplementedError("Метод calculate_area() должен быть переопределен в подклассах")

    def info(self):
        raise NotImplementedError("Метод info() должен быть переопределен в подклассах")


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        print(f"Square side length: {self.__side_length}{self.unit}, area: {self.calculate_area()}{self.unit}²")


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        print(f"Rectangle length: {self.__length}{self.unit}, width: {self.__width}{self.unit}, area: {self.calculate_area()}{self.unit}²")


figures = [
    Square(5),
    Square(7),
    Rectangle(5, 8),
    Rectangle(10, 3),
    Rectangle(6, 4)
]

for figure in figures:
    figure.info()