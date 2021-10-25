with open('words.txt', 'r') as file:
    s = file.readline()   
a = s.split(' ')
b = [a[i].strip(',.') for i in range(len(a)) if a[i].find('c') != -1]
for i in range(len(b)):
    print(b[i])
