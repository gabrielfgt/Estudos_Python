print("Bem vindo ao sistema de calculo do estúdio!")
print("___________________________________________")
print("Digite o número da sua assinatura contratada...")
print(" 1 - Basic \n 2 - Silver \n 3 - Gold \n 4 - Platinum\n")
taxa = float(0)
plano = int(input())

if plano == 1:
    taxa = 0.30
    print("Voce escolheu o plano Basic!")

elif plano == 2:
    taxa = 0.20
    print("Voce escolheu o plano Silver!")

elif plano == 3:
    taxa = 0.10
    print("Voce escolheu o plano Gold!")

elif plano == 4:
    taxa = 0.05
    print("Voce escolheu o plano PLatinum!")

else:
    print("Numero de plano inválido!")

print("\nDigite valor do faturamento anual.\n R$: ")

faturamento = float(input())

bonus = float(faturamento * taxa)

print(f'\nO valor à pagar de bônus é de: R${bonus:,.2f}')