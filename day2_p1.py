# 1. Find max of each color in each game

def array(line):
    line_rgb = [0, 0, 0]
    # remove Game X:
    line = line[line.find(':') + 2:]
    # seperate into draws
    draws = line.split(" | ")
    # everything goes [r, g, b]
    for draw in draws:
        colors = draw.split(", ")
        for color in colors:
            ball_count = int(color[:color.find(' ')])
            ball_color = color[color.find(' ') + 1:color.find(' ') + 2]
            if ball_color == 'r' and ball_count > line_rgb[0]:
                line_rgb[0] = ball_count
            if ball_color == 'g' and ball_count > line_rgb[1]:
                line_rgb[1] = ball_count
            if ball_color == 'b' and ball_count > line_rgb[2]:
                line_rgb[2] = ball_count
    return line_rgb

rgb = [[0, 0, 0] for _ in range(100)] # this thing is 0-base

with open(r"day2_input.txt", 'r') as fp:
    for count, line in enumerate(fp):
        rgb[count] = array(line)
fp.close()

print(rgb[:10])

sum = 0
target = [12, 13, 14]
for i in range(len(rgb)):
    flag = True
    for col in range(3):
        if (target[col] < rgb[i][col]):
            flag = False
            break
    if (flag):
        sum += (i + 1)
print (sum)