x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
y = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key, value in x.items():
    print(key, value)

for key in x.keys():
    print(key, end=' ')
print()

for value in x.values():
    print(value, end=' ')
print()

keys = ['a', 'b', 'c', 'd']
x = {key:value for key, value in dict.fromkeys(keys).items()}
print(x)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x = {key: value for key, value in x.items() if value != 20}
print(x)

terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}
 
print(terrestrial_planet['Venus']['mean_radius'])    # 6051.8

x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x
print("x is y :", x is y)
y['a'] = 99
print(x, y)

y = x.copy()
print("x is y ", x is y)
y['a'] = 100
print(x, y)

#중첩 딕셔너리를 완전히 복사하려면 copy 메서드 대신 copy 모듈의 deepcopy 함수를 사용
x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
import copy
y = copy.deepcopy(x)
y['a']['python'] = '2.5'
print(x)
print(y)

