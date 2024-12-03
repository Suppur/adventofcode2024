def parse_input():
    reports_list = []
    with open('/home/nelby/Documents/Projects/adventofcode2024/day2/input.txt') as txt:
        for line in txt:
            report = line.strip().split('\n')
            for n in report:
                tmp_list = [int(x) for x in n.split()]
            reports_list.append(tmp_list)

    return reports_list
