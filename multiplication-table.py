#Game of Multiplication Table
#Created by Jhonatas Góis
#Build version: 1.0
from random import sample

def titulo(txt):
    print("\033[0:44m-" * (len(txt) + 5))
    print(f"{txt}".center((len(txt) + 5)))
    print("-" * (len(txt) + 5))


titulo("Multiplication Table")
erros = acertos = 0
tabuada = int(input("\033[mQual tabuada deseja?: "))

ordem_perguntas = sample(range(1, 11), 10)

#criando a tabuada do 1 ao 10
for numero in ordem_perguntas:
    while True:
        print(numero, f"x {tabuada} = ", end='')
        resposta = int(input(""))

        #calculando e validando a resposta
        validador = numero * tabuada
        if resposta == validador:
            acertos += 1
            break #vai para a próxima multiplicação da tabuada
        else:
            erros += 1
            print("\033[1;31mValor incorreto!\033[m")

#dados de desempenho do jogador
print("\033[0:47m")
print(f"\033[1:31:47mErros: {erros}\n\033[1:32:47mAcertos: {acertos}2")
print()
