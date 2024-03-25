from Vehicle import Vehicle


class Bicycle(Vehicle):
    def __init__(self, id, make, model, year):
        super().__init__(id, make, model, year)

    def __str__(self):
        return f"{super().__str__()}"
