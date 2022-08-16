respuesta = "s"
tot=0
while respuesta == "s":
    diccionario = {"codigo":["1", "2", "3", "4", "5"], "nombre":["leche", "aceite", "atún", "azúcar", "arroz"], "precio":["4", "12", "4", "4.5", "5"]}
    print(diccionario)
    for key in diccionario:
        print(key, ":", diccionario[key])
    codigo = input("INGRESA EL CÓDIGO: ")
    cantidad = int(input("INGRESA LA CANTIDAD: "))
    if codigo == "E-001":
        precio = 4
        product = "leche"
    elif codigo == "E-002":
        precio = 12
        product = "aceite"
    elif codigo =="E-003":
        precio = 5
        product = "atún"
    elif codigo == "E-004":
        precio = 4
        product = "azúcar"
    elif codigo == "E-005":
        precio = 5
        product = "arroz"
    print("EL CÓDIGO ES: ",codigo)
    print("EL NOMBRE DEL PRODUCTO ES:", product)
    print("LA CANTIDAD ES: ",cantidad)
    print("EL PRECIO ES: S/",precio)
    total = precio * cantidad
    print("EL MONTO ES: S/", total)
    print("DESEA CONTINUAR SI (s) O NO (n)")
    respuesta = input()
    tot += total
    tup = [str(codigo), " - ", product, " - ", str(cantidad), " - ", str(precio), " - ", str(total)]
    cadenav = "".join(tup)
    f = open("demofile.txt", "a")
    f.write("\n" + cadenav)
    f.close()
f = open("demofile.txt")
print(f.read())
f.close()
print("EL PRECIO TOTAL A PAGAR ES: S/",tot)
print("GRACIAS POR LA COMPRA")