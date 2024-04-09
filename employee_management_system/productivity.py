class ProductivitySystem:
    def __init__(self):
        self._roles = {
            "general_manager": GeneralManagerRole(),
            "shift_leader": ShiftLeaderRole(),
            "crew_member": CrewMemberRole(),
            "team_member": TeamMemberRole(),
            "custodial": CustodialRole(),
        }

    def get_role(self, role_id):
        role_instance = self._roles.get(role_id)
        if not role_instance:
            raise ValueError(f"No role found for role_id {role_id}")
        return role_instance

    def track(self, employee, hours):
        print("Tracking Employee Productivity")
        print("==============================")
        result = employee.role.perform_duties(hours)
        print(f"{employee.name}: {result}")
        print("")


class GeneralManagerRole:
    def perform_duties(self, hours):
        return f"manages the restaurant."


class ShiftLeaderRole:
    def perform_duties(self, hours):
        return f"oversees the shift."


class CrewMemberRole:
    def perform_duties(self, hours):
        return f"prepares food, bags meals, passes orders to the 'Team member', and serves customers."


class TeamMemberRole:
    def perform_duties(self, hours):
        return f"assists in various task. Drive thru, front counter, and kitchen."


class CustodialRole:
    def perform_duties(self, hours):
        return f"cleans the restaurant as needed."
