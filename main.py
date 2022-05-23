usuario = input("Introduce una lista de paises separados por comas: ")

paises = set(usuario.split(","))

print(sorted(paises))