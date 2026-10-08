

def leer_patron(nombre_archivo):

    archivo = open(nombre_archivo, "r")

    vector = []

    for linea in archivo:

        elementos = linea.split()

        for elemento in elementos:

            if elemento == "*":
                vector.append(1)
            else:
                vector.append(-1)

    archivo.close()

    return vector


patron1 = leer_patron("patron1.txt")
patron2 = leer_patron("patron2.txt")


W = []

for i in range(36):

    fila = []

    for j in range(36):

        peso = patron1[i] * patron1[j]
        peso = peso + patron2[i] * patron2[j]

        fila.append(peso)

    W.append(fila)


for i in range(36):

    W[i][i] = 0

def recordar(entrada):

    resultado = []

    for j in range(36):

        suma = 0

        for i in range(36):

            suma = suma + entrada[i] * W[i][j]

        if suma > 0:

            resultado.append(1)

        elif suma < 0:

            resultado.append(-1)

        else:

            resultado.append(entrada[j])

    return resultado


def mostrar_patron(vector):

    tamaño = int(len(vector) ** 0.5)

    for i in range(tamaño):

        fila = ""

        for j in range(tamaño):

            posicion = i * tamaño + j

            if vector[posicion] == 1:
                fila = fila + "* "
            else:
                fila = fila + ". "

        print(fila)


entrada = leer_patron("entrada.txt")

print("Entrada dañada:")

print("Vector:")
print(entrada)

print("Imagen:")
mostrar_patron(entrada)



for i in range(10):

    nuevo = recordar(entrada)

    if nuevo == entrada:

        print()
        print("El patrón se estabilizó.")
        break


    print()
    print("Iteración:", i + 1)

    print("Vector:")
    print(nuevo)

    print("Imagen:")
    mostrar_patron(nuevo)

    entrada = nuevo



print()
print("RESULTADO FINAL:")

print("Vector:")
print(entrada)

print("Imagen:")
mostrar_patron(entrada)