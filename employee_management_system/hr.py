class Shift:
    EARLY_MORNING = "early_morning"
    DAY = "day"
    LATE_NIGHT = "late_night"

    SHIFT_PAY_RATES = {
        EARLY_MORNING: 1.0,
        DAY: 1.0,
        LATE_NIGHT: 1.2,
    }

    @staticmethod
    def get_shift_pay_rate(shift):
        return Shift.SHIFT_PAY_RATES.get(shift, 1.0)


class PayrollPolicy:
    def __init__(self):
        self.hours_worked = 0

    def track_work(self, hours):
        self.hours_worked += hours


class SalaryPolicy(PayrollPolicy):
    def __init__(self, annual_salary):
        super().__init__()
        self.annual_salary = annual_salary

    def calculate_payroll(self):
        return self.annual_salary / 52


class HourlyPolicy(PayrollPolicy):
    def __init__(self, hour_rate, shift):
        super().__init__()
        self.hour_rate = hour_rate
        self.shift = shift

    def calculate_payroll(self):
        shift_pay_rate = Shift.get_shift_pay_rate(self.shift)
        return self.hours_worked * self.hour_rate * shift_pay_rate


class PayrollSystem:
    def __init__(self):
        self._employee_policies = {
            "general_manager": SalaryPolicy(52000),
            "shift_leader_early_morning": HourlyPolicy(18, Shift.EARLY_MORNING),
            "shift_leader_day": HourlyPolicy(18, Shift.DAY),
            "shift_leader_late_night": HourlyPolicy(18, Shift.LATE_NIGHT),
            "crew_member_early_morning": HourlyPolicy(15, Shift.EARLY_MORNING),
            "crew_member_day": HourlyPolicy(15, Shift.DAY),
            "crew_member_late_night": HourlyPolicy(15, Shift.LATE_NIGHT),
            "team_member_early_morning": HourlyPolicy(15, Shift.EARLY_MORNING),
            "team_member_day": HourlyPolicy(15, Shift.DAY),
            "team_member_late_night": HourlyPolicy(15, Shift.LATE_NIGHT),
            "custodial_early_morning": HourlyPolicy(12, Shift.EARLY_MORNING),
            "custodial_day": HourlyPolicy(12, Shift.DAY),
            "custodial_late_night": HourlyPolicy(12, Shift.LATE_NIGHT),
        }

    def get_policy(self, role, shift):
        if "general_manager" in role:
            return self._employee_policies["general_manager"]

        policy_key = f"{role}_{shift}"
        policy = self._employee_policies.get(policy_key)
        if not policy:
            raise ValueError(f"No pay policy found for role {policy_key}")
        return policy

    def calculate_payroll(self, employees):
        print("Calculating Payroll")
        print("===================")
        for employee in employees:
            print(f"Payroll for: {employee.id} - {employee.name}")
            print(f"- Check amount: {employee.calculate_payroll()}")
            print("- Sent to:")
            print(employee.address)
            print("")
