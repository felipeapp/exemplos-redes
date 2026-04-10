a = False
b = True
c = False

print(a and b)
print(2 + 3 == 5 or 4 != 4)
print((a or b) and c)
print(a and b and c)
print(a or b or c)
print(a or b and c)  # noqa: RUF021 - O ideal é usar parenteses para melhorar a clareza do código
print(not a)
print(not b)
print(a or b and not c)  # noqa: RUF021 - O ideal é usar parenteses para melhorar a clareza do código
print(not (a and b))
