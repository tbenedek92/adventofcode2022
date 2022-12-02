LOSES_TO_DICT = {
    'A': 'B',
    'B': 'C',
    'C': 'A'
}

SHAPE_POINTS_DICT = {
    'A': 1,
    'B': 2,
    'C': 3
}


def rps(rounds_list):
    print(rounds_list)
    sum_score = 0
    for round in rounds_list:
        score = score_calc(round.split()[0], round.split()[1])
        sum_score += score
    return sum_score


def score_calc(opponent, outcome):
    mapping_dict = {
        'X': list(LOSES_TO_DICT.keys())[list(LOSES_TO_DICT.values()).index(opponent)],
        'Y': opponent,
        'Z': LOSES_TO_DICT[opponent]
    }

    match_result = -1
    mine_mapped = mapping_dict[outcome]
    if LOSES_TO_DICT[mine_mapped] == opponent:
        match_result = 0
    elif mine_mapped == opponent:
        match_result = 3
    elif LOSES_TO_DICT[opponent] == mine_mapped:
        match_result = 6
    score = SHAPE_POINTS_DICT[mine_mapped] + match_result

    return score


def read_input(input_file):
    with open(input_file) as f:
        data = f.read().splitlines()
    return data


if __name__ == '__main__':
    data = read_input('input.txt')

    result = rps(data)
    print(result)
