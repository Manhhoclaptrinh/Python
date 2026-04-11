from .employee import Employee


class Manager(Employee):
    SALARY_COEFF = 1.3

    def __init__(self, name: str, salary: float, age: int, department: str = ""):
        super().__init__(name, salary, age, department)

    def get_type(self) -> str:
        return "Manager"

    def calculate_salary(self) -> float:
        bonus = len(self.projects) * 0.5
        return round(self.salary * self.SALARY_COEFF + bonus, 2)

    def __str__(self):
        return super().__str__() + f" | Phòng: {self.department}"
