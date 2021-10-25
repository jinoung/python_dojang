import pickle

with open('jinoung.p', 'rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    print(name)
    print(age)
