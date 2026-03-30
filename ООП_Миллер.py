#1
class Employee:
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print(f'My id is {self.id}')

e1 = Employee()
e2 = Employee()
e1.say_id()
e2.say_id()

#2
class Admin(Employee):
    pass

e3 = Admin()
e3.say_id()

#3
class Admin(Employee):
    def say_id(self):
        print(f'I am an admin')

e3 = Admin()
e3.say_id()

#4
class Admin(Employee):
    def say_id(self):
        super().say_id()
        print(f'I am an admin')

e3 = Admin()
e3.say_id()

#5
class Manager(Admin):
    def say_id(self):
        super().say_id()
        print(f'I am an manager')

e4 = Manager()
e4.say_id()

#6
class User():
    def __init__(self, username,  role):
        self.username = username
        self.role = role

    def say_user_info(self):
        print(f'My username is {self.username} and role is {self.role}')

class Admin(Employee, User):
    def __init__(self):
        Employee.__init__(self)
        User.__init__(self, self.id, 'Admin')

e3 = Admin()
e3.say_user_info()

#7
meeting = [Employee(), Admin(), Manager()]

for m in meeting:
    m.say_id()

#8
class Meeting():
    def __init__(self):
        self.attendance = []

    def __add__(self, employee):
        self.attendance.append(employee)

    def __len__(self):
        return len(self.attendance)

m1 = Meeting()
m1 + e1
m1 + e2
m1 + e3
print(len(m1))

#9
from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
    new_id = 1

    def __init__(self):
        self.id = AbstractEmployee.new_id
        AbstractEmployee.new_id += 1

    @abstractmethod
    def say_id(self):
        pass

class Employee(AbstractEmployee):
    def say_id(self):
        print(f'My id is {self.id}')

abstract_e1 = Employee()
abstract_e1.say_id()

#10
class Employee():
    def __init__(self):
        self.id = 1
        self._id = 'single'
        self.__id = 'double'

e = Employee()
print(dir(e))

#11
class  Employee(AbstractEmployee):
    def __init__(self, _name = None):
        super().__init__()
        self.__id = 0
        if isinstance(_name, str):
            self._name = _name
        self._name = None

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def del_name(self):
        del self._name

    def say_id(self):
        print(f'My id is {self.id}')
