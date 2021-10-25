with open('words.txt', 'r') as file:
    line = None
    a = []
    while line != '':
        line = file.readline()
        a.append(line.strip('\n'))

for i in a:
    if i == i[::-1]:
        print(i)
