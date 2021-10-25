start, stop = map(int, input().split())
while start <= stop:
    if start % 5 == 0 and start % 7 == 0:
        print('FizzBuzz')
    elif start % 5 == 0:
        print('Fizz')
    elif start % 7 == 0:
        print('Buzz')
    else:
        print(start)
    start+=1
        
