def get_range(range_str):
    range_min, range_max = range_str.split('-')
    range_min, range_max = [int(range_min), int(range_max)]
    if range_min == range_max:
        return {range_min}
    return set(range(range_min, range_max+1))


if __name__ == '__main__':
    puzzle1_counter: int = 0
    puzzle2_counter: int = 0
    with open('input.txt') as f:
        processed_range: list[list] = []
        for line in f:
            elf_ranges: list[set] = []
            range1_str, range2_str = line.splitlines()[0].split(',')
            range1 = get_range(range1_str)
            range2 = get_range(range2_str)

            if range1.issubset(range2) or range2.issubset(range1):
                puzzle1_counter += 1
            if len(range1.intersection(range2)) > 0:
                puzzle2_counter += 1
    print(puzzle1_counter)
    print(puzzle2_counter)

