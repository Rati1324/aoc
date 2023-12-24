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

def find_matching_digit(word, start, end):
    substr = word[start:end]
    if substr.isdigit():
        return substr

    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    matching_digits = [i for i in range(len(digits)) if substr in digits[i]]
    if not len(matching_digits):
        return False
    if any([digits[i] == substr for i in matching_digits]):
        return digits.index(substr)+1
    return False

def part_2_solution():
    result = 0
    for i in range(len(input)):
        word = input[i]
        matching_digit = False
        for start in range(len(word)):
            for end in range(start+1, len(word)+1):
                matching_digit = find_matching_digit(word, start, end)
                if matching_digit:
                    first = matching_digit
                    break
            if matching_digit:
                break

        for end in range(len(word), -1, -1):
            for start in range(end, -1, -1):
                matching_digit = find_matching_digit(word, start, end)
                if matching_digit:
                    last = matching_digit
                    break
            if matching_digit:
                break
        result += int(str(first) + str(last))
    return result

print(part_2_solution())