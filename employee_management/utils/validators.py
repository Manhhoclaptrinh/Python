from exceptions.employee_exceptions import InvalidSalaryError, InvalidAgeError


def validate_salary(s: str) -> float:
    try:
        val = float(s)
        if val <= 0:
            raise InvalidSalaryError(f"Lương phải là số dương, nhận được: {s}")
        return val
    except ValueError:
        raise InvalidSalaryError(f"Lương không hợp lệ: {s}")


def validate_age(s: str) -> int:
    try:
        val = int(s)
        if not 18 <= val <= 65:
            raise InvalidAgeError(f"Tuổi phải từ 18 đến 65, nhận được: {s}")
        return val
    except ValueError:
        raise InvalidAgeError(f"Tuổi không hợp lệ: {s}")


def validate_score(s: str) -> float:
    try:
        val = float(s)
        if not 0 <= val <= 10:
            raise ValueError(f"Điểm phải từ 0 đến 10, nhận được: {s}")
        return val
    except ValueError:
        raise ValueError(f"Điểm không hợp lệ: {s}")


def validate_name(s: str) -> str:
    name = s.strip()
    if not name:
        raise ValueError("Tên không được để trống!")
    return name


def validate_int_menu(s: str, valid: list[str]) -> str:
    s = s.strip()
    if s not in valid:
        raise ValueError(f"Vui lòng chọn một trong: {', '.join(valid)}")
    return s
