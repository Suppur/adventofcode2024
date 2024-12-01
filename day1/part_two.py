#Advent of code day1 part 2!
from dayone_lib import parse_input

def main():
    list_a, list_b = parse_input()
    dic = {}
    result = 0

    for n in list_b:
        if n not in dic:
            dic[n] = 1
        else:
            dic[n] += 1

    for i in range(len(list_a)):
        if list_a[i] not in dic:
            pass
        else:
            result += list_a[i] * dic[list_a[i]]

    print(result)

main()
