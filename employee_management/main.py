import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from models import Manager, Developer, Intern
from services import Company, Payroll
from utils import (validate_salary, validate_score, validate_name,
                   print_table, print_header, print_msg, print_separator)
from utils.validators import validate_age, validate_int_menu
from exceptions import (
    EmployeeNotFoundError, InvalidSalaryError, InvalidAgeError,
    ProjectAllocationError, DuplicateEmployeeError, EmployeeException
)

company = Company("ABC")

def menu_them():
    print_header("1. Thêm nhân viên mới")
    print("  a. Thêm Manager")
    print("  b. Thêm Developer")
    print("  c. Thêm Intern")

    try:
        ch = validate_int_menu(input("\n  Chọn (a/b/c): "), ['a', 'b', 'c'])
        name = validate_name(input("  Họ tên: "))
        salary = validate_salary(input("  Lương cơ bản (triệu): "))
        age = validate_age(input("  Tuổi (18-65): "))

        if ch == 'a':
            dept = input("  Phòng ban: ").strip()
            emp = Manager(name, salary, age, dept)
        elif ch == 'b':
            dept = input("  Phòng ban: ").strip()
            langs = [l.strip() for l in input("  Ngôn ngữ lập trình (phân cách bằng dấu phẩy): ").split(",") if l.strip()]
            emp = Developer(name, salary, age, dept, langs)
        else:
            univ = input("  Trường đại học: ").strip()
            emp = Intern(name, salary, age, univ)

        company.add_employee(emp)
        print_msg(f"Đã thêm {emp.get_type()}: {emp.name} (ID: {emp.id})", "success")

    except (InvalidSalaryError, InvalidAgeError, ValueError, EmployeeException) as e:
        print_msg(str(e), "error")


def menu_hien():
    print_header("2. Hiển thị danh sách nhân viên")
    print("  a. Tất cả nhân viên")
    print("  b. Theo loại (Manager/Developer/Intern)")
    print("  c. Theo hiệu suất (từ cao đến thấp)")

    try:
        ch = input("\n  Chọn (a/b/c): ").strip().lower()
        if ch == 'a':
            print_header("Tất cả nhân viên")
            print_table(company.get_all())
        elif ch == 'b':
            loai = input("  Loại (Manager/Developer/Intern): ").strip()
            lst = company.get_by_type(loai)
            print_header(f"Danh sách {loai}")
            print_table(lst)
        elif ch == 'c':
            lst = sorted(company.get_all(), key=lambda e: e.performance_score, reverse=True)
            print_header("Theo hiệu suất (cao → thấp)")
            print_table(lst)
        else:
            print_msg("Lựa chọn không hợp lệ!", "error")
    except IndexError as e:
        print_msg(str(e), "error")


def menu_tim():
    print_header("3. Tìm kiếm nhân viên")
    print("  a. Theo ID")
    print("  b. Theo tên")
    print("  c. Theo ngôn ngữ lập trình (Developer)")

    try:
        ch = input("\n  Chọn (a/b/c): ").strip().lower()
        if ch == 'a':
            eid = int(input("  Nhập ID: "))
            emp = company.find_by_id(eid)
            print_separator()
            print(f"  {emp}")
            print_separator()
        elif ch == 'b':
            name = input("  Nhập tên: ").strip()
            lst = company.find_by_name(name)
            print_header(f"Kết quả tìm '{name}'")
            print_table(lst)
        elif ch == 'c':
            lang = input("  Ngôn ngữ lập trình: ").strip()
            lst = company.find_by_language(lang)
            print_header(f"Developer biết '{lang}'")
            print_table(lst)
        else:
            print_msg("Lựa chọn không hợp lệ!", "error")
    except (EmployeeNotFoundError, ValueError) as e:
        print_msg(str(e), "error")


def menu_luong():
    print_header("4. Quản lý lương")
    print("  a. Tính lương cho từng nhân viên")
    print("  b. Tính tổng lương công ty")
    print("  c. Top 3 nhân viên lương cao nhất")

    try:
        ch = input("\n  Chọn (a/b/c): ").strip().lower()
        if ch == 'a':
            print_header("Bảng lương nhân viên")
            print_table(company.get_all(), show_salary=True)
        elif ch == 'b':
            total = Payroll.total_salary(company.get_all())
            print_separator()
            print_msg(f"Tổng lương công ty: {total} triệu đồng", "info")
            by_dept = Payroll.salary_by_department(company.get_all())
            print("\n  Theo phòng ban:")
            for dept, sal in by_dept.items():
                print(f"    • {dept}: {sal}tr")
            print_separator()
        elif ch == 'c':
            top3 = Payroll.top_n_salary(company.get_all(), 3)
            print_header("Top 3 lương cao nhất")
            for i, e in enumerate(top3, 1):
                print(f"  {i}. {e.name} ({e.get_type()}) — Thực lĩnh: {e.calculate_salary()}tr")
        else:
            print_msg("Lựa chọn không hợp lệ!", "error")
    except IndexError as e:
        print_msg(str(e), "error")


