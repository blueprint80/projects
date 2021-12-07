cubes_odd = []
result = 0
for number in range(50):
    if number % 2 != 0:
        cubes_odd.append(number ** 3)
print(cubes_odd)

for element in cubes_odd:
    inx = cubes_odd.index(element)
    length = 0
    sum_el = 0
    while cubes_odd[inx] > 0:
        a = cubes_odd[inx] % 10
        cubes_odd[inx] //= 10
        length += 1
        sum_el += a
    if sum_el % 7 == 0:
        result += element
print(result)
