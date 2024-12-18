def score(line):
    # remove Game X:
    line = line.replace('  ', ' ').replace('\n', '')
    line = line[line.find(':') + 2:]
    
    # seperates into winning numbers and card numbers
    win_num = line[:line.find('|') - 1]
    card_num = line[line.find('|') + 2:]
    win_num = win_num.split(' ')
    card_num = card_num.split(' ')

    # check the value of this card
    points = 0.5
    for num in card_num:
        if num in win_num:
            points *= 2
    return int(points)

with open(r"day4_input.txt", 'r') as fp:
    sum = 0
    for count, line in enumerate(fp):
        sum += score(line)
fp.close()

print(sum)