# # 1
# class BankAccount:
def __init__(self, owner, account_number, balance):

        self.owner = owner
        self.account_number = account_number
        self.__balance = balance   # keep it private

    def deposit(self, amount):
        if amount <= 0:
            print("Amount should be greater than 0")
        else:
            self.__balance += amount
            print("Money added")
            
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not enough balance")
        else:
            self.__balance -= amount
            print("Money withdrawn")

    def get_balance(self):
        return self.__balance


acc1 = BankAccount("Amna", 123, 1000)
acc1.deposit(300)
acc1.withdraw(200)
print("Balance is:", acc1.get_balance())
#
# # 2
#
# class Student:
#
#     def __init__(self, name, student_id):
#         self.name = name
#         self.student_id = student_id
#         self.__marks = []   # private list
#
#     def add_mark(self, mark):
#         if mark >= 0 and mark <= 100:
#             self.__marks.append(mark)
#         else:
#             print("Marks should be between 0 and 100")
#
#     def get_average(self):
#         if len(self.__marks) == 0:
#             return 0
#         return sum(self.__marks) / len(self.__marks)
#
#     def get_grade(self):
#         avg = self.get_average()
#         if avg >= 80:
#             return "A"
#         elif avg >= 60:
#             return "B"
#         elif avg >= 40:
#             return "C"
#         else:
#             return "F"
#
# # checking
#
# s1 = Student("Ali", 101)
# s1.add_mark(75)
# s1.add_mark(85)
# print("Average:", s1.get_average())
#
# # 3
#
# class CoffeeMachine:
#
#     def _heat_water(self):
#         print("Heating water...")
#
#     def _grind_beans(self):
#         print("Grinding beans...")
#
#     def _filter_water(self):
#         print("Making coffee...")
#
#     def make_coffee(self):
#         self._heat_water()
#         self._grind_beans()
#         self._filter_water()
#         print("Coffee is ready")

# checking
#
# cm = CoffeeMachine()
# cm.make_coffee()
#
# # 4
# class SmartTV:
#
#     def __init__(self):
#         self.__current_channel = 1   # starting channel
#
#     def _check_signal(self):
#         print("Checking signal...")
#
#     def _decode_stream(self):
#         print("Loading channel...")

    # def _update_display(self):
    #     print("Display updated")
    #
    # def change_channel(self, number):
    #     self._check_signal()
    #     self._decode_stream()
    #     self._update_display()
    #     self.__current_channel = number
    #     print("Now on channel", number)
    #
    # def get_channel(self):
    #     return self.__current_channel

# checking

# tv1 = SmartTV()
# tv1.change_channel(7)
# print("Current channel:", tv1.get_channel())
#
#
# # 5
# class Vehicle:
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def start(self):
#         print("Engine started")
#     def display_info(self):
#         print(self.make, self.model, self.year)
#
#
# class Truck(Vehicle):
#
#     def __init__(self, make, model, year, cargo_capacity):
#         super().__init__(make, model, year)
#         self.cargo_capacity = cargo_capacity
#
#     def load_cargo(self, weight):
#         if weight <= self.cargo_capacity:
#             print("Cargo loaded")
#         else:
#             print("Too much weight")
#
#
# class Motorcycle(Vehicle):
#
#     def __init__(self, make, model, year, has_sidecar):
#         super().__init__(make, model, year)
#         self.has_sidecar = has_sidecar
#
# # checking
#
# t1 = Truck("Toyota", "Hilux", 2022, 1000)
# t1.start()
# t1.display_info()
# t1.load_cargo(900)
# m1 = Motorcycle("Honda", "125", 2021, False)
# m1.start()
# m1.display_info()