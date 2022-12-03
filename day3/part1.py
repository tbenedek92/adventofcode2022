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


def prioritization(rucksacks, priority_dict):
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


if __name__ == '__main__':
    result = prioritization(read_file(), set_item_priority())
    print(result)
