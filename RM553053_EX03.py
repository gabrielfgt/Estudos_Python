import time

print("Bem vindo ao sistema de cálculo de notas!")
print("_________________________________________")

alunos = int(50)
turmaPar = []
turmaImpar = []

for contadorImpar in range (1, 51, 2):
    print('VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES.')
    print(f'POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {contadorImpar}: ')
    notaImpar = input()
    turmaImpar.append(notaImpar)

for contadorPar in range (2, 51, 2):
    print('VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES.')
    print(f'POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {contadorPar}: ')
    notaPar = input()
    turmaPar.append(notaPar)

print('Calculando notas...')
time.sleep(3)

soma_das_notas_par = 0
for notaPar in turmaPar:
    soma_das_notas_par += int(notaPar)

soma_das_notas_impar = 0
for notaImpar in turmaImpar:
    soma_das_notas_impar += int(notaImpar)

media_Par = soma_das_notas_par / 25
media_Impar = soma_das_notas_impar / 25

print(f'A média da turma Par foi de: {media_Par} \nA média da turma Ímpar foi de: {media_Impar}')

if media_Impar > media_Par:
    print('A turma de maior nota foi a dos alunos de números Ímpares.')
else:
    print('A turma de maior nota foi a dos alunos de números Pares.')