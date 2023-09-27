print("Bem vindo ao sistema de quebra de senha!")
print("________________________________________")

def calcular_fatorial(numero):
    if numero == 0:
        return 1
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

minutos = int(input("Digite os minutos atuais: "))

fatorial_minutos = calcular_fatorial(minutos)

senha = "LIBERDADE" + str(fatorial_minutos)

print("A senha de desbloqueio é:", senha)
