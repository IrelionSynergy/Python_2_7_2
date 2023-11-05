print('Введите строку до 1000 символов')
string = input().split(' ')
if len(string) > 1000: 
    print('Введено неверное количество символов')
else:
    result = []
    for ch in string:
        if ch != '': result.append(ch)
        print(' '.join(result))