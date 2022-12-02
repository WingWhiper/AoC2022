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
    return top_three_total


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    biggest_number = get_biggest_number('venv/AoC_D1_P1.txt')
    top_three_total = get_top_three_total('venv/AoC_D1_P1.txt')
    print("Day one answer 1: " + str(biggest_number))
    print("Day one answer 2: " + str(top_three_total))