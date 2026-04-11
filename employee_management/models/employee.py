from abc import ABC, abstractmethod
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from exceptions.employee_exceptions import InvalidSalaryError, InvalidAgeError, ProjectAllocationError


class Employee(ABC):
    _id_counter = 1
    MAX_PROJECTS = 5

    def __init__(self, name: str, salary: float, age: int, department: str = ""):
        self._validate_salary(salary)
        self._validate_age(age)
        self.id = Employee._id_counter
        Employee._id_counter += 1
        self.name = name
        self.salary = salary
        self.age = age
        self.department = department
        self.performance_score = 0.0
        self.projects: list[str] = []

    @staticmethod
    def _validate_salary(salary):
        try:
            val = float(salary)
            if val <= 0:
                raise InvalidSalaryError(f"Lương phải là số dương, nhận được: {salary}")
        except (TypeError, ValueError):
            raise InvalidSalaryError(f"Lương không hợp lệ: {salary}")

    @staticmethod
    def _validate_age(age):
        try:
            val = int(age)
            if not 18 <= val <= 65:
                raise InvalidAgeError(f"Tuổi phải từ 18 đến 65, nhận được: {age}")
        except (TypeError, ValueError):
            raise InvalidAgeError(f"Tuổi không hợp lệ: {age}")

    @abstractmethod
    def get_type(self) -> str:
        pass

    @abstractmethod
    def calculate_salary(self) -> float:
        pass

    def add_project(self, project: str):
        if len(self.projects) >= self.MAX_PROJECTS:
            raise ProjectAllocationError(
                f"{self.name} đã có {self.MAX_PROJECTS} dự án, không thể thêm!")
        if project in self.projects:
            raise ProjectAllocationError(
                f"Nhân viên đã tham gia dự án '{project}'")
        self.projects.append(project)

    def remove_project(self, project: str):
        if project not in self.projects:
            raise ProjectAllocationError(
                f"Nhân viên không có dự án '{project}'")
        self.projects.remove(project)

    def update_performance(self, score: float):
        try:
            val = float(score)
            if not 0 <= val <= 10:
                raise ValueError(f"Điểm phải từ 0 đến 10, nhận được: {score}")
            self.performance_score = round(val, 1)
        except (TypeError, ValueError) as e:
            raise ValueError(str(e))

    def raise_salary(self, percent: float):
        if percent <= 0:
            raise InvalidSalaryError("% tăng lương phải > 0")
        self.salary = round(self.salary * (1 + percent / 100), 2)

    def __str__(self):
        return (f"[{self.get_type()}] ID={self.id} | {self.name} | Tuổi: {self.age} | "
                f"Lương CB: {self.salary}tr | HS: {self.performance_score} | "
                f"Dự án: {len(self.projects)}")
