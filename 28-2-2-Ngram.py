text = 'hello'
a = list(zip(*[text[i:] for i in range(2)]))
print(a)
