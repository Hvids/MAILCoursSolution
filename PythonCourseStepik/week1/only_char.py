from collections import OrderedDict
if __name__ == '__main__':
    str = input().lower()
    str = ''.join(OrderedDict.fromkeys(str))
    str_result = ''
    for c in str:
        if 'a' <= c <= 'z':
            str_result += c
    str_result = sorted(str_result)
    print()
    print("".join(str_result))