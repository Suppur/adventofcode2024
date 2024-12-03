from daytwo_lib import parse_input

safe_reports = []
safe = False

def main():
    reports_list = parse_input()
    counter = 0

    for report in reports_list:
        for i in range(len(report)):
            modified_report = report[:i] + report[i+1:]
            safe = all(1 <= abs(modified_report[i] - modified_report[i + 1]) <= 3 for i in range(len(modified_report) - 1))
            
            is_monotonic = sorted(modified_report) == modified_report or sorted(modified_report, reverse=True) == modified_report

            if safe and is_monotonic:
                safe_reports.append(modified_report)
                break
        
    for n in safe_reports:
        counter +=1

    print(counter)


main()