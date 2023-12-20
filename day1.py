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

def part_2_solution():
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    result = 0
    for i in range(len(input)):
        for n in range(len(digits)):
            index = input[i].find(digits[i])
            if index != -1:
                input[i] = input[i].replace(digits[n][:-1], str(n+1))
        
        word = input[i]
        for i in range(len(word)):
            if word[i].isdigit():
                first = word[i]
                break
        for i in range(len(word) - 1, -1, -1):
            if word[i].isdigit():
                last = word[i]
                print(word, first, last)
                break
        result += int(str(first) + str(last))
    return result

print(part_2_solution())