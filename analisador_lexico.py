import re

padrao_tokens = [
    (r'\b[a-zA-Z]+[a-zA-Z0-9]*', "ATOM"),
    (r'~', "OPUN"),
    (r'\&|\||->|<->', "OPBIN"),
    (r'\(', "LPAREN"),
    (r'\)', "RPAREN"),
    (r'\s',"IGNOR")
]

def identificar_tokens(string, padrao_tokens):
    lista_tokens = []
    simbolos_validos = "" 
    
    for i in range(len(padrao_tokens)):
        regex = padrao_tokens[i][0]
        match = re.finditer(regex, string)
        
        for m in match:
            elemento = (m.span()[0], m.group(), padrao_tokens[i][1])
            
            if i != len(padrao_tokens)-1:
                lista_tokens.append(elemento)
            
            simbolos_validos += m.group()
    
    if len(simbolos_validos) == len(string):
        lista_tokens = sorted(lista_tokens, key=lambda elemento: elemento[0])
        return (True, lista_tokens)
    
    else:
        return (False,None)


def realizar_analise_lexica(string):
    valido, lista_simbolos = identificar_tokens(string, padrao_tokens)
    
    if valido:
        return lista_simbolos

    else:
        print("Ocorrência de símbolos inválidos...")
        return None

if __name__ == "__main__":
    string = input("Digite uma sentença lógica: ")
    string = "(" + string + ")"

    resultado = realizar_analise_lexica(string)

    if resultado is not None:
        for token in resultado:
            print(token) 