#Advent of code day 1
#part 1
from dayone_lib import parse_input

def main():
    list_a, list_b = parse_input()
    total_dist = 0

    sorted_a = sorted(list_a)
    sorted_b = sorted(list_b)

    for i in range(len(sorted_a)):
        x = abs(sorted_a[i] - sorted_b[i])
        total_dist += x

    print(total_dist)

main()

