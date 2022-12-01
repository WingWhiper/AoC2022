
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def get_biggest_number(listOfNumbers):
    big_number = 0
    total = 0
    for i in listOfNumbers:
        if i.startswith("\n"):
            if total > big_number:
                big_number = total
            total = 0
        else:
            total = total + int(i)
    return big_number


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open('/Users/josephsergent/PycharmProjects/AoC22/venv/AoC_D1_P1.txt')
    biggest_number = get_biggest_number(file)
    print(biggest_number)
    print_hi('Joe')
    file.close()
