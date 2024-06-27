import sys

star = '*'
nostar = ' '
n = int(sys.argv[1])

for y in range(0, n):
    for x in range(0, n):
        print(star if x <= y else nostar, end='')
    print()
pass
