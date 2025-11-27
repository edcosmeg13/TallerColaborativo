def generar_numeros_perfectos(cantidad):
    perfectos = []
    numero = 2

    while len(perfectos) < cantidad:
        suma = 1
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                suma += i
                if i != numero // i:
                    suma += numero // i
        if suma == numero:
            perfectos.append(numero)
        numero += 1

    return perfectos

