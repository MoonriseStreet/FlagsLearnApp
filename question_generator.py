import random


def new_question(level) -> []:
    random_numbers = []
    if level == 'None':
        level = 0
    file = 'data' + str(level) + '.txt'
    f = open(file, 'r')
    lines = f.readlines()
    number_of_countries = len(lines)
    while len(random_numbers) < 4:
        number = random.randrange(number_of_countries)
        while number in random_numbers:
            number = random.randrange(number_of_countries)
        random_numbers.append(number)
    countries = []
    for i in range(4):
        countries.append(lines[random_numbers[i]])
    f.close()
    return countries
