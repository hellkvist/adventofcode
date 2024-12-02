REPORTS_FILE_PATH = "2024/2/input.txt"

def read_file_lines(file_path) -> list[list[int]]:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def get_reports():
    lines = read_file_lines(REPORTS_FILE_PATH)
    reports = []
    for line in lines:
        reports.append(
            line.split()
        )

    return reports

def is_all_increasing_minmax_diff(report: list[int]) -> bool:
    min_diff = 1
    max_diff = 3

    for i in range(len(report)-1):
        level_1 = int(report[i])
        level_2 = int(report[i+1])

        diff = level_2 - level_1

        if diff < min_diff or diff > max_diff:
            return False
        else:
            pass

    return True

def is_all_decreasing_minmax_diff(report: list[int]) -> bool:
    min_diff = 1
    max_diff = 3

    for i in range(len(report)-1):
        level_1 = int(report[i])
        level_2 = int(report[i+1])

        diff = level_1 - level_2

        if diff < min_diff or diff > max_diff:
            return False
        else:
            pass

    return True

def check_report(report: list) -> bool:
    bool1 = is_all_increasing_minmax_diff(report)
    bool2 = is_all_decreasing_minmax_diff(report)
    check = bool1 or bool2

    return check


def check_reports(reports: list[list[int]]) -> list[bool]:
    safe_bool = []

    for report in reports:
        check = check_report(report)
        safe_bool.append(check)

    return safe_bool

def check_unsafe_reports(reports):
    safe_reports = []
    for report in reports:
        check_ = []
        for i in range(len(report)):
            copy = report.copy()
            copy.pop(i)

            check = check_report(copy)
            if check:
                check_.append(True)
                break
            else:
                check_.append(False)

        safe_reports.append(any(check_))

    return safe_reports


def main():
    reports = get_reports()

    # part 1
    reports_safe_bool = check_reports(reports)

    no_safe_reports = sum(reports_safe_bool)

    print(f"Number of safe reports: {no_safe_reports}")

    unsafe_reports = [report for report, bool in zip(reports, reports_safe_bool) if not bool]

    # part 2
    reports_safe_bool_dampened = check_unsafe_reports(unsafe_reports)

    no_safe_reports_dampened = sum(reports_safe_bool_dampened)

    print(f"Number of safe reports when dampened: {no_safe_reports_dampened}")
    print(f"Total number of safe reports: {no_safe_reports + no_safe_reports_dampened}")

if __name__=='__main__':
    main()