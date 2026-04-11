from models import Employee


class Payroll:
    @staticmethod
    def total_salary(employees: list[Employee]) -> float:
        return round(sum(e.calculate_salary() for e in employees), 2)

    @staticmethod
    def top_n_salary(employees: list[Employee], n: int = 3) -> list[Employee]:
        return sorted(employees, key=lambda e: e.calculate_salary(), reverse=True)[:n]

    @staticmethod
    def salary_by_department(employees: list[Employee]) -> dict[str, float]:
        result: dict[str, float] = {}
        for e in employees:
            dept = getattr(e, 'department', '') or 'Không xác định'
            result[dept] = round(result.get(dept, 0) + e.calculate_salary(), 2)
        return result
