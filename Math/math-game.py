#Math Game
#Created by Jhonatas Góis
#Build version: 1.4
import time
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
                print("\033[1;31mErro! Opção inválida, tente novamente.\033[m")
            except ValueError:
                print("\033[1;31mErro! Digite um número de 1 a 4.\033[m")

        simbolo = operacao.simb(resp) #simbolo da operação

        #validação da escolha da tabuada
        while True:
            try:
                interface.dificuldade()
                nivel = int(input("Selecione uma dificuldade: "))
                if 1 <= nivel <= 3:
                    tabuada = operacao.nivel_tabuadas(nivel)
                    break
                print("\033[1;31mErro! Opção inválida, tente novamente.\033[m")
            except ValueError:
                print("\033[1;31mErro! Por favor, digite um número de 1 a 3.\033[m")

        #ordena de forma aleatória números de 1 a 10
        ordem_perguntas = sample(range(1, 11), 10)

        #inicia o cronômetro
        tempo_inicio = time.time()

        for numero in ordem_perguntas:
            solucao = operacao.opcao(resp, tabuada, numero)

            while True:
                print("\033[0;41m", tabuada, f"{simbolo} {numero} \033[m = ", end='')
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

        #cronômetro para e contabiliza
        tempo_fim = time.time()
        tempo_gasto = tempo_fim - tempo_inicio

        #dados de desempenho do jogador
        print("\033[0;47m" + "-" * 25)
        print(f"\033[1;31;47mErros: {erros}\n\033[1;32;47mAcertos: {acertos}\n\033[1;34mTempo gasto: {tempo_gasto:.2f}ms")
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
