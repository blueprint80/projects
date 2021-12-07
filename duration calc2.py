duration = int(input())
dividers = [1, 60, 60, 24, 10000]
names = ["д.", "ч.", "мин.", "сек."]
lst = []
result = []
for i in dividers:
    duration //= i
    lst.append(duration)
print(lst)


def func(x, y):
    return x % y


z = list(map(func, lst, dividers[1::]))[::-1]
for n in range(len(z)):
    if z[n] != 0:
        print(str(z[n]) + names[n])
