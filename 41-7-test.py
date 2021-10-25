def calc():
    result = 0
    while True:
        ex = (yield result)
        a, op, b = ex.split()
        
        if op == '+':
            result = int(a) + int(b)
        elif op == '-':
            result = int(a) - int(b)
        elif op == '*':
            result = int(a) * int(b)
        elif op == '/':
            result = int(a) / int(b)
            
expressions = input().split(', ')

c = calc()
next(c)

for e in expressions:
    print(c.send(e))

c.close()    
