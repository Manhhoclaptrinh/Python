from models import Employee, Manager, Developer, Intern
from exceptions.employee_exceptions import (
    EmployeeNotFoundError, DuplicateEmployeeError,
    ProjectAllocationError
)


class Company:
    def __init__(self, name: str):
        self.name = name
        self._employees: list[Employee] = []

    # Thêm / Xóa
    def add_employee(self, employee: Employee):
        self._employees.append(employee)

    def remove_employee(self, employee_id: int) -> Employee:
        emp = self.find_by_id(employee_id)
        self._employees.remove(emp)
        return emp

    def mass_layoff(self, employee_ids: list[int]) -> tuple[list[Employee], list[str]]:
        """Cắt giảm nhiều nhân viên cùng lúc. Trả về (thành công, lỗi)."""
        removed, errors = [], []
        for eid in employee_ids:
            try:
                emp = self.remove_employee(eid)
                removed.append(emp)
            except EmployeeNotFoundError as e:
                errors.append(str(e))
        return removed, errors

    # Tìm kiếm
    def find_by_id(self, employee_id: int) -> Employee:
        for e in self._employees:
            if e.id == employee_id:
                return e
        raise EmployeeNotFoundError(employee_id)

    def find_by_name(self, name: str) -> list[Employee]:
        result = [e for e in self._employees if name.lower() in e.name.lower()]
        if not result:
            raise EmployeeNotFoundError(f"'{name}'")
        return result

    def find_by_language(self, lang: str) -> list[Employee]:
        return [e for e in self._employees
                if isinstance(e, Developer)
                and any(lang.lower() in l.lower() for l in e.programming_languages)]

    # Danh sách
    def get_all(self) -> list[Employee]:
        if not self._employees:
            raise IndexError("Chưa có dữ liệu nhân viên")
        return list(self._employees)

    def get_by_type(self, emp_type: str) -> list[Employee]:
        return [e for e in self._employees if e.get_type().lower() == emp_type.lower()]

    def get_sorted_by_salary(self) -> list[Employee]:
        return sorted(self._employees, key=lambda e: e.calculate_salary(), reverse=True)

    # Dự án
    def get_top_projects(self, n: int = 10, most: bool = True) -> list[Employee]:
        """Top N nhân viên tham gia nhiều/ít dự án nhất."""
        lst = [e for e in self._employees]
        lst.sort(key=lambda e: len(e.projects), reverse=most)
        return lst[:n]

    def get_members_of_project(self, project_name: str) -> list[tuple[Employee, str]]:
        """Danh sách thành viên tham gia 1 dự án kèm chức vụ."""
        result = []
        for e in self._employees:
            if project_name.lower() in [p.lower() for p in e.projects]:
                result.append((e, e.get_type()))
        return result

    # Thăng chức
    def promote(self, employee_id: int) -> tuple[Employee, Employee]:
        old = self.find_by_id(employee_id)
        if isinstance(old, Manager):
            raise ValueError(f"{old.name} đã là Manager, không thể thăng chức thêm!")

        if isinstance(old, Intern):
            new = Developer(old.name, old.salary, old.age, programming_languages=[])
        elif isinstance(old, Developer):
            new = Manager(old.name, old.salary, old.age, old.department)
        else:
            raise ValueError("Không xác định được loại nhân viên!")

        new.id = old.id
        new.performance_score = old.performance_score
        new.projects = old.projects[:]
        self._employees[self._employees.index(old)] = new
        return old, new

    def __len__(self):
        return len(self._employees)
