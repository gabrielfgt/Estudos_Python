import time

print("Bem vindo ao sistema de votação de lives!")
print("_________________________________________")
totalVotos = []
print("Digite as quantidades de votos para Segunda-Feira: ")
votosSegunda = int(input())
totalVotos.append(votosSegunda)

print("Digite as quantidades de votos para Terça-Feira: ")
votosTerca = int(input())
totalVotos.append(votosTerca)

print("Digite as quantidades de votos para Quarta-Feira: ")
votosQuarta = int(input())
totalVotos.append(votosQuarta)

print("Digite as quantidades de votos para Quinta-Feira: ")
votosQuinta = int(input())
totalVotos.append(votosQuinta)

print("Digite as quantidades de votos para Sexta-Feira: ")
votosSexta = int(input())
totalVotos.append(votosSexta)

print("Votação finalizada.")
print("Aguarde o cálculo...")
time.sleep(2)
print("OK!")

diavencedor = max(totalVotos)

if int(diavencedor) == votosSegunda:
    print(f'O dia vencedor é Segunda-Feira, com {votosSegunda} votos.')
elif int(diavencedor) == votosTerca:
    print(f'O dia vencedor é Terça-Feira, com {votosTerca} votos.')
elif int(diavencedor) == votosQuarta:
    print(f'O dia vencedor é Quarta-Feira, com {votosQuarta} votos.')
elif int(diavencedor) == votosQuinta:
    print(f'O dia vencedor é Quinta-Feira, com {votosQuinta} votos.')
elif int(diavencedor) == votosSexta:
    print(f'O dia vencedor é Sexta-Feira, com {votosSexta} votos.')
else:
    print("Erro de sistema.")