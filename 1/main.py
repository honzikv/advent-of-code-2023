import re

valid_digit_strings = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
digit_strings_to_numbers = {
    digit_string: str(index + 1)
    for index, digit_string in enumerate(valid_digit_strings)
}
digit_regex = "\d|" + "|".join(valid_digit_strings)
reversed_regex = "\d|" + "|".join([num[::-1] for num in valid_digit_strings])


def get_line_code(line: str):
    first_occurrence = re.search(rf"{digit_regex}", line).group()
    last_occurrence = re.search(rf"{reversed_regex}", line[::-1]).group()[::-1]

    if first_occurrence in digit_strings_to_numbers:
        first_occurrence = digit_strings_to_numbers[first_occurrence]
    if last_occurrence in digit_strings_to_numbers:
        last_occurrence = digit_strings_to_numbers[last_occurrence]

    number = f"{first_occurrence}{last_occurrence}"
    return int(number)


total = 0
with open("1/input.txt") as f:
    for line in f:
        total += get_line_code(line)

print(total)
