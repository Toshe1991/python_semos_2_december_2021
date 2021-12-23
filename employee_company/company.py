from .offer import Offer


class Company:

    def __init__(self, name, address, company_id):
        # Initialization of attribute values
        self.name = name
        self.address = address
        self.company_id = company_id
        self.employee_list = []
        self.assets = []

    def serialize(self):
        return self.__dict__  # dunder dict method

    @property  # Getter
    def company_id(self):
        return self.__company_id

    @company_id.setter
    def company_id(self, value):
        if not isinstance(value, str) or len(value) != 4 or not value.isdigit():
            raise Exception(f"Value for company id is not valid. Value provided: {value}")

        self.__company_id = value

    def make_offer(self, employee, salary):
        offer = Offer(self, employee, salary)
        offer.send_offer()
        print(offer)

    def fire(self, employee):
        if (not employee.company) or (employee.company.company_id != self.__company_id):
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

