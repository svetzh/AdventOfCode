# Part_1

def calculate_calibration_sum(calibration_document):
    total_sum = 0

    for line in calibration_document:
        digits = [char for char in line if char.isdigit()]

        if len(digits) >= 1:
            first_digit = int(digits[0])
            last_digit = int(digits[-1])

            calibration_value = int(str(first_digit) + str(last_digit))
            total_sum += calibration_value

    return total_sum
#

def read_calibration_document(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    document = read_calibration_document("puzzle_input.txt")
    print(calculate_calibration_sum(document))

##########################################################################################
# t = 0
#
# for x in open("puzzle_input.txt"):
#     digits = [ch for ch in x if ch.isdigit()]
#     t += int(digits[0] + digits[-1])
#
# print(t)
##########################################################################################
##########################################################################################
# Part_2
import re

trebuchets = 0

n = "one two three four five six seven eight nine".split()
p = "(?=(" + "|".join(n) + "|\\d))"

def func(x):
    if x in n:
        return str(n.index(x) + 1)
    return x


for x in open("puzzle_input.txt"):
    digits = [*map(func, re.findall(p, x))]
    trebuchets += int((digits[0] + digits[-1]))

print(trebuchets)
##########################################################################################
