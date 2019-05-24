#! /usr/bin/env python3
import re
coord_matcher_regex = "^#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)$"


b=set()
def mark(cloth, x, y, width, height, marker):
    b.add(marker)
    for i in range(x+1, x+width+1):
        for j in range(y+1, y+height+1):
#            print(i,j)
            if(cloth[i][j] != 0 and cloth[i][j]!=-1):
#                print('clash')
                try:
                    b.remove(cloth[i][j])
                except KeyError as e:
                    pass
                try:
                    b.remove(marker)
                except KeyError as e:
                    pass
                cloth[i][j] = -1
            else:
                cloth[i][j] = marker
        
def main():
    cloth = [[0 for i in range(1001)] for j in range(1001)]
    with open('input3.txt') as file:
        for line in file:
            match = re.search(coord_matcher_regex, line)
            num, x, y, width, height = match.group(*range(1, 6))
            num, x, y, width, height = [int(i) for i in [num, x, y, width, height]]
            mark(cloth, x, y, width, height, num)

    counter = 0
    for i in cloth[1:]:
        for j in i[1:]:
            if(j == -1):
                counter += 1
    print(counter)
    print(b)


if __name__ == '__main__':
    main()
