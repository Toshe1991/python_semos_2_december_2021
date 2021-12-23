from .company import Company


class Employee:

    def __init__(self, first_name, last_name, email, embg):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.salary = None
        self.company = None
        self.embg = self.validate_embg(embg)
        self.offers = dict()

    def deserialize_object(self, salary, position, company, offers):
        self.salary = salary
        self.position = position
        self.company = company
        self.offers = offers

    def serialize(self):
        return self.__dict__  # dunder dict method

    @staticmethod
    def validate_embg(embg):
        if len(str(embg)) != 13:
            raise Exception(f"Invalid EMBG: {embg}. Must be 13 characters")

        return embg

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

    def __repr__(self):
        return self.full_name()

    def receive_offer(self, offer):
        if not isinstance(offer.company, Company):
            raise Exception(f"{offer.company} is not instance of class Company.")

        if not isinstance(offer.employee, Employee):
            raise Exception(f"{offer.employee} must be instance of class Employee.")

        self.offers[offer.company.company_id] = offer

    def accept_offer(self, company):
        if self.company:
            raise Exception(f"{self} is already employeed in {self.company}")

        offer = self.offers.pop(company.company_id, None)
        if not offer:
            raise Exception(f"No offer was found from company {company}")

        self.company = offer.company
        self.salary = offer.salary
        self.company.employee_list.append(self)

        print(f"{self} accepted the offer from company {self.company}")

    def quit(self):
        if not self.company:
            raise Exception(f"{self} is not employeed. Can't quit.")

        print(f"{self} is quitting the job from {self.company}")

        self.company.employee_list.remove(self)
        self.company = None
        self.salary = None

    def do_work(self):
        print(f"I am working, doing {self.asset}")
        self.company.assets.append(self.asset)


class Developer(Employee):
    position = "Developer"
    asset = "develop software"


class Accountant(Employee):
    position = "Accountant"
    asset = "calculation"

    # Partial override of method
    def do_work(self):
        print("Preparing documents, will take around 1 month...")
        super().do_work()