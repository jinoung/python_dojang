import threading

def sum(low, high):
    total = 0
    for i in range(low, high):
        total += i
    print("Sub Thread...\n", total)

t = threading.Thread(target=sum, args=(1, 200000))
t.start()

print("Main Thread...\n")

      
