from random import randint

def opcao(opera, tabuadas, num):
    match opera:
        case 1:
            return num + tabuadas
        case 2:
            return num - tabuadas
        case 3:
            return num * tabuadas
        case 4:
            if tabuadas == 0:
                return 0 #evitando divisão por 0
            return round(num / tabuadas, 2)
        case _:
            return None

def simb(opera):
    match opera:
        case 1: return "+"
        case 2: return "-"
        case 3: return "x"
        case 4: return "/"
        case _: return "?"

def nivel_tabuadas(valor):
    match valor:
        case 1:
            return randint(1, 10)
        case 2:
            return randint(11, 50)
        case 3:
            return randint(51, 100)
        case _:
            return None
