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
    print("1 -> Verificar Argumento Válido")
    print("2 -> Ajuda")
    print("-"*15, end="\n"*2)

def imprimir_ajuda():
    limpar_tela()
    
    print("Ajuda", end="\n"*2)
    
    print("Sobre:")
    print("-- Esse programa tem como propósito aplicar conhecimentos adquiridos")
    print("-- sobre validade de argumentos no estudo da lógica proposicional", end="\n"*2)
    
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

def pegar_premissas():
    qtd_premissas = int(input("Quantas premissas (Ao menos 1): "))
    if qtd_premissas <= 0:
        print("Quantidade de premissas inválida")
        return None

    premissas = []

    for i in range(qtd_premissas):
        string = input(f"Digite a {i+1}º premissa: ")
        string = "(" + string + ")"
        premissas.append(string)

    return premissas

def formatar_argumento(premissas, conclusao):
    sentenca = "("
    for i in range(len(premissas)-1):
        sentenca += premissas[i] + " & "
    
    sentenca += premissas[-1] + ")"
    sentenca += "->" + conclusao
    
    sentenca = "(" + sentenca + ")"

    return sentenca

if __name__ == "__main__":
    executar = True
    while executar:
        imprimir_menu()
        
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 0:
            executar = False

        elif opcao == 1:
            premissas = pegar_premissas()

            if premissas is not None:
                conclusao = input("Digite a conclusão: ")
                conclusao =  "(" + conclusao + ")"

                sentenca = formatar_argumento(premissas, conclusao)

                lista_simbolos = realizar_analise_lexica(sentenca)
        
                if lista_simbolos is not None:
                    posicoes = realizar_analise_sintatica(lista_simbolos)

                    if posicoes is not None:
                        expressao = criar_expressao(lista_simbolos, posicoes)
                        resultado = verificar_validade(expressao, lista_simbolos)

                        if resultado[0]:
                            print("Argumento Válido")

                        else:
                            print("Argumento Inválido")
                            for contraexemplo in resultado[1]:
                                for atom in contraexemplo:
                                    print(f"{atom[0]}:{atom[1]}", end="; ")
                                print()
                            print()
                    else:
                        print("Erro!")
                
                else:
                    print("Erro!")
                            

        elif opcao == 2:
            imprimir_ajuda()

        else:
            print("Opção Inválida!")

        trava = input("Pressione Enter para continuar...") 