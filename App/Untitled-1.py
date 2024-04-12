def palabra(a):
    caracter = ''
    for i in a:
        caracter = caracter + i+ i
    return caracter

print(palabra('animo'))