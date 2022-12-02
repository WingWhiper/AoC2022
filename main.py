import const

def get_biggest_number(fileName):
    data = open(fileName)
    big_number = 0
    total = 0
    for i in data:
        if i.startswith("\n"):
            if total > big_number:
                big_number = total
            total = 0
        else:
            total = total + int(i)
    data.close()
    return big_number


def get_top_three_total(fileName):
    data = open(fileName)
    total = 0
    totals_list = []
    top_three_total = 0
    for i in data:
        if i.startswith("\n"):
            totals_list.append(total)
            total = 0
        else:
            total = total + int(i)
    top_three_total += max(totals_list)
    totals_list.remove(max(totals_list))
    top_three_total += max(totals_list)
    totals_list.remove(max(totals_list))
    top_three_total += max(totals_list)
    totals_list.remove(max(totals_list))
    data.close()
    return top_three_total


def determine_winner(opponents_choice, player_choice):
    o = opponents_choice
    p = player_choice
    game_result = ''
    match o:
        case 'A':
            if p == 'X':
                game_result = 'Tie'
            elif p == 'Y':
                game_result = 'Won'
            elif p == 'Z':
                game_result = 'Lost'
        case 'B':
            if p == 'X':
                game_result = 'Lost'
            elif p == 'Y':
                game_result = 'Tie'
            elif p == 'Z':
                game_result = 'Won'
        case 'C':
            if p == 'X':
                game_result = 'Won'
            elif p == 'Y':
                game_result = 'Lost'
            elif p == 'Z':
                game_result = 'Tie'
    return game_result


def get_round_score(opponent_choice, player_choice):
    total_points = 0
    round_result = determine_winner(opponent_choice, player_choice)
    if round_result == 'Won':
        total_points += const.WON
    elif round_result == 'Tie':
        total_points += const.TIED
    elif round_result == 'Lost':
        total_points += const.LOST

    if player_choice == 'X':
        total_points += const.ROCK
    elif player_choice == 'Y':
        total_points += const.PAPER
    elif player_choice == 'Z':
        total_points += const.SCISSORS

    return total_points


def get_total_score(file):
    data = open(file)
    total_score = 0
    for i in data:
        choices = i.split()
        total_score += get_round_score(choices[0], choices[1])
    return total_score


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    biggest_number = get_biggest_number('venv/AoC_D1_P1.txt')
    top_three_total = get_top_three_total('venv/AoC_D1_P1.txt')
    score = get_total_score('venv/AoC_D2_P1.txt')
    print("Day one answer 1: " + str(biggest_number))
    print("Day one answer 2: " + str(top_three_total))
    print("Day two answer 1: " + str(score))
