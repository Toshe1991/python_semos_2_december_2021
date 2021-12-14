class Company:
    def hire(self, employee, position, salary):
        if employee.company:
            raise Exception(f"{employee} is already working in {employee.company}")

        employee.position = position
        employee.salary = salary
        employee.company = self

        self.employee_list.append(employee)

    def fire(self, employee):
        if (not employee.company) or (employee.company.company_id != self.company_id):
            raise Exception(f"{employee} can't be fired, not working in {self.name}")

        employee.position = None
        employee.salary = None
        employee.company = None

        self.employee_list.remove(employee)

    def get_salary_costs(self):
        total_salary_costs = 0

        for employee in self.employee_list:
            total_salary_costs += employee.salary

        return total_salary_costs

    def __str__(self):
        return self.name


class Employee:
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

    def __repr__(self):
        return self.full_name()



semos = Company()
seavus = Company()

marija = Employee()
kristijan = Employee()
jovan = Employee()

semos.name = "Semos Edukacija"
semos.address = "Kuzman Josifovski Pitu br. 1000"
semos.company_id = "1234"
semos.employee_list = []

seavus.name = "Seavus AD"
seavus.address = "Boris Trajkovski br. 60"
seavus.company_id = "9876"
seavus.employee_list = []

marija.first_name = "Marija"
marija.last_name = "Krstevska"
marija.email = "marija@gmail.com"
marija.salary = None
marija.position = None
marija.company = None

kristijan.first_name = "Kristijan"
kristijan.last_name = "Gjorgiev"
kristijan.email = "kristijan@gmail.com"
kristijan.salary = None
kristijan.position = None
kristijan.company = None

jovan.first_name = "Jovan"
jovan.last_name = "Jankov"
jovan.email = "jovan@yahoo.com"
jovan.salary = None
jovan.position = None
jovan.company = None


semos.hire(kristijan, "Python Developer", 40000)
semos.hire(marija, "HR", 30000)
# semos.hire(marija, "HR", 30000)

# semos.fire(jovan)

# print(semos.get_salary_costs())
#
# semos.fire(marija)
#
# print(semos.get_salary_costs())
#
# for employee in semos.employee_list:
#     print(employee)

# dir() -> 1 argument some object -> return all methods and attributes instance has
# print(dir(kristijan))
# int num = 20  # explicit type notation
# num = 20 # implicit type notation


# __dict__ -> dunder attributes/methods (SPECIAL SYNTAX)
# print(jovan.__dict__)
# print(kristijan.__dict__)
# print(semos.__dict__)

# {"first_name": "Jovan", "last_name": "Jankov" ..., "company": seavus}
# print(marija.company.address)

# print(id(semos))
# print(id(seavus))

# classes are blueprint / kalap za kreiranje na entitetite
# vo Python nemame zagradi za definiranje blokovi

## MEMORY MANAGEMENT IN PYTHON ##

# Non Volatile memory -> Hard Disk (HDD or SSD)
# RAM Memory / Operative memory  - Volatile Memory
# name = "Toshe"
# surname = "Petrovski"
#
# # STACK BASED VIRTUAL MACHINE
# # name -> Registry -> 0001 (Memory Address)
# # surname -> Registry -> 0002 (Memory Address)
#
# # id() -> returns the memory address of the object / variable
# print(id(name))
# print(id(surname))

# def replace(str1, replace_value, replace_str):
#     print(f"Replacing {replace_value} in {str1} with {replace_str}")

# replace(name, "Hello", "Welcome")
# name = "Hello Toshe"
# name = name.replace("Hello", "Welcome").upper()
# print(name)

# "Hello Toshe" -> "Welcome Toshe"


# REMOVING ELEMENT FROM LIST

# kristijan2 = Employee()
# kristijan2.first_name = "Kristijan"
# kristijan2.last_name = "Gjorgiev"
# kristijan2.email = "kristijan@gmail.com"
# kristijan2.salary = None
# kristijan2.position = None
# kristijan2.company = None
#
# list_of_names = [kristijan, marija]
# list_of_names.remove(kristijan2)
#
# print(list_of_names)

