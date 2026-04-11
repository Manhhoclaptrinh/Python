from .employee import Employee


class Developer(Employee):
    SALARY_COEFF = 1.15

    def __init__(self, name: str, salary: float, age: int, department: str = "",
                 programming_languages: list[str] = None):
        super().__init__(name, salary, age, department)
        self.programming_languages = programming_languages or []

    def get_type(self) -> str:
        return "Developer"

    def calculate_salary(self) -> float:
        bonus = len(self.projects) * 0.5
        return round(self.salary * self.SALARY_COEFF + bonus, 2)

    def __str__(self):
        langs = ", ".join(self.programming_languages) if self.programming_languages else "N/A"
        return super().__str__() + f" | Ngôn ngữ: {langs}"
