class Address:
    def __init__(self, street, city, state, zipcode, street2=""):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f"{self.city}, {self.state} {self.zipcode}")
        return "\n".join(lines)


class AddressBook:
    def __init__(self):
        self._employee_addresses = {
            1: Address("121 Admin Rd.", "Concord", "NH", "03301"),
            2: Address("67 Paperwork Ave", "Manchester", "NH", "03101"),
            3: Address("15 Rose St", "Concord", "NH", "03301"),
            4: Address("39 Sole St.", "Concord", "NH", "03301"),
            5: Address("99 Mountain Rd.", "Concord", "NH", "03301"),
            6: Address("82 Cedar Ln.", "Concord", "NH", "03301"),
            7: Address("14 Maple Dr.", "Concord", "NH", "03302"),
            8: Address("56 Oak St.", "Concord", "NH", "03303"),
            9: Address("230 Elm St.", "Concord", "NH", "03301"),
            10: Address("98 Pine St.", "Concord", "NH", "03301"),
            11: Address("112 Birch Rd.", "Concord", "NH", "03301"),
            12: Address("476 Spruce Way", "Concord", "NH", "03302"),
            13: Address("789 Willow St.", "Concord", "NH", "03303"),
            14: Address("321 Poplar Ave.", "Concord", "NH", "03301"),
            15: Address("654 Cherry Blvd.", "Concord", "NH", "03301"),
        }

    def get_employee_address(self, employee_id):
        address = self._employee_addresses.get(employee_id)
        if not address:
            raise ValueError(employee_id)
        return address