def menu_du_an():
    print_header("5. Quản lý dự án")
    print("  a. Phân công nhân viên vào dự án")
    print("  b. Xóa nhân viên khỏi dự án")
    print("  c. Hiển thị dự án của 1 nhân viên")
    print("  d. Top 10 nhân viên tham gia nhiều dự án nhất")
    print("  e. Top 10 nhân viên tham gia ít dự án nhất")
    print("  f. Danh sách thành viên tham gia 1 dự án và chức vụ")

    try:
        ch = input("\n  Chọn (a-f): ").strip().lower()

        if ch in ('a', 'b', 'c'):
            eid = int(input("  ID nhân viên: "))
            emp = company.find_by_id(eid)
            if ch == 'a':
                proj = input("  Tên dự án: ").strip()
                emp.add_project(proj)
                print_msg(f"Đã phân công {emp.name} vào dự án '{proj}'", "success")
            elif ch == 'b':
                proj = input("  Tên dự án cần xóa: ").strip()
                emp.remove_project(proj)
                print_msg(f"Đã xóa {emp.name} khỏi dự án '{proj}'", "success")
            elif ch == 'c':
                projs = ", ".join(emp.projects) if emp.projects else "(chưa có dự án)"
                print_separator()
                print(f"  {emp.name}: {projs}")
                print_separator()

        elif ch == 'd':
            lst = company.get_top_projects(10, most=True)
            print_header("Top 10 tham gia nhiều dự án nhất")
            _print_project_rank(lst)

        elif ch == 'e':
            lst = company.get_top_projects(10, most=False)
            print_header("Top 10 tham gia ít dự án nhất")
            _print_project_rank(lst)

        elif ch == 'f':
            proj = input("  Tên dự án: ").strip()
            members = company.get_members_of_project(proj)
            print_header(f"Thành viên dự án '{proj}'")
            if not members:
                print_msg("Không có nhân viên nào trong dự án này!", "error")
            else:
                print(f"  {'ID':<6} {'Họ tên':<22} {'Chức vụ':<14}")
                print("  " + "-" * 44)
                for emp, role in members:
                    print(f"  {emp.id:<6} {emp.name:<22} {role:<14}")
        else:
            print_msg("Lựa chọn không hợp lệ!", "error")

    except (EmployeeNotFoundError, ProjectAllocationError, ValueError) as e:
        print_msg(str(e), "error")


def _print_project_rank(lst):
    print(f"  {'#':<4} {'ID':<6} {'Họ tên':<22} {'Loại':<12} {'Số dự án':>8}")
    print("  " + "-" * 55)
    for i, e in enumerate(lst, 1):
        print(f"  {i:<4} {e.id:<6} {e.name:<22} {e.get_type():<12} {len(e.projects):>8}")


def menu_hieu_suat():
    print_header("6. Đánh giá hiệu suất")
    print("  a. Cập nhật điểm hiệu suất")
    print("  b. Nhân viên xuất sắc (điểm > 8)")
    print("  c. Nhân viên cần cải thiện (điểm < 5)")

    try:
        ch = input("\n  Chọn (a/b/c): ").strip().lower()
        if ch == 'a':
            eid = int(input("  ID nhân viên: "))
            emp = company.find_by_id(eid)
            score = validate_score(input("  Điểm hiệu suất (0-10): "))
            emp.update_performance(score)
            print_msg(f"Đã cập nhật điểm cho {emp.name}: {score}", "success")
        elif ch == 'b':
            lst = [e for e in company._employees if e.performance_score > 8]
            print_header("Nhân viên xuất sắc (điểm > 8)")
            print_table(lst)
        elif ch == 'c':
            lst = [e for e in company._employees if 0 < e.performance_score < 5]
            print_header("Nhân viên cần cải thiện (điểm < 5)")
            print_table(lst)
        else:
            print_msg("Lựa chọn không hợp lệ!", "error")
    except (EmployeeNotFoundError, ValueError) as e:
        print_msg(str(e), "error")


