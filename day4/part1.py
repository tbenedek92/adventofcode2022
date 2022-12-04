
def read_file(in_file):
    with open(in_file) as f:
        processed_range: list[list] = []
        for line in f:
            elf_ranges: list[dict] = []
            ranges_str = line.splitlines()[0].split(',')
            for rng in ranges_str:
                range_dict: dict[str, int] = {
                    'range_start': int(rng.split('-')[0]),
                    'range_end': int(rng.split('-')[1])
                }

                elf_ranges.append(range_dict)
            processed_range.append(elf_ranges)
    return processed_range


def enclosed_counter(elf_cleanup_ranges):
    assignment_enclosed_counter: int = 0
    for elf_pairs in elf_cleanup_ranges:
        if elf_pairs[0]['range_start'] <= elf_pairs[1]['range_start']:
            if elf_pairs[0]['range_end'] >= elf_pairs[1]['range_end']:
                assignment_enclosed_counter += 1
                continue

        if elf_pairs[1]['range_start'] <= elf_pairs[0]['range_start']:
            if elf_pairs[1]['range_end'] >= elf_pairs[0]['range_end']:
                assignment_enclosed_counter += 1
    return assignment_enclosed_counter


def overlap_counter(elf_cleanup_ranges):
    assignment_overlap_counter: int = 0
    for elf_pairs in elf_cleanup_ranges:
        if elf_pairs[0]['range_start'] <= elf_pairs[1]['range_start'] <= elf_pairs[0]['range_end'] <= elf_pairs[1]['range_end']:
            assignment_overlap_counter += 1
            continue
        if elf_pairs[1]['range_start'] <= elf_pairs[0]['range_start'] <= elf_pairs[1]['range_end'] <= elf_pairs[0]['range_end']:
            assignment_overlap_counter += 1
            continue
        if elf_pairs[0]['range_start'] <= elf_pairs[1]['range_start'] <= elf_pairs[1]['range_end'] <= elf_pairs[0]['range_end']:
            assignment_overlap_counter += 1
            continue
        if elf_pairs[1]['range_start'] <= elf_pairs[0]['range_start'] <= elf_pairs[0]['range_end'] <= elf_pairs[1]['range_end']:
            assignment_overlap_counter += 1

    return assignment_overlap_counter

if __name__ == '__main__':
    input_file = read_file('input.txt')
    part1 = enclosed_counter(input_file)
    print(part1)

    part2 = overlap_counter(input_file)
    print(part2)

