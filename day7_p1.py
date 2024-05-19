# greater rank = more powerful  
def run():
    global sum
    sum = 1

with open(r"day7_input.txt", 'r') as fp:
    # score, bid, rank
    list = 0 * [1000][3]
    for count, line in enumerate(fp):
        run()
fp.close()

print(sum)