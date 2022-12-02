
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


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

def get_next_biggest_number(bigger_number, list_Of_Numbers):
    big_number = bigger_number
    total = 0
    next_biggest = 0
    for i in list_Of_Numbers:
        if i.startswith("\n"):
            if next_biggest > total < big_number:
                next_biggest = total
                total = 0
        else:
            total = total + int(i)
    return next_biggest


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    biggest_number = get_biggest_number('venv/AoC_D1_P1.txt')
    #second_biggest = get_next_biggest_number(biggest_number, 'venv/AoC_D1_P1.txt')
    #print("Second number: " + str(second_biggest))
    #third_biggest = get_next_biggest_number(second_biggest, 'venv/AoC_D1_P1.txt')
    #top_three = int(biggest_number) + int(second_biggest) + int(third_biggest)
    print(biggest_number)
