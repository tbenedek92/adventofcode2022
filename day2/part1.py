
LOSES_TO_DICT = {
    'A': 'B',
    'B': 'C',
    'C': 'A'
}

POINTS_DICT = {
    'A': 1,
    'B': 2,
    'C': 3
}

MAPPING_DICT = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}


def rps(rounds_list):
    print(rounds_list)
    sum_score = 0
    for round in rounds_list:
        splitted_round = round.split()
        score = score_calc(splitted_round[0], splitted_round[1])
        sum_score += score
    return sum_score


def score_calc(opponent, mine):
    match_result = -1
    mine_mapped = MAPPING_DICT[mine]
    if LOSES_TO_DICT[mine_mapped] == opponent:
        match_result = 0
    elif mine_mapped == opponent:
        match_result = 3
    elif LOSES_TO_DICT[opponent] == mine_mapped:
        match_result = 6
    else:
        print('Houston we have a problem')
    score = POINTS_DICT[mine_mapped] + match_result

    return score


def read_input(input_file):
    with open(input_file) as f:
        data = f.read().splitlines()
    return data


if __name__ == '__main__':
    data = read_input('input.txt')

    result = rps(data)
    print(result)