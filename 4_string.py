i = str(input("Escreva um texto: "))

i = i.lower()
i = i.replace("a","4")
i = i.replace("e","3")
i = i.replace("i","1")
i = i.replace("o","0")
i = i.replace("u","V")
i = i.upper()
print(f"O resultado é: {i}")

i = i.replace(" ","-")
print(f"Resultado com hífen: {i}")
