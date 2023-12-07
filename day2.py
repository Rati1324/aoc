input = open("input2.txt", "r").read().split("\n")

def solution():
    # combinations = {"red": 12, "green": 13, "blue": 14}
    print(input)
    for game in input:
        colors = {"r": 0, "g": 0, "b": 0}
        for i in range(6, len(game)):
            if game[i].isdigit():
                colors[game[i+1]] = i
    print(colors)

solution()