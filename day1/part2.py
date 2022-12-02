def elf_top_three_calories(calories_list, max_n):
    elf_calorie = 0
    elf_calorie_sum_list = []

    for calorie in calories_list:
        if calorie.isdigit():
            elf_calorie += int(calorie)
        else:
            elf_calorie_sum_list.append(elf_calorie)
            elf_calorie = 0

    top_max_calorie = 0
    for i in range(max_n):
        max_calorie = max(elf_calorie_sum_list)
        top_max_calorie += max_calorie
        max_index = elf_calorie_sum_list.index(max_calorie)
        elf_calorie_sum_list.pop(max_index)

    return top_max_calorie
def file_reader():
    with open('input.txt') as f:
        data = f.read().splitlines()
    return data


if __name__ == '__main__':
    data = file_reader()
    result = elf_top_three_calories(data, 3)
    print(result)