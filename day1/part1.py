def elf_max_calorie(elf_calorie_list):
    elf_calorie = 0
    max_elf_calorie = 0
    for calorie in elf_calorie_list:
        if calorie.isdigit():
            elf_calorie += int(calorie)
        else:
            elf_calorie = 0

        max_elf_calorie = max(elf_calorie, max_elf_calorie)

    return max_elf_calorie


def file_reader():
    with open('day1/input.txt') as f:
        data = f.read().splitlines()
    return data


if __name__ == '__main__':
    data = file_reader()
    result = elf_max_calorie(data)
    print(result)
