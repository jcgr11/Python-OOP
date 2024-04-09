from productivity import ProductivitySystem
from hr import PayrollSystem, Shift
from contacts import AddressBook


class Employee:
    def __init__(self, id, name, address, role, payroll_policy, shift):
        self.id = id
        self.name = name
        self.address = address
        self.role = role
        self.payroll_policy = payroll_policy
        self.shift = shift

    def work(self, hours):
        duties = self.role.perform_duties(hours)
        shift_name = self.get_shift_name()
        print(f"Employee {self.id} - {self.name} ({shift_name} Shift):")
        print(f"- {duties}")
        print("")
        self.payroll_policy.track_work(hours)

    def get_shift_name(self):
        shift_names = {
            Shift.EARLY_MORNING: "Early Morning",
            Shift.DAY: "Day",
            Shift.LATE_NIGHT: "Late Night",
        }

        return shift_names.get(self.shift, "Unknown")

    def calculate_payroll(self):
        return self.payroll_policy.calculate_payroll()


class ShiftCrew:
    def __init__(self, shift_name):
        self.shift_name = shift_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)


class EmployeeDatabase:
    def __init__(self):
        self.productivity_system = ProductivitySystem()
        self.payroll_system = PayrollSystem()
        self.address_book = AddressBook()
        self._employees = {
            # General Manager
            1: {"name": "Mary Poppins", "role": "general_manager", "shift": Shift.DAY},
            # Shift Leaders
            2: {
                "name": "John Day",
                "role": "shift_leader",
                "shift": Shift.EARLY_MORNING,
            },
            3: {"name": "Jane Morning", "role": "shift_leader", "shift": Shift.DAY},
            4: {
                "name": "Jack Night",
                "role": "shift_leader",
                "shift": Shift.LATE_NIGHT,
            },
            # Crew Members
            5: {
                "name": "Steve Day",
                "role": "crew_member",
                "shift": Shift.EARLY_MORNING,
            },
            6: {"name": "Lucy Morning", "role": "crew_member", "shift": Shift.DAY},
            7: {"name": "Dave Night", "role": "crew_member", "shift": Shift.LATE_NIGHT},
            # Team Members
            8: {
                "name": "Mike Day",
                "role": "team_member",
                "shift": Shift.EARLY_MORNING,
            },
            9: {"name": "Sara Morning", "role": "team_member", "shift": Shift.DAY},
            10: {
                "name": "Ryan Night",
                "role": "team_member",
                "shift": Shift.LATE_NIGHT,
            },
            # Custodial Staff
            11: {
                "name": "Chris Day",
                "role": "custodial",
                "shift": Shift.EARLY_MORNING,
            },
            12: {"name": "Emma Morning", "role": "custodial", "shift": Shift.DAY},
            13: {
                "name": "Olivia Night",
                "role": "custodial",
                "shift": Shift.LATE_NIGHT,
            },
        }

    def get_employee_info(self, employee_id):
        employee_info = self._employees.get(employee_id)
        if not employee_info:
            raise ValueError(f"No employee found with id {employee_id}")
        return employee_info

    def get_employee(self, employee_id):
        employee_info = self.get_employee_info(employee_id)
        name = employee_info["name"]
        role_name = employee_info["role"]
        shift = employee_info["shift"]

        address = self.address_book.get_employee_address(employee_id)
        role = self.productivity_system.get_role(role_name)
        payroll_policy = self.payroll_system.get_policy(role_name, shift)

        return Employee(employee_id, name, address, role, payroll_policy, shift)

    @property
    def employees(self):
        return [self.get_employee(emp_id) for emp_id in sorted(self._employees)]
