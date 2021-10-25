start, stop = map(int, input().split())
a = [2**i for i in range(start,stop+1) if start <= stop]
a.pop(1) #del a[1]
a.pop(-2) #del a[-2]
print(a)