def menu_nhan_su():
    print_header("7. Quản lý nhân sự")
    print("  a. Xóa nhân viên (nghỉ việc)")
    print("  b. Tăng lương cơ bản")
    print("  c. Thăng chức (Intern → Developer → Manager)")
    print("  d. Cắt giảm nhân sự (cho nghỉ việc nhiều nhân viên)")

    try:
        ch = input("\n  Chọn (a/b/c/d): ").strip().lower()

        if ch == 'a':
            eid = int(input("  ID nhân viên: "))
            emp = company.remove_employee(eid)
            print_msg(f"Đã xóa nhân viên: {emp.name} (ID: {emp.id})", "success")

        elif ch == 'b':
            eid = int(input("  ID nhân viên: "))
            emp = company.find_by_id(eid)
            pct = float(input("  % tăng lương: "))
            old = emp.salary
            emp.raise_salary(pct)
            print_msg(f"{emp.name}: {old}tr → {emp.salary}tr (+{pct}%)", "success")

        elif ch == 'c':
            eid = int(input("  ID nhân viên: "))
            old, new = company.promote(eid)
            print_msg(f"{old.name}: {old.get_type()} → {new.get_type()}", "success")

        elif ch == 'd':
            raw = input("  Nhập danh sách ID cần cho nghỉ việc (cách nhau bằng dấu phẩy): ")
            try:
                ids = [int(x.strip()) for x in raw.split(',') if x.strip()]
            except ValueError:
                print_msg("ID không hợp lệ, vui lòng nhập số!", "error")
                return
            if not ids:
                print_msg("Không có ID nào được nhập!", "error")
                return

            confirm = input(f"  Xác nhận cho nghỉ việc {len(ids)} nhân viên? (y/n): ").strip().lower()
            if confirm != 'y':
                print_msg("Đã hủy thao tác.", "info")
                return

            removed, errors = company.mass_layoff(ids)
            print_separator()
            if removed:
                print_msg(f"Đã cho nghỉ việc {len(removed)} nhân viên:", "success")
                for emp in removed:
                    print(f"    • [{emp.id}] {emp.name} ({emp.get_type()})")
            if errors:
                print_msg(f"Có {len(errors)} lỗi:", "error")
                for err in errors:
                    print(f"    • {err}")
            print_separator()
        else:
            print_msg("Lựa chọn không hợp lệ!", "error")

    except (EmployeeNotFoundError, InvalidSalaryError, ValueError, EmployeeException) as e:
        print_msg(str(e), "error")

def menu_bao_cao():
    print_header("8. Thống kê báo cáo")
    try:
        all_emp = company.get_all()

        print("\n  a. Số lượng nhân viên theo loại:")
        for t in ["Manager", "Developer", "Intern"]:
            count = len(company.get_by_type(t))
            print(f"    • {t}: {count} người")

        print("\n  b. Tổng lương theo phòng ban:")
        by_dept = Payroll.salary_by_department(all_emp)
        for dept, sal in by_dept.items():
            print(f"    • {dept}: {sal}tr")

        avg_proj = sum(len(e.projects) for e in all_emp) / len(all_emp)
        print(f"\n  c. Số dự án trung bình / nhân viên: {avg_proj:.1f}")
        print_separator()
    except IndexError as e:
        print_msg(str(e), "error")


def print_main_menu():
    print_separator()
    print(f"  HỆ THỐNG QUẢN LÝ NHÂN VIÊN CÔNG TY {company.name.upper()}")
    print_separator()
    print("  1. Thêm nhân viên mới")
    print("  2. Hiển thị danh sách nhân viên")
    print("  3. Tìm kiếm nhân viên")
    print("  4. Quản lý lương")
    print("  5. Quản lý dự án")
    print("  6. Đánh giá hiệu suất")
    print("  7. Quản lý nhân sự")
    print("  8. Thống kê báo cáo")
    print("  9. Thoát")
    print_separator()


def main():
    MENU = {
        '1': menu_them,
        '2': menu_hien,
        '3': menu_tim,
        '4': menu_luong,
        '5': menu_du_an,
        '6': menu_hieu_suat,
        '7': menu_nhan_su,
        '8': menu_bao_cao,
    }

    while True:
        print_main_menu()
        try:
            choice = input("  Chọn chức năng (1-9): ").strip()
        except (EOFError, KeyboardInterrupt):
            print_msg("\nTạm biệt!", "info")
            break

        if choice == '9':
            print_msg("Tạm biệt!", "info")
            break
        elif choice in MENU:
            print()
            MENU[choice]()
        else:
            print_msg("Vui lòng chọn từ 1 đến 9!", "error")

        try:
            input("\n  [Enter để tiếp tục...]")
        except (EOFError, KeyboardInterrupt):
            break


if __name__ == "__main__":
    main()
