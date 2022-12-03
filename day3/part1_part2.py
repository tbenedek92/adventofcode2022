def set_item_priority():
    priority_dict = {}
    for i in range(97, 123):
        priority_dict[chr(i)] = i-96

    for i in range(65, 91):
        priority_dict[chr(i)] = i-38

    return priority_dict


def read_file():
    with open("input.txt" ) as f:
        infile = f.read().splitlines()
    return infile


def prioritization_part1(rucksacks, priority_dict):
    sum_priorities = 0
    for rucksack in rucksacks:
        compartment1 = rucksack[:int(len(rucksack)/2)]
        compartment2 = rucksack[-int(len(rucksack)/2):]
        item_counted_already = []
        for item in compartment1:
            if item in compartment2:
                if item not in item_counted_already:
                    sum_priorities += priority_dict[item]
                    item_counted_already.append(item)
    return sum_priorities


def part2(rucksacks, priority_dict):
    sum_priorities = 0
    for x in range(len(rucksacks))[::3]:
        group_rucksack_list = []
        group_rucksack_list.append([rucksacks[x], rucksacks[x+1], rucksacks[x+2]])
        for item in rucksacks[x]:
            if item in rucksacks[x+1]:
                if item in rucksacks[x+2]:
                    sum_priorities += priority_dict[item]
                    break
    return sum_priorities


if __name__ == '__main__':
    result_part1 = prioritization_part1(read_file(), set_item_priority())
    print(f'part1: {result_part1}')
    result_part2 = part2(read_file(), set_item_priority())
    print(f'part2: {result_part2}')
