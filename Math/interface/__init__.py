def titulo(txt):
    tamanho = len(txt) + 6
    print("\033[0;44m" + "-" * tamanho)
    print(f"   {txt}   ")
    print("-" * tamanho + "\n\033[m", end="")

def menu():
    operacao = ["Adição", "Subtração", "Multiplicação", "Divisão"]
    for indice, nome in enumerate(operacao, start=1):
        print(f"\033[1;33m{indice}\033[m - \033[1;34m{nome}\033[m")
