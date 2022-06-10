letra = input("Digite uma letra: ")

# if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
if letra.lower() in ("a", "e", "i", "o", "u"):
    print("A letra é uma vogal!")
else:
    print("A letra não é uma vogal!")
