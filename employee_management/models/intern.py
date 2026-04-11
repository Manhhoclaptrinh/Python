from .employee import Employee


class Intern(Employee):
    SALARY_COEFF = 1.0

    def __init__(self, name: str, salary: float, age: int, university: str = ""):
        super().__init__(name, salary, age)
        self.university = university

    def get_type(self) -> str:
        return "Intern"

    def calculate_salary(self) -> float:
        bonus = len(self.projects) * 0.5
        return round(self.salary * self.SALARY_COEFF + bonus, 2)

    def __str__(self):
        return super().__str__() + f" | Trường: {self.university}"
