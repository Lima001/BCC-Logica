def conj(*sentencas):
    retorno = ""
    retorno += "(" + sentencas[0] + " ! " + sentencas[0] + ")"
    for i in sentencas[1:]:
        retorno +=  " ! " + "(" + i + " ! " + i + ")"

    return "(" + retorno + ")"
        
def disj(*sentencas):
    retorno = ""
    retorno += sentencas[0]
    for i in sentencas[1:]:
        retorno +=  " ! " + i

    retorno = "((" + retorno + ")" + " ! " + "(" + retorno + "))" 
    return retorno

def neg(sentenca):
    retorno = "(" + sentenca + ")" + "!" + "(" + sentenca + ")"
    return "(" + retorno + ")"

def cond(sentenca1, sentenca2):
    sentenca1 = neg(sentenca1)
    return disj(sentenca1, sentenca2)

def bicon(sentenca1, sentenca2):
    return conj(cond(sentenca1, sentenca2), cond(sentenca2, sentenca1))


def gerar_sentencas_atomicas(lista_tokens):
    atoms = []
    for i in lista_tokens:
        if i[2] == "ATOM" and i[1] not in atoms:
            atoms.append(i[1])

    return atoms

def substituir_conectivos(expressao, lista_tokens):
    atoms = gerar_sentencas_atomicas(lista_tokens)
    for i in atoms:
        a = i
        exec(f"{i} = '{str(i)}'")

    return eval(expressao)


if __name__ == "__main__":
    from analisador_lexico import *
    from analisador_sintatico import *
    from criador_expressao import *

    string = input("Digite uma sentença lógica: ")
    string = "(" + string + ")"

    valido, lista_simbolos = identificar_tokens(string, padrao_tokens)

    posicoes = identificar_sentencas(lista_simbolos)
    expressao = criar_expressao(lista_simbolos,posicoes)
    print(expressao)
    print(substituir_conectivos(expressao,lista_simbolos))