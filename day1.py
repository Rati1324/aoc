input = open("input.txt", "r").read().split("\n")

def solution():
    sum = 0
    first = 1
    first_num = ''
    last_num = ''
    for i in input:
        first = 1
        for j in i:
            if j.isdigit():
                if first:
                    first_num = j
                    first = 0
                last_num = j
        sum += int(first_num + last_num)
    return int(sum)

print(solution())