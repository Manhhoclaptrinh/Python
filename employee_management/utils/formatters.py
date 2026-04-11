def print_separator():
    print("=" * 65)

def print_header(title: str):
    print_separator()
    print(f"  {title.upper()}")
    print_separator()

def print_msg(msg: str, kind: str = "info"):
    icons = {"success": "✓", "error": "✗", "info": "→", "warn": "!"}
    print(f"  [{icons.get(kind, '·')}] {msg}")

def print_table(employees, show_salary=False):
    if not employees:
        print("  (Không có nhân viên)")
        return
    header = f"  {'ID':<5} {'Họ tên':<20} {'Loại':<12} {'Lương CB':>9}"
    if show_salary:
        header += f" {'Thực lĩnh':>10}"
    header += f" {'HS':>5} {'Dự án':>6}"
    print(header)
    print("  " + "-" * 62)
    for e in employees:
        row = f"  {e.id:<5} {e.name:<20} {e.get_type():<12} {e.salary:>8.1f}tr"
        if show_salary:
            row += f" {e.calculate_salary():>9.1f}tr"
        row += f" {e.performance_score:>5.1f} {len(e.projects):>5}"
        print(row)
