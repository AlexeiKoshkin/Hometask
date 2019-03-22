import pickle
#Исходные данные
list_user = {}
registr_user = {}
#Функции
def vivod_user():
    with open('results_user.txt', 'rb') as fp:
        try:
            while True:
                list_user.update(pickle.load(fp))
        except EOFError:
            pass
    if len(list_user) == 0:
        print('Список пуст')
    else:
        for key in list_user:
            print(key)
               
def add_user():
    n = input('Имя: ')
    v = float(input('Возраст: '))
    p = input('Пол (м/ж): ')
    h = float(input('Рост в сантиметрах: '))
    m = float(input('Вес в килограммах: '))
    list_user[n] = {'vozrast': v,'pol': p, 'hieght': h, 'massa': m}
    with open('results_user.txt', 'ab') as fp:
        pickle.dump(list_user, fp)
   
def del_user():
    n = input('Введите Имя: ')
    with open('results_user.txt', 'rb') as fp:
        try:
            while True:
                list_user.update(pickle.load(fp))
        except EOFError:
            pass
    del(list_user[n])
    with open('results_user.txt', 'wb') as fp:
        pickle.dump(list_user, fp)


def cho_user():
    n = input('Введите имя: ')
    with open('results_user.txt', 'rb') as fp:
        try:
            while True:
                list_user.update(pickle.load(fp))
        except EOFError:
            pass
    print("Имя: {}\nВозраст: {}\nПол: {}\nРост: {}\nВес: {}".format(n, list_user[n]['vozrast'], list_user[n]['pol'], list_user[n]['hieght'], list_user[n]['massa']))
    #Вычисляем BMI
    i = round(((list_user[n]['massa'] / list_user[n]['hieght'] ** 2) * 10000), 2)
    list_user.update({n: {'vozrast': list_user[n]['vozrast'],'pol': list_user[n]['pol'], 'hieght': list_user[n]['hieght'], 'massa': list_user[n]['massa'], 'bmi': i}})
    with open('results_user.txt', 'wb') as fp:
        pickle.dump(list_user, fp)
    #Выводим: Приветствие: Уважаемая(й) <Имя> Ваш возраст: Ваш рост: Ваш вест Ваш BMI
    if list_user[n]['pol'] == 'м':
        s = 'ый'
    else:
        s = 'ая'
        print('Уважаем' + '{} '.format(s) + n + '.' + ' Ваш возраст: ' + str(list_user[n]['vozrast']) + '.' + ' Ваш рост: ' + str(list_user[n]['hieght']) + '.' + ' Ваш вес: ' + str(list_user[n]['massa']) + '.' + ' Ваш BMI: ' + str(i) + '.')
        print('Классификация: ', end='')
    if i <= 16:
        print('выраженный дефицит массы тела.')
        print('Рекомендуется повышение веса, лечение анорексии.')
    elif 16 < i <= 18.5:
        print('недостаточная масса тела.')
        print('Рекомендуется повышение веса.') 
    elif 18.5 < i <= 25:
        print('нормальная масса тела.')
        print('Похудение не требуется.') 
    elif 25 < i <= 30:
        print('избыточная масса тела (предожирение).')
        print('Рекомендуется похудение.') 
    elif 30 < i <= 35:
        print('ожирение 1-ой степени.')
        print('Рекомендуется снижение массы тела.')
    elif 35 < i <= 40:
        print('ожирение 2-ой степени.') 
        print('Настоятельно рекомендуется снижение массы тела.')
    elif i > 40:
        print('ожирение 3-ой степени.')
        print('Необходимо немедленное снижение массы тела.') 

    #График BMI
    print('График BMI')
    d = int(i - 11)
    l = int(79 - i)
    print('10' + '#' * d + str(i) + '*' * l + '80')

    obnov = input('Обновить информацию (да/нет)?')
    if obnov == 'да':
        v = float(input('Возраст: '))
        p = input('Пол (м/ж): ')
        h = float(input('Рост в сантиметрах: '))
        m = float(input('Вес в килограммах: '))
        list_user.update({n: {'vozrast': v,'pol': p, 'hieght': h, 'massa': m}})
        with open('results_user.txt', 'wb') as fp:
            pickle.dump(list_user, fp)


def login_required(fn):
    def wrapper():
        if registr_user:
            fn()
        else:
            print('Авторизуйтесь')
            login = input('Логин: ')
            password = input('Пароль: ')
            registr_user[login] = password
            fn()      
    return wrapper()



@login_required
def menu_user():
    k = 0
    while k != 5:
        print('Доступные команды: \n 1 - вывести список пользователей \n 2 - добавить пользователя \n 3 - удалить пользователя \n 4 - выбрать пользователя \n 5 - выход')
        var = int(input('Выберите команду: '))
    #1 - вывести список пользователей
        if var == 1:
            vivod_user()
        
    #2 - добавить пользователя      
        elif var == 2:
            add_user()
        
    #3 - удалить пользователя
        elif var == 3:
            del_user()
           
    #4 - выбрать пользователя
        elif var == 4:
            cho_user()

    #5 - выход
        elif var == 5:
            k = 5
                           
print('Завершение')
