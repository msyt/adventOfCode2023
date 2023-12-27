# 1. Getting input line by line
# 2. Obtain the first and last int and add them up to be a 2-digit number
#    e.g. 1mmmmm2 --> 12; skjanknk2 --> 22; kkk2kkkkk3k --> 23
# 3. Add all the numbers up

def find_number(line):
    number = 0
    for character in line:
        if (character.isnumeric()):
            number += int(character)*10
            break
    for character in line[::-1]:
        if (character.isnumeric()):
            number += int(character)
            break
    return number

sum = 0 
with open(r"day1_input.txt", 'r') as fp:
    for count, line in enumerate(fp):
       sum += find_number(line)
fp.close()

# inputs = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

# for i in inputs:
#     print(find_number(i))
#     sum += find_number(i)

print(sum)