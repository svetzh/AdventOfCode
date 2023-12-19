#Part_1
# with open("engine_puzzle_input.txt", "r") as file_input:
#     grid = file_input.read()
#     lines = grid.splitlines()
#
# nums = []
# str_nums = ''
#
#
# for ch in grid:
#     if ch.isdigit():
#         str_nums += ch
#
#     elif str_nums:
#         nums.append(int(str_nums))
#         str_nums = ''
#
# if str_nums:
#     nums.append(int(str_nums))
#
# print(nums)

##########################################################################################
with open("engine_puzzle_input.txt", "r") as file_input:
    grid = file_input.read().splitlines()

containing_sets = set()

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch.isdigit() or ch ==".":
            continue
        for crr_row in [r-1, r, r+1]:
            for curr_col in [c-1, c, c+1]:
                if (crr_row < 0 or crr_row > len(grid) or
                        curr_col < 0 or curr_col > len(grid[crr_row]) or not
                        grid[crr_row][curr_col].isdigit()
                ):
                    continue

                while curr_col > 0 and grid[crr_row][curr_col - 1].isdigit():
                    curr_col -= 1
                containing_sets.add((crr_row, curr_col))

numbers = []

for r, c in containing_sets:
    s = ""
    while c < len(grid[r]) and grid[r][c].isdigit():
        s += grid[r][c]
        c += 1
    numbers.append(int(s))

print(sum(numbers))




##########################################################################################

#Part_2




