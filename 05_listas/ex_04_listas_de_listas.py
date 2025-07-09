composta = [[3, 2, 3], [9, 3, 2], [5, 4, 0]]

print(composta[0])
print(composta[0][2])
print(composta[0], composta[2])
print(composta[0:2])

for linha in composta:
    for elem in linha:
        print(elem, end=" ")
    print()
