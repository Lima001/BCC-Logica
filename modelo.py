from analisador_lexico import *
from analisador_sintatico import *
from criador_expressao import *
from avaliador_expressao import *

def limpar_tela():
    print("\n"*80)

def imprimir_menu():
    limpar_tela()
    
    print("Menu")
    print("-"*15)
    print("0 -> Sair")
    print("1 -> Encontrar Modelo")
    print("2 -> Ajuda")
    print("-"*15, end="\n"*2)

def imprimir_ajuda():
    limpar_tela()
    
    print("Ajuda", end="\n"*2)
    
    print("Sobre:")
    print("-- Esse programa tem como propósito aplicar conhecimentos adquiridos")
    print("-- sobre consistência e modelos no estudo da lógica proposicional", end="\n"*2)
    
    print("Como funciona:")
    print("-- Após escolher a opção de gerar a tabela, o programa irá solicitar")
    print("-- uma sentença da lógica proposicional para avaliar.")
    print("-- Em caso de algum erro, o programa irá retornar")
    print("-- uma mensagem avisando o problema encontrado.", end="\n"*2)

    print("Formato da Sentença Lógica")
    print("-- A sentença lógica deve seguir o seguinte formato:")
    print("-- Sentenças Atômicas devem ser compostas por letras e números")
    print("--   sendo que deve sempre iniciar com uma letra;")
    print("-- Deve-se fazer o uso de parênteses para identificar sentenaças")
    print("--   compostas;")
    print("-- Os símbolos para os conectivos aceitos são:")
    print("--   ~ para negação")
    print("--   & para conjunção (E lógico)")
    print("--   | para a disjunção (OU lógico)")
    print("--   -> para a condicional (Implicação)")
    print("--   <-> para a bicondicional (Dupla implicação)")
    print("-- Exemplos de sentenças aceitas")
    print("--   X")
    print("--   ~X")
    print("--   (X&Y)")
    print("--   ~(X|Y)")
    print("--   (X->Y) & ~Y", end="\n"*3)

def pegar_sentencas():
    qtd_sentencas = int(input("Quantas sentencas pertencem ao conjunto: "))
    if qtd_sentencas <= 0:
        print("Quantidade de sentencas inválida")
        return None

    sentencas = []

    for i in range(qtd_sentencas):
        string = input(f"Digite a {i+1}º Sentença: ")
        string = "(" + string + ")"
        sentencas.append(string)

    return sentencas

def formatar_sentenca(*sentencas):
    sentenca_formatada = "("
    
    sentenca_formatada += sentencas[0]
    for i in sentencas[1:]:
        sentenca_formatada += " & " + i

    sentenca_formatada += ")"

    return sentenca_formatada


if __name__ == "__main__":
    executar = True
    while executar:
        imprimir_menu()
        
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 0:
            executar = False

        elif opcao == 1:
            sentencas = pegar_sentencas()

            if sentencas is not None:

                sentenca = formatar_sentenca(*sentencas)

                lista_simbolos = realizar_analise_lexica(sentenca)
        
                if lista_simbolos is not None:
                    posicoes = realizar_analise_sintatica(lista_simbolos)

                    if posicoes is not None:
                        expressao = criar_expressao(lista_simbolos, posicoes)
                        resultado = achar_modelo(expressao, lista_simbolos)

                        if resultado[0]:
                            print("Conjunto de Sentenças Consistente")
                            print("Modelo:")
                            for casos in resultado[1]:
                                for atom, valor in casos:
                                    print(f"{atom}:{int(valor)}", end="; ")
                                print()
                            print()

                        else:
                            print("Conjunto de Sentenças Inconsistente!\n")

        elif opcao == 2:
            imprimir_ajuda()

        else:
            print("Opção Inválida!")

        trava = input("Pressione Enter para continuar...") 