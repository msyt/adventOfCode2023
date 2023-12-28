content = ''
with open(r"day3_input.txt", 'r') as fp:
    for count, line in enumerate(fp):
        content += line
fp.close()

content = content.replace('.', '')

new = ''
for i in content:
    if not i.isdigit():
        new += i

final = []
for i in new:
    if i not in final:
        final += i

print(final)

# ['\n', '-', '+', '*', '&', '/', '@', '%', '=', '$', '#']