import sys
from collections import OrderedDict
if __name__ == '__main__':
    str1 = input().lower()
    str2 = input().lower()
    str2 = "".join(OrderedDict.fromkeys(str2))
    for c in str2:
        if  (not 'A' <= c <= 'Z') and (not 'a' <=c <= 'z'):
            continue

        print(c, end = ' ')
        meet = False
        for i in range(len(str1)):
           if c == str1[i]:
                meet = True
                print(i+1, end=' ')
        if not meet:
            print('None')
        else:
            print()
