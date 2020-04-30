import random

def get_number_str(number, ind):
    str_number = str(number)
    null = '0'*(6 - len(str_number))
    str_number = null + str_number
    ind = ind.upper()
    result ='{0} {1}'.format(str_number, ind)
    return result
if __name__ == '__main__':
    count_winner = int(input())
    number_end = input().split(' ')
    ticket_ind = number_end[1]
    ticket_number = int(number_end[0])
    number_win = []
    if count_winner >= ticket_number:
        for i in range(ticket_number):
            win = i + 1
            win = get_number_str(win, ticket_ind)
            print('Победитель {0} - "{1}"'.format(i+1, win))
    else:
        while count_winner > 0:
            win = random.randint(1,ticket_number)
            if win in number_win:
                continue
            else:
                number_win.append(win)
                print('Победитель {0} - "{1}"'.format(count_winner,get_number_str(win, ticket_ind)))
                count_winner -= 1