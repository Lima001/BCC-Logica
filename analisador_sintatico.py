def identificar_sentencas(lista_tokens):
    posicoes = []
    pilha = []

    for i in range(len(lista_tokens)):
        if lista_tokens[i][2] == "LPAREN":
            pilha.append(lista_tokens[i][0])
        
        elif lista_tokens[i][2] == "RPAREN":
            if len(pilha) == 0:
                #print("ERRO: Parênteses sem abertura!!!")
                return None
            else:
                posicoes.append((pilha.pop(),lista_tokens[i][0]))
    
    if len(pilha) == 0:
        #print("ERRO: Parênteses sem Fechamento!!!")
        return posicoes
    return None

def validar_sintaxe(lista_tokens):
    
    def verificar_sentenca_atomica(lista_tokens):
        operador = 0
        atom = 0

        for i in lista_tokens:
            if i[2] == "OPBIN" or i[2] == "OPUN":
                operador += 1
            elif i[2] == "ATOM" or i[2] == "SENT":
                atom += 1

        return operador == 0 and atom == 1

    def validar_operador(lista_tokens):
        operador_bin = []
        operador_un = []

        for i in lista_tokens:
            if i[2] == "OPBIN":
                operador_bin.append(i[1])
            elif i[2] == "OPUN":
                operador_un.append(i[1])
        
        if len(set(operador_bin)) == 0:
            return len(operador_un) != 0
        
        if len(set(operador_bin)) == 1:
            if len(operador_bin) == 1:
                return True
            else:
                return operador_bin[0] in ["|","&"]
        return False

    def validar_ordem_simbolos(lista_tokens):
        for i in range(len(lista_tokens)):
            if lista_tokens[i][2] == "OPUN":
                try:
                    if lista_tokens[i+1][2] == "OPUN" or lista_tokens[i+1][2] == "ATOM" or lista_tokens[i+1][2] == "SENT":
                        pass
                    else:
                        return False 
                except:
                    return False
            
            elif lista_tokens[i][2] == "OPBIN":
                try:
                    if lista_tokens[i-1][2] == "ATOM" or lista_tokens[i-1][2] == "SENT":
                        if lista_tokens[i+1][2] == "ATOM" or lista_tokens[i+1][2] == "OPUN" or lista_tokens[i+1][2] == "SENT":
                            pass
                        else:
                            return False
                    else:
                        return False
                except:
                    return False
        
        return True
    
    if verificar_sentenca_atomica(lista_tokens):
        return True
    else:
        return validar_operador(lista_tokens) and validar_ordem_simbolos(lista_tokens)

def localizar_chave_tokens(lista_tokens, chave):
    for i in range(len(lista_tokens)):
        if lista_tokens[i][0] == chave:
            return i
    return None

def verificar_sentenca_valida(lista_tokens, posicoes):
    sentencas_validas = []

    for i in range(len(posicoes)):
        inicio, fim = posicoes[i]
        pos_inicio = localizar_chave_tokens(lista_tokens, inicio)
        pos_final = localizar_chave_tokens(lista_tokens, fim)
        
        sentenca = lista_tokens[pos_inicio:pos_final+1]

        inicio_sub_sent, fim_sub_sent = None, None

        for i in range(len(sentencas_validas)):
            inicio_sub_sent = sentencas_validas[i][0]
            fim_sub_sent = sentencas_validas[i][1]

            if inicio_sub_sent is not None and fim_sub_sent is not None:
                if inicio < inicio_sub_sent and fim > fim_sub_sent:
                    ponto1 = localizar_chave_tokens(sentenca, inicio_sub_sent)
                    ponto2 = localizar_chave_tokens(sentenca, fim_sub_sent)+1
                    
                    sentenca = sentenca[:ponto1] + [("SENT","SENT","SENT")] + sentenca[ponto2:]
        
        if validar_sintaxe(sentenca):
            sentencas_validas.append((inicio,fim))

    if sentencas_validas == posicoes:
        return True
    return False

def realizar_analise_sintatica(lista_simbolos):
    posicoes_sentencas = identificar_sentencas(lista_simbolos)

    if posicoes_sentencas is None:
        print("ERRO DE SINTAXE!")
        return None

    else:
        if verificar_sentenca_valida(lista_simbolos, posicoes_sentencas):
            return posicoes_sentencas
        else:
            print("ERRO DE SINTAXE")
            return None

if __name__ == "__main__":
    from analisador_lexico import *
    
    string = input("Digite uma sentença lógica: ")
    string = "(" + string + ")"

    resultado_lexico = realizar_analise_lexica(string)

    if resultado_lexico is not None:
        resultado_sintatico = realizar_analise_sintatica(resultado_lexico)

        if resultado_sintatico is not None:
            for pos in resultado_sintatico:
                print(pos, resultado_lexico[pos[0]:pos[1]+1])