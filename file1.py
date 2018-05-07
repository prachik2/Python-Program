class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age

    def show_age(self):
        return self._get_age()

    def _get_age(self):
        return self._age

    def show_name(self):
        return self.get_name()

    def get_name(self):
        return self.first_name

tk = Person('TK', 25)
print(tk.show_age()) # => 25
print(tk.show_name())
