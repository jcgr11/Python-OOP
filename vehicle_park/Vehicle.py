class Vehicle:
    all_vehicles = []

    def __init__(self, id, make, model, year):
        self._id = id
        self._make = make
        self._model = model
        self._year = year
        Vehicle.all_vehicles.append(self)

    @property
    def id(self):
        return self._id

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

    def __str__(self):
        return (
            "ID: "
            + self._id
            + "\nMake: "
            + self._make
            + "\nModel: "
            + self._model
            + "\nYear: "
            + self._year
        )
