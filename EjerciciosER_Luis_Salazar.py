import re

print("TEXTO A ANALIZAR: ")
texto = """
        Tecnologico
        Myster
        Maria
        Fundado
        Gracias
        Eugenio
        "Garza"
        Empresarios
        Constituyeron
        Asociacion
        Investigacion
        Superior
        +52 9851245678
        08:00 a.m
        17:30 p.m
        https://tec.mx/es
        info@tec.mx
        198.162.0.1
        97780
"""
print(texto)

print("1. Todas las palabras que tengan una longitud de 7 o más letras")
regex = r"[a-zA-Z]{7,}"
for matchNum, match in enumerate(re.finditer(regex, texto), start=1):
    print ("Coicidencia {matchNum} fue encontrado en {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
print("\n")


print("2. Expresiones que NO finalicen con una vocal.")
regex2 = r"^[a-zA-Z]*[^aeiou]$"
for matchNum, match in enumerate(re.finditer(regex2, texto), start=1):
    print ("Coincidencia {matchNum} fue encontrado en {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
print("\n")

print("3. Las palabras que inicien con “M” donde la segunda letra no sea vocal")
regex3 = r"[M][^aeiou][\w]*"
for matchNum, match in enumerate(re.finditer(regex3, texto), start=1):
    print ("Coincidencia {matchNum} fue encontrado en {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
print("\n")


print("4. Expresiones encerradas entre comillas")
regex4 = r"\"*[a-zA-Z]*\""
re.finditer(regex4, texto)
for matchNum, match in enumerate(re.finditer(regex4, texto), start=1):
    print ("Coincidencia {matchNum} fue encontrado en {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
print("\n")


print("5. Buscar IP's")
regex5 = r"\d\d\d.\d\d\d.\d.\d"
for matchNum, match in enumerate(re.finditer(regex5, texto), start=1):
    print ("Coincidencia {matchNum} fue encontrado en {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
print("\n")


print("6. Buscar la Hora")
regex6 = r"\d\d:\d\d"
for matchNum, match in enumerate(re.finditer(regex6, texto), start=1):
    print ("Coincidencia {matchNum} fue encontrado en {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
print("\n")


print("7. Buscar Telefonos")
regex7 = r"[0-9]{10,}"
for matchNum, match in enumerate(re.finditer(regex7, texto), start=1):
    print ("Coincidencia {matchNum} fue encontrado en {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
print("\n")


print("8. Buscar Correos electrónicos")
regex8 = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
for matchNum, match in enumerate(re.finditer(regex8, texto), start=1):
    print ("Coincidencia {matchNum} fue encontrado en {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
print("\n")


print("9. Buscar URL’s")
regex9 = r"http*[0-9]*(.+)?"
for matchNum, match in enumerate(re.finditer(regex9, texto), start=1):
    print ("Coincidencia {matchNum} fue encontrado en {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
print("\n")


print("9. Buscar Codigo Postal")
regex10 = r"[0-9]{5}$"
for matchNum, match in enumerate(re.finditer(regex10, texto), start=1):
    print ("Coincidencia {matchNum} fue encontrado en {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
print("\n")


print("""--------------------------------------------------------------------------
------------    Realizado por: Luis Ricardo Salazar Cetina    ------------
------------     5° B   Ing. en Sistemas Computacionales      ------------
--------------------------------------------------------------------------""")