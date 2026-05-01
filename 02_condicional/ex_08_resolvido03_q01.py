letra = input("Digite uma letra: ").lower()

# if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
if letra in ("a", "e", "i", "o", "u"):
    print(f"A letra '{letra}' é uma vogal!")
else:
    print(f"A letra '{letra}' não é uma vogal!")
