def formatar_sentenca(lista_tokens):
    operadores_binarios = {
        "&":"conj",
        "|":"disj",
        "~":"neg",
        "->":"cond",
        "<->":"bicon"
    }
    operador = ""
    sentencas_componente = []
    
    for i in range(len(lista_tokens)):
        if lista_tokens[i][2] == "OPBIN":
            operador = operadores_binarios[lista_tokens[i][1]]
            break

    for i in range(len(lista_tokens)):
        if lista_tokens[i][2] == "ATOM" or lista_tokens[i][2] == "SENT":
            
            cont_negacao = 0
            j = i-1
            
            while j >= 0 and lista_tokens[j][2] == "OPUN":
                cont_negacao += 1
                j -=1

            expressao = "neg("*cont_negacao + lista_tokens[i][1] + ")"*cont_negacao

            sentencas_componente.append(expressao)

    expressao = operador + "("
    
    for i in range(len(sentencas_componente)):
        if i != len(sentencas_componente) -1:
            expressao += sentencas_componente[i] + ","
     
    expressao += sentencas_componente[-1] + ")"

    return expressao

def localizar_chave_tokens(lista_tokens, chave):
    for i in range(len(lista_tokens)):
        if lista_tokens[i][0] == chave:
            return i
    return None

def criar_expressao(lista_tokens, posicoes):
    pos_sentencas = {}

    for i in range(len(posicoes)):
        inicio, fim = posicoes[i]
        pos_inicio = localizar_chave_tokens(lista_tokens, inicio)
        pos_final = localizar_chave_tokens(lista_tokens, fim)
        
        sentenca = lista_tokens[pos_inicio:pos_final+1]
        
        inicio_sub_sent, fim_sub_sent = None, None

        for i in range(len(pos_sentencas.values())):
            inicio_sub_sent = posicoes[i][0]
            fim_sub_sent = posicoes[i][1]
            
            if inicio_sub_sent is not None and fim_sub_sent is not None:
                if inicio < inicio_sub_sent and fim > fim_sub_sent:
                    pos_inico_sub = localizar_chave_tokens(sentenca, inicio_sub_sent)
                    pos_final_sub = localizar_chave_tokens(sentenca, fim_sub_sent)+1

                    adicionar = pos_sentencas[(inicio_sub_sent,fim_sub_sent)]

                    sentenca = sentenca[:pos_inico_sub] + [adicionar]  + sentenca[pos_final_sub:]

        pos_sentencas[(inicio,fim)] = ("", formatar_sentenca(sentenca),"SENT")

    return list(pos_sentencas.values())[-1][1]

if __name__ == "__main__":
    from analisador_lexico import *
    from analisador_sintatico import *

    string = input("Digite uma sentença lógica: ")
    string = "(" + string + ")"

    valido, lista_simbolos = identificar_tokens(string, padrao_tokens)

    posicoes = identificar_sentencas(lista_simbolos)
    print(criar_expressao(lista_simbolos,posicoes))