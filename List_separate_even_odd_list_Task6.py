original = [10, 501, 22, 37, 100, 999, 87, 351]

even = []
odd = []

for n in original:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print(original)
print(even)
print(odd)