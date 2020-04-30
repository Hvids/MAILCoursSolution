if __name__ == '__main__':
    str_original = 'abcdefghijklmnopqrstuvwxyz'
    str_input = input()
    str_shifr = ""
    str_result = ''
    for i in range(len(str_input)):
        if 'a' <= str_input[i] <=  'z':
            c = str_input[i]
            ind_shifr = str_shifr.find(c)
            str_result += str_original[ind_shifr]
        else:
            str_result += str_input[i]
    print(str_result)