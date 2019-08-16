import random

def jogar():
    print("================================")
    print("Bem vindo ao jogo de adivinhação")
    print("================================")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual é o seu nivel de dificuldade")
    print("(1) Fácil \n(2) Médio \n(3) Díficil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número de 1 a 100: ")
        print("Voce digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Voce deve digitar um número de 1 a 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Parabéns! Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("O seu chute foi maior do que o número secreto!")
            elif(menor):
                print("O seu chute foi menor do que o número secreto!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("\nFim do jogo")

if(__name__ == "__main__"):
    jogar()
    
input()