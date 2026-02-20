print("-------------------------------------")
print("\nBem vindo ao Seu Cofre Python\n")
print("-------------------------------------")

saldo = 1000
prosseguir = 1
sair = 0

print ("Para Prosseguir 1, para sair 0")
entrada = (input("Digite um numero: "))
entrar = entrada == prosseguir
saida = entrada == sair

print(f"Você digitou o numero {entrada}")

if(entrar):
    print("Saldo da conta: {saldo}")




