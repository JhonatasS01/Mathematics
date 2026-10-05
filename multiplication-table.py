#Multiplication Table Game
#Created by Jhonatas Góis
#Build version: 1.1
from random import sample

def titulo(txt):
    tamanho = len(txt) + 6
    print("\033[0;44m" + "-" * tamanho)
    print(f"   {txt}   ")
    print("-" * tamanho + "\n\033[m", end="")

titulo("Multiplication Table")

while True:
    try:
        erros = acertos = 0
        tabuada = int(input("\033[mQual tabuada deseja estudar? (Ex: 7): "))

        #ordena de forma aleatória e única, números de 1 a 10
        ordem_perguntas = sample(range(1, 11), 10)

        for numero in ordem_perguntas:
            while True:
                print("\033[0;41m", numero, f"x {tabuada} \033[m = ", end='')
                try:
                    resposta = int(input(""))
                    validador = numero * tabuada

                    if resposta == validador:
                        acertos += 1
                        break #vai para a próxima multiplicação da tabuada
                    else:
                        erros += 1
                        print("\033[1;31mValor incorreto! Tente novamente.\033[m")

                #log de erros de digitação
                except ValueError:
                    print("\033[1;31mErro! valor diferente de inteiro.\033[m")

        #dados de desempenho do jogador
        print("\033[0;47m" + "-" * 25)
        print(f"\033[1;31;47mErros: {erros}\n\033[1;32;47mAcertos: {acertos}")
        print("\033[m\033[0;47m" + "-" * 25 + "\n\033[m", end="")

        #
        continuar = input("Deseja treinar outra tabuada? [S/N]: ").strip().upper()
        if continuar != 'S':
            print("\n\033[1;32mObrigado por jogar! Até a próxima.\033[m")
            break

    #log de erros e paradas inesperadas
    except KeyboardInterrupt:
        print("\n\033[1;31mPrograma finalizado pelo usuário\033[m")
        break
    except ValueError:
        print("\033[1;31mErro! Por favor, digite um número inteiro válido para a tabuada.\033[m")
