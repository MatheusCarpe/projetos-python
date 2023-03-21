import random


def jogar():
    print('*********************************')
    print('Bem vindo ao jogo de adivinhação!')
    print('*********************************')

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 3
    nivel = 0
    pontos = 1000

    print('Qual nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')

    while nivel > 3 or nivel < 1:
        nivel = int(input('Defina o nível: '))
        if (nivel == 1):
            total_de_tentativas = 20
        elif (nivel == 2):
            total_de_tentativas = 10
        elif (nivel == 3):
            total_de_tentativas = 5
        else:
            print('OPÇÃO INVALIDA...DIGITE UM NÍVEL ENTRE 1 e 3')

    for rodada in range(1, total_de_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
        chute = int(input('Digite um número entre 1 e 100: '))
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        print('Você digitou', chute)

        if (chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100!')
            continue

        if (acertou):
            print('Você acertou e fez {} pontos'.format(pontos))
            break
        else:
            if (maior):
                print('Você errou...seu chute foi MAIOR que o número secreto')
            elif (menor):
                print('Você errou...seu chute foi MENOR que o número secreto')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print('Fim do Jogo')

if(__name__ == '__main__'):
    jogar()