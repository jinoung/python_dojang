def prime_number_generator(start, stop):
    count = 0
    while start <= stop:
        for i in range(start):
            if start % (i+1) == 0:
                count += 1
        if count <= 2:
            yield start
        start += 1
        count = 0
            
start, stop = map(int, input().split())
 
g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')
