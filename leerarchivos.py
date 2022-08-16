f = open("demofile.txt", "a")
f.write("\n" + "este es un nuevo texto")
f.close()

f = open("demofile.txt")
print(f.read())
f.close()