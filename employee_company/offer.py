class Offer:
    minimum_salary = 15000

    def __init__(self, company, employee, salary, position):

        if not isinstance(salary, int):
            raise Exception(f"{salary} must be integer.")

        if not isinstance(position, str):
            raise Exception(f"{position} must be string.")

        if salary < self.minimum_salary:
            raise Exception(f"Salary provided is under minimum wage of {self.minimum_salary}")

        self.company = company
        self.employee = employee
        self.salary = salary
        self.position = position

    def send_offer(self):
        self.employee.receive_offer(self)

    def __str__(self):
        return f"Offer from {self.company} to {self.employee}"

    def __repr__(self):
        return f"Offer from {self.company} to {self.employee}"
