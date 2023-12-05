######################################## Part_1 ##################################################
RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14

ids_sum = 0
for game_id, game_line in enumerate(open("puzzle_input.txt")):
    game_info = game_line.strip().split(": ")[1].split("; ")
    for group in game_info:
        mapper = {"red": 0, "green": 0, "blue": 0}
        for el in group.split(", "):
            num, color = el.split()
            mapper[color] = int(num)
        if mapper["red"] > RED_LIMIT or mapper["green"] > GREEN_LIMIT or mapper["blue"] > BLUE_LIMIT:
            break
    else:
        ids_sum += game_id + 1

print(ids_sum)


######################################## Part_2 ##################################################
answer = 0
for game_id, game_line in enumerate(open("puzzle_input.txt")):
    game_info = game_line.strip().split(": ")[1].split("; ")

    r, g, b = 0, 0, 0

    for group in game_info:
        mapper = {"red": 0, "green": 0, "blue": 0}

        for el in group.split(", "):
            num, color = el.split()
            m = int(num)

            if color == "red":
                r = max(m, r)
            if color == "green":
                g = max(m, g)
            if color == "blue":
                b = max(m, b)

    answer += r * g * b

print(answer)