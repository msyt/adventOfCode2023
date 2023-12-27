# 1. Getting input line by line
# 2. Obtain the first and last number (in string) and add them up to be a 2-digit number
#    e.g. one234five --> 15; 123two124 --> 22; aaaaa1onelllkethree   --> 23
# 3. Add all the numbers up
# ok I'm planning to use substring and their indexes

# slicing:
# b = "0123456789"
# print(b[2:5])
# output: 234

def find_number(line):

    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    first = len(line) 
    last = 0
    ind = [0, 0]

    number = 0

    for i in range(len(nums)):
        if line.find(nums[i]) >= 0:
            if line.rfind(nums[i]) > last:
                last = line.rfind(nums[i])
                ind[1] = i + 1
            if line.find(nums[i]) < first:
                first = line.find(nums[i])
                ind[0] = i + 1
    for character in line[:first]:
        if (character.isnumeric()):
            ind[0] = int(character)
            break
    for character in line[last:][::-1]:
        if (character.isnumeric()):
            ind[1] = int(character)
            break

    return ind[0]*10 + ind[1]

sum = 0 
with open(r"day1_input.txt", 'r') as fp:
    for count, line in enumerate(fp):
       sum += find_number(line)
fp.close()

# inputs = ['thfjtb56c']

# for i in inputs:
#     print(find_number(i))
#     sum += find_number(i)

print(sum)