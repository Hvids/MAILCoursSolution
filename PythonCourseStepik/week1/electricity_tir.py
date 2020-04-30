if __name__ == '__main__':
    count = int(input())
    sum = 0
    for i in range(count):
        str_input = input().split(' ')
        x = float(str_input[0])
        y = float(str_input[1])
        r = (x ** 2 + y ** 2) ** (1 / 2)
        r_int = int(r)
        r_int = r_int  if (r_int + 1) <=10 else 10

        sum += 10 - r_int
    print(sum)
