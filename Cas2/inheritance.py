# DRY PRINCIPLE -> DO NOT REPEAT YOUR SELF

# inheritance , inheritance by composition
# inheritance

class Animal:
    species = None

    def __init__(self, age, name):
        self.sound = None
        self.age = age
        self.name = name
        self.breathing = True

    def say_welcome(self):
        if self.breathing:
            return f"Hello from me, I am a {self.species}, yes I am breathing."
        else:
            return f"Hello from me also, I am a {self.species}, for some reason I am not breathing."

    def make_sound(self):
        return f"Hello, I am: {self.name}, and I say {self.sound}"


class Dog(Animal):
    species = "Dog"

    def __init__(self, age, name, sound):
        super().__init__(age=age, name=name)
        self.sound = sound


class Cat(Animal):
    species = "Cat"

    def __init__(self, age, name, sound):
        super().__init__(age=age, name=name)
        self.sound = sound

    # Override na methods
    def make_sound(self):
        return f"Don't bother me, I say {self.sound}"


johnny = Dog(age=30, name="Johnny", sound="Waf Waf")
marry = Cat(age=10, name="Marry", sound="Mjau")
print(marry.make_sound())