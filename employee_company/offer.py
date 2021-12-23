class Offer:
    minimum_salary = 15000

    def __init__(self, company, employee, salary):

        if not isinstance(salary, int):
            raise Exception(f"{salary} must be integer.")

        if salary < self.minimum_salary:
            raise Exception(f"Salary provided is under minimum wage of {self.minimum_salary}")

        self.company = company
        self.employee = employee
        self.salary = salary

    def send_offer(self):
        self.employee.receive_offer(self)

    def __str__(self):
        return f"Offer from {self.company} to {self.employee}"

    def __repr__(self):
        return f"Offer from {self.company} to {self.employee}"

    def serialize(self):
        return self.__dict__  # dunder dict method
