import re
input = open("input.txt", "r").read().split("\n")

def solution():
    res = 0
    color_limits = {"r": 12, "g": 13, "b": 14}
    for game in input:
        numbers = re.findall(r'(\d+\s\w|\d+:)', game)
        game_id = int(numbers[0][:-1])
        good = True
        for i in numbers[1:]:
            i = i.split()
            color = i[1]
            amount = int(i[0])
            if amount > color_limits[color]:
                good = False
                break
        if good:
            res += game_id
    return res

def solution_part_2():
    res = 0
    for game in input:
        numbers = re.findall(r'(\d+\s\w|\d+:)', game)
        good = True
        amount_max = {"r": 0, "g": 0, "b": 0}
        for i in numbers[1:]:
            i = i.split()
            color = i[1]
            amount = int(i[0])
            if amount > amount_max[color]:
                amount_max[color] = amount
        res += amount_max["r"] * amount_max["g"] * amount_max["b"]
    return res
print(solution_part_2())