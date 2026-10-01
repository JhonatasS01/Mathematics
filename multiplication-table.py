#Game of Multiplication Table
#Created by Jhonatas Góis
#Build version: 1.0
from random import sample

erros = acertos = 0
tabuada = int(input("Qual tabuada deseja?: "))

#criando a tabuada do 1 ao 10
aleatorio = sample(range(1, 11), 1)
for c in range(1, 10+1):
    while True:
        print(aleatorio[0], f"x {tabuada} = ", end='')
        resposta = int(input(""))
        #calculando e validando a resposta
        validador = aleatorio[0] * tabuada
        if resposta == validador:
            acertos += 1
            break
        else:
            erros += 1
            print("\033[1;31mValor incorreto!\033[m")

#dados do desempenho do jogador
print("-" * 30)
print(f"Erros: {erros}\nAcertos: {acertos}")