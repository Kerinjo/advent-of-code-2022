# every item type is identified by single lowercase or uppercase letter
# rucksack always has the same number of items in each of compartments

def split_to_compartments(string):
    compartment_length = len(string) // 2
    first_half = string[:compartment_length]
    second_half = string[compartment_length:]

    return first_half, second_half

def find_item(first, second):  # first, second are equal length strings
    # brute force is O(n^2)
    used_chars = []
    for char in first:
        if char not in used_chars:
            used_chars.append(char)
            for match in second:
                if char == match:
                    return char

with open("day-3/input") as f:

    # split to compartments and find item appearing in both
    item_list = []
    for line in f:
        first, second = split_to_compartments(line)
        item = find_item(first, second)
        item_list.append(item)

    # find item priorities
    # lowercase item types a through z have priorities 1 through 26
    # uppercase item types A through Z have priorities 27 through 52

    priorities = []
    for item in item_list:
        if item.islower():
            priorities.append( ord(item) - 96 ) # 'a' is 97, hence "- 96"
        elif item.isupper():
            priorities.append( ord(item) - 64 + 26 ) # 'A' is 65, hence "- 64", A-Z have priorities 27-52, hence "+ 26"

    # sum up the priorities
    sum_of_priorities = 0
    for elem in priorities:
        sum_of_priorities += elem

    print(sum_of_priorities)