print('Это пробная версия для отправки на GIT')
x_list = []
y_list = []
for i in range(10):
    try:
        x = int(input('Введите X = '))
        x_list.append(x)
        y = int(input('Введите Y = '))
        y_list.append(y)
    except:
        ValueError
        print('Нужно вводить только цифры.')
        print('Попробуем еще раз.')

oper_dir_x = [x ** 3 for x in x_list]
print(oper_dir_x)