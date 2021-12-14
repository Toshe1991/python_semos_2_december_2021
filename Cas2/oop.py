class Company:

    def __init__(self, name, address, company_id):
        # Initialization of attribute values
        self.name = name
        self.address = address
        self.company_id = company_id
        self.employee_list = []

    def hire(self, employee, position, salary):
        if employee.company:
            raise Exception(f"{employee} is already working in {employee.company}")

        if salary < Employee.minimum_salary:
            raise Exception(f"Can't hire {employee}, salary must be above {Employee.minimum_salary}")

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
    minimum_salary = 15000

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.salary = None
        self.position = None
        self.company = None

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

    def __repr__(self):
        return self.full_name()

semos = Company("Semos Edukacija", "Kuzman Josifovski Pitu br. 1000", "1234")
seavus = Company("Seavus AD", "Boris Trajkovski br. 60", "9876")

marija = Employee("Marija", "Krstevska", "marija@gmail.com")
kristijan = Employee("Kristijan", "Gjorgiev", "kristijan@gmail.com")
jovan = Employee("Jovan", "Jankov", "jovan@yahoo.com")

# semos.hire(jovan, "Developer", 14999)
# print(semos.employee_list)

# print(isinstance(jovan, Company))

class A:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            return True

        return False

obj1 = A("Hello", 100)
obj2 = A("Hello", 100)

print(obj1 == obj2)