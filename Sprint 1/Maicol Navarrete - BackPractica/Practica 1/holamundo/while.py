intentos = 3
while intentos > 0:
    if input(">>>Ingrese la contraseña correcta:") == "Maicol2006":
        print("¡Correcta!")
        break
    intentos = intentos - 1
    print("Contraseña incorrecta")
else:
    print("Se te acabaron los intentos")