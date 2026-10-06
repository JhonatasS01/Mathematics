#Math Game
#Created by Jhonatas Góis
#Build version: 1.3
from random import sample
from Math import interface, operacao

interface.titulo("Math Game")

while True:
    try:
        erros = acertos = 0
        interface.menu()

        #validando a opção escolhida no menu
        while True:
            try:
                resp = int(input("Selecione uma opção: "))
                if 1 <= resp <= 4:
                    break
                print("\033[1;31mErro! opção invalida, tente novamente.\033[m")
            except ValueError:
                print("\033[1;31mErro! digite um número de 1 a 4.\033[m")

        simbolo = operacao.simb(resp) #simbolo da operação

        #validação da escolha da tabuada
        while True:
            try:
                tabuada = int(input("\033[mQual tabuada deseja estudar? (Ex: 7): "))
                if resp == 4 and tabuada == 0:
                    print("\033[1;31mNão é possível dividir por zero! Escolha outro número.\033[m")
                    continue
                break
            except ValueError:
                print("\033[1;31mErro! Por favor, digite um número inteiro válido para a tabuada.\033[m")

        #ordena de forma aleatória números de 1 a 10
        ordem_perguntas = sample(range(1, 11), 10)

        for numero in ordem_perguntas:
            solucao = operacao.opcao(resp, tabuada, numero)

            while True:
                print("\033[0;41m", numero, f"{simbolo} {tabuada} \033[m = ", end='')
                try:
                    resposta = float(input("").strip().replace(",", "."))

                    if resposta == solucao:
                        acertos += 1
                        break #vai para a próxima multiplicação da tabuada
                    else:
                        erros += 1
                        print("\033[1;31mValor incorreto! Tente novamente.\033[m")

                #log de erros de digitação
                except ValueError:
                    print("\033[1;31mErro! Digite um valor numérico válido.\033[m")

        #dados de desempenho do jogador
        print("\033[0;47m" + "-" * 25)
        print(f"\033[1;31;47mErros: {erros}\n\033[1;32;47mAcertos: {acertos}")
        print("\033[m\033[0;47m" + "-" * 25 + "\n\033[m", end="")

        #finalizador do programa
        continuar = input("Deseja treinar outra tabuada? [S/N]: ").strip().upper()
        if continuar != 'S':
            print("\n\033[1;32mObrigado por jogar! Até a próxima.\033[m\n")
            break

    #log de erros e paradas inesperadas
    except KeyboardInterrupt:
        print("\n\033[1;31mPrograma finalizado pelo usuário\033[m")
        break
