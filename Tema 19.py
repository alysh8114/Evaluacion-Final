datos = {
    "codigo": ["001", "002", "003", "004", "005"],
    "nombre": ["Diego Ramos", "Alexander Lopez", "Sara Villalta", "Thiago Guzman", "David Peña"],}
listadatos = []
respuesta = "s"
while respuesta == "s":
    codigodato = input("Ingresar el codigo del alumno: ")
    curso = input("Ingrese el curso: ")
    nota1 = int(input("Ingresar nota 1 : "))
    nota2 = int(input("Ingresar nota 2 : "))
    nota3 = int(input("Ingresar nota 3 : "))
    nota4 = int(input("Ingresar nota 4 : "))
    nota5 = int(input("Ingresar nota 5 : "))
    x = 0
    for i in datos["codigo"]:
        if i == codigodato:
            codigodato = i
            nombredato = datos["nombre"][x]
            promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
            registro = ["Codigo: " + str(codigodato) + " | " + "Nombre: " + str(nombredato) + " | " + "Curso: " + str(curso) + " | " + "Nota 1: " + str(nota1) + "| " + "Nota 2: " + str(nota2) + " | " + "Nota 3: " + str(nota3) + " | " "Nota 4: " + str(nota4) + " | " "Nota 5: " + str(nota5) + " | " + "Promedio: " + str(promedio)]
            cadena = "".join(registro)
            f = open("demofile.txt", "a")
            f.write("\n" + cadena)
            f.close()

        x += 1
    respuesta = input("¿Desea seguir ingresando datos? : s/n ")

print("Datos generales del alumno")
f = open("demofile.txt")
print(f.read())
f.close()

