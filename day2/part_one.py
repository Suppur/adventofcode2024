from daytwo_lib import parse_input

safe_reports = []
safe = False

def main():
    reports_list = parse_input()
    counter = 0

    for report in reports_list:
        safe = all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))
        
        is_monotonic = sorted(report) == report or sorted(report, reverse=True) == report

        if safe and is_monotonic:
            safe_reports.append(report)

        
    for n in safe_reports:
        counter +=1

    print(counter)


main()