if __name__ == '__main__':
    f = open('data.txt', 'r')
    lines = f.readlines()
    f.close()
    easy = open('data0.txt', 'w')
    hard = open('data2.txt', 'w')
    easy_counter = 0
    hard_counter = 0
    for line in lines:
        answer = -1
        country = line.split('\t')[1]
        flag = line.split('\t')[2]
        capital = line.split('\t')[3]
        while not answer == 0 and not answer == 1:
            print('Is ' + country + ' difficult? (say 1 if yes and 0 if no)')
            answer = int(input())
        if answer:
            new_line = str(hard_counter) + '\t' + country + '\t' + flag + \
                       '\t' + capital
            hard.write(new_line)
            hard_counter += 1
        else:
            new_line = str(easy_counter) + '\t' + country + '\t' + flag + \
                       '\t' + capital
            easy.write(new_line)
            easy_counter += 1
    easy.close()
    hard.close()
