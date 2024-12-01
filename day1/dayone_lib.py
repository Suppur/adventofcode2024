

def parse_input():
    list_a = []
    list_b = []
    with open('input.txt', 'r') as txt:
        for line in txt:
            nums = line.strip().split()
            list_a.append(int(nums[0]))
            list_b.append(int(nums[1]))

    return list_a, list_b