def generar_primos():
    lista_primos = [2, 3, 5, 7]
    numero = 8
    while True:
        for i in lista_primos:
            #print (f"--{numero}--")
            #print (f"{i}---{lista_primos[-1]}")     
        
            if numero % i == 0:
                break
            if i == lista_primos[-1]:
                lista_primos.append(numero)
                print (numero)
                break
        numero = numero + 1

generar_primos()