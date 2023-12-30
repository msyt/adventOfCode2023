def score(line, count):
    # remove Game X:
    line = line.replace('  ', ' ').replace('\n', '')
    line = line[line.find(':') + 2:]
    
    # seperates into winning numbers and card numbers
    win_num = line[:line.find('|') - 1]
    card_num = line[line.find('|') + 2:]
    win_num = win_num.split(' ')
    card_num = card_num.split(' ')

    # check the value of this card
    match = 0
    for num in card_num:
        if num in win_num:
            match += 1
    # print(match)
    if match > 0:
        for i in range(1, match + 1):
            card_count[count + i] += card_count[count]
    return

with open(r"day4_input.txt", 'r') as fp:
    card_count = [1] * 193
    for count, line in enumerate(fp):
        score(line, count)
fp.close()

print(sum(card_count))