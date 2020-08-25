f = open('data.txt', 'r')

for line in f:
    number = line.split('\t')[0]
    name = line.split('\t')[1]
    pic = line.split('\t')[2]
    capital = line.split('\t')[3]
    if len(name) == 0 or len(pic) == 0 or len(capital) == 0:
        print('F U C K F U C K ! ! ! ! ! ! ! ! ')
        break
    print(
        number + ' ' + name + ' ' + pic + ' ' + capital
    )
