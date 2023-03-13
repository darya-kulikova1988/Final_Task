path = 'file_new.txt'
# read , r, a - если их нет - выдает ошибку, w- создает новую
file = open(path, 'r', encoding='UTF-8')
data = file.read()
# data=file.readline()
# data=file.readlines()
print(data)
