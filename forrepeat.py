a = [[10,20], [30,40], [50,60]]


for i in a:
    print(i)
    for j in i:
        print(j)

i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j], end=' ')
        j += 1
    print()
    i+=1
    
