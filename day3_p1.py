with open(r"day2_input.txt", 'r') as fp:
    for count, line in enumerate(fp):
        rgb[count] = array(line)
fp.close()

valid = ['-', '+', '*', '&', '/', '@', '%', '=', '$', '#']