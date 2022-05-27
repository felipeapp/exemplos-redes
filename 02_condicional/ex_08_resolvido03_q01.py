# A função lower converte a letra para minúsculo
letra = input("Digite uma letra: ").lower()

# if letra in "aeiouAEIOU":
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("A letra é uma vogal!")
else:
    print("A letra não é uma vogal!")
