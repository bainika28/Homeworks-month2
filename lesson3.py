class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__cpu + self.__memory, self.__cpu - self.__memory, self.__cpu * self.__memory, self.__cpu / self.__memory

    def __str__(self):
        return f"Computer(cpu={self.__cpu}, memory={self.__memory})"

    def __eq__(self, other):
        return self.__memory == other.memory

    def __ne__(self, other):
        return self.__memory != other.memory

    def __lt__(self, other):
        return self.__memory < other.memory

    def __le__(self, other):
        return self.__memory <= other.memory

    def __gt__(self, other):
        return self.__memory > other.memory

    def __ge__(self, other):
        return self.__memory >= other.memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {self.__sim_cards_list[sim_card_number - 1]}")
        else:
            print("Неверный номер сим-карты!")

    def __str__(self):
        return f"Phone(sim_cards={self.__sim_cards_list})"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Прокладывается маршрут до {location}...")

    def __str__(self):
        return f"SmartPhone(cpu={self.cpu}, memory={self.memory}, sim_cards={self.sim_cards_list})"


computer = Computer(3.5, 16)
phone = Phone(["Beeline", "MegaCom", "O!"])
smartphone1 = SmartPhone(2.8, 8, ["Beeline", "MegaCom"])
smartphone2 = SmartPhone(3.0, 12, ["O!"])

print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

print("\nАрифметические вычисления на компьютере:", computer.make_computations())
phone.call(1, "+996 111 222 333")
smartphone1.call(2, "+996 444 555 666")
smartphone1.use_gps("Бишкек, улица Токомбава 1")

print("\nСравнение компьютеров:")
print(computer > smartphone1)
print(computer < smartphone2)
print(computer == smartphone2)
print(computer != smartphone1)