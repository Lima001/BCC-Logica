def conj(*sentencas):
    valor_logico = sentencas[0]
    for i in range(1,len(sentencas)):
        valor_logico = valor_logico and sentencas[i]

    return valor_logico

def disj(*sentencas):
    valor_logico = sentencas[0]
    for i in range(1,len(sentencas)):
        valor_logico = valor_logico or sentencas[i]

    return valor_logico

def neg(sentenca):
    return not sentenca

def cond(sentenca1, sentenca2):
    return not(sentenca1) or sentenca2

def bicon(sentenca1, sentenca2):
    return (not(sentenca1) or sentenca2) and (not(sentenca2) or sentenca1)

def gerar_valores_logicos(lista_tokens):
    atoms = []

    for i in lista_tokens:
        if i[2] == "ATOM" and i[1] not in atoms:
            atoms.append(i[1])
    
    qtd_linhas = 2 ** len(atoms)
    alternar = qtd_linhas/2

    atoms_logicos = []

    for i in atoms:
        valores = []
        valor = False
        
        while len(valores) < qtd_linhas:
            valores.append(valor)
            if len(valores) % alternar == 0:
                valor = not valor
        
        atoms_logicos.append((i,valores))
        alternar /= 2

    return atoms_logicos

def gerar_tabela_verdade(expressao, lista_tokens):
    sentencas_atomicas = gerar_valores_logicos(lista_tokens)
    tabela_verdade = []

    for i in range(len(sentencas_atomicas[0][1])):
        for j in range(len(sentencas_atomicas)):

            executar = f"{sentencas_atomicas[j][0]}={sentencas_atomicas[j][1][i]}"
            exec(executar)

        tabela_verdade.append(eval(expressao))

    return (sentencas_atomicas,tabela_verdade)

def achar_contra_exemplo(tabela):
    contraexemplo = []
    atoms = tabela[0]
    sentenca = tabela[1]

    for i in range(len(sentenca)):
        if sentenca[i] == 0:
            caso = []
            for a in atoms:
                caso.append((a[0],a[1][i]))
            
            contraexemplo.append(caso)

    return contraexemplo

def verificar_validade(expressao, lista_tokens):
    tabela = gerar_tabela_verdade(expressao, lista_tokens)

    contraexemplo = achar_contra_exemplo(tabela)
    
    if len(contraexemplo) == 0:
        return (True, None)
    
    else:
        lista_contraexemplos = []

        for c in contraexemplo:
            caso = []
            for atom, valor in c:
                caso.append((atom, int(valor)))
            
            lista_contraexemplos.append(caso)

        return (False, lista_contraexemplos)

def achar_modelo(expressao, lista_tokens):
    tabela_verdade = gerar_tabela_verdade(expressao, lista_tokens)

    modelo = []

    for i in range(len(tabela_verdade[1])):

        if tabela_verdade[1][i]:
            caso = []

            for atom in tabela_verdade[0]:
                caso.append((atom[0], atom[1][i]))

            modelo.append(caso)

    if len(modelo) != 0:
        return (True, modelo)

    return (False, None)