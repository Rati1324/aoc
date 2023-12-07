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

def solution2():
    sum = 0

    for word in input:
        for char in word:
            if char.isdigit():
                first_num = char
                break
        for char in word[::-1]:
            if char.isdigit():
                last_num = char
                break
        sum += int(first_num+last_num)
    return sum
print(solution2())