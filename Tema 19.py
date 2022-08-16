productos = {"codigo" : ["4651", "4651", "4583", "4464", "4375"],
            "alumno" :["Diego", "David", "Azul", "Sara", "Alex"],
            "nota" :[]}

listaproductos = []
totalCompra = 0
resp = "s"
while resp == "s":
    codigoIn = input("Ingresar el codigo del alumno: ")
    cantidad = int(input("Ingresar la cantidad del producto: "))
    x = 0
    for i in productos["codigo"]:
        if i == codigoIn:
            codigoTemp = i
            nombreTemp = productos["alumno"][x]
            precioTemp = ["nota"][x]
            totalTemp = cantidad
            totalCompra = totalCompra + totalTemp
            registro = codigoTemp, nombreTemp, precioTemp, cantidad, totalTemp
            listaproductos.append(registro)
        x += 1
    resp = input("¿Desea seguir ingresando datos? : s/n ")

print("Cod Nombre Precio Cant Total")
for x in listaproductos:
    print(*x, end="\n")

print("El Total de la compra es: ", totalCompra)
