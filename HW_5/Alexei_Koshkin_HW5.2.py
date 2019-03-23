headers = input("Файл содержит заголовки? (д/н)")
delim = input("Используемый разделитель: ")
result = {}

if headers == 'н':
    with open('1.csv', 'r') as fp:
        for line in fp.readlines():
            list = line.split(delim)
            result[list[0]] = list[1:]
    print(result)
  
elif headers == 'д':
    #не успел реализовать с заголовком
    with open('2.csv', 'r') as fp:
        for line in fp.readlines():
            list = line.split(delim)
            result[list[0]] = list[1:]
    print(result)









