import json

from employee_company.employee import Developer, Accountant
from employee_company.company import Company

semos = Company("Semos Edukacija", "Kuzman Josifovski Pitu br. 1000", "1234")
seavus = Company("Seavus AD", "Boris Trajkovski br. 60", "9876")

# marija = Employee("Marija", "Krstevska", "marija@gmail.com", "2"*13)
kristijan = Developer("Kristijan", "Gjorgiev", "kristijan@gmail.com", "3"*13)
jovan = Accountant("Jovan", "Jankov", "jovan@yahoo.com", "4"*13)

semos.make_offer(kristijan, salary=50000)
kristijan.accept_offer(semos)
semos.make_offer(jovan, 40000)
jovan.accept_offer(semos)

jovan.do_work()
kristijan.do_work()
print(semos.assets)
# marija_serialized = marija.serialize()

# dictionary to string/text
# marija_text = json.dumps(marija_serialized)
#
# clone_marija = json.loads(marija_text)
# print(type(clone_marija))
# print(clone_marija)
# file descriptor / handle

# context managers
# with open("object_serialized.json", "w") as f:
#     f.write(json.dumps(marija_serialized))
# print("Completed")
# semos.make_offer(kristijan, 50000, "Python Developer")
#
# kristijan.accept_offer(semos)
# kristijan.quit()
# kristijan.quit()

# print(Employee.validate_embg("3"*12))

### DESERIALIZATION ###

# with open("object_serialized.json", "r") as f:
#     data = json.loads(f.read())
#     marija = Employee(
#         first_name=data.get("first_name"),
#         last_name=data.get("last_name"),
#         email=data.get("email"),
#         embg=data.get("embg")
#     )
#
#     marija.deserialize_object(
#         salary=data.get("salary"),
#         position=data.get("position"),
#         company=data.get("company"),
#         offers=data.get("offers")
#     )
#
# print(marija)
# print(marija.__dict__)
#
#














# semos.hire(jovan, "Developer", 14999)
# print(semos.employee_list)

# print(isinstance(jovan, Company))
#
# class A:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __eq__(self, other):
#         if self.a == other.a and self.b == other.b:
#             return True
#
#         return False
#
# obj1 = A("Hello", 100)
# obj2 = A("Hello", 100)
#
# print(obj1 == obj2)