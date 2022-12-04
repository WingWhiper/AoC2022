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


def determine_winner_incorrectly(opponents_choice, player_choice):
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


def determine_winner_correctly(opponent_choice, round_choice):
    player_choice = ''
    round_result = ''
    match opponent_choice:
        case 'A':
            if round_choice == 'X':
                round_result = 'Lost'
                player_choice = 'Z'
            elif round_choice == 'Y':
                round_result = 'Tie'
                player_choice = 'X'
            elif round_choice == 'Z':
                round_result = 'Won'
                player_choice = 'Y'
        case 'B':
            if round_choice == 'X':
                round_result = 'Lost'
                player_choice = 'X'
            elif round_choice == 'Y':
                round_result = 'Tie'
                player_choice = 'Y'
            elif round_choice == 'Z':
                round_result = 'Won'
                player_choice = 'Z'
        case 'C':
            if round_choice == 'X':
                round_result = 'Lost'
                player_choice = 'Y'
            elif round_choice == 'Y':
                round_result = 'Tie'
                player_choice = 'Z'
            elif round_choice == 'Z':
                round_result = 'Won'
                player_choice = 'X'
    return round_result, player_choice


def get_round_score(opponent_choice, choice, doCorrectly):
    total_points = 0
    if doCorrectly:
        round_result, player_choice = determine_winner_correctly(opponent_choice, choice)
    else:
        round_result = determine_winner_incorrectly(opponent_choice, choice)
        player_choice = choice

    if player_choice == 'X':
        total_points += const.ROCK
    elif player_choice == 'Y':
        total_points += const.PAPER
    elif player_choice == 'Z':
        total_points += const.SCISSORS

    if round_result == 'Won':
        total_points += const.WON
    elif round_result == 'Tie':
        total_points += const.TIED
    elif round_result == 'Lost':
        total_points += const.LOST
    return total_points


def get_total_score(file, do_correctly):
    data = open(file)
    total_score = 0
    for i in data:
        choices = i.split()
        total_score += get_round_score(choices[0], choices[1], do_correctly)
    return total_score


def open_rucksack(rucksack):
    compartment = [rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]]
    print()
    return compartment


def compare_compartments(rucksack):
    compartments = open_rucksack(rucksack)
    compartment_a = compartments[0]
    compartment_b = compartments[1]
    matched_items = []
    matched_letter = ''
    for i in compartment_a:
        for o in compartment_b:
            if i == o and o != matched_letter:
                matched_items.append(i)
                matched_letter = o
                break
    return matched_items


def get_priority_value(matching_priority_list):
    total_value = 0
    for i in matching_priority_list:
        print(i[0])
        if i[0].isupper():
            print("Is was upper")
            total_value += 26

        for o in const.ITEM_PRIORITY:
            if i[0].lower() == o:
                print(int(const.ITEM_PRIORITY.index(o)))
                total_value += int(const.ITEM_PRIORITY.index(o)) + 1
                print("total value: " + str(total_value))
    print(total_value)
    return total_value


def reorganize_rucksacks(file):
    rucksacks = open(file)
    matched_priorities = []
    for i in rucksacks:
        matched_priorities.append(compare_compartments(i))
    priority_total = get_priority_value(matched_priorities)
    print(priority_total)
    rucksacks.close()
    return priority_total


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    biggest_number = get_biggest_number('venv/AoC_D1_P1.txt')
    top_three_total = get_top_three_total('venv/AoC_D1_P1.txt')
    wrongScore = get_total_score('venv/AoC_D2_P1.txt', False)
    correctScore = get_total_score('venv/AoC_D2_P1.txt', True)
    priority_total = reorganize_rucksacks('venv/AoC_D3_P1.txt')
    print("Day one answer 1: " + str(biggest_number))
    print("Day one answer 2: " + str(top_three_total))
    print("Day two answer 1: " + str(wrongScore))
    print("Day two answer 2: " + str(correctScore))
    print("Day three answer 1: " + str(priority_total))
