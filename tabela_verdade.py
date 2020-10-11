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
    print("1 -> Gerar Tabela Verdade")
    print("2 -> Ajuda")
    print("-"*15, end="\n"*2)

def imprimir_ajuda():
    limpar_tela()
    
    print("Ajuda", end="\n"*2)
    
    print("Sobre:")
    print("-- Esse programa tem como propósito aplicar conhecimentos adquiridos")
    print("-- sobre tabelas verdade no estudo da lógica proposicional", end="\n"*2)
    
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

def imprimir_tabela_verdade(tabela, string):
    atoms = tabela[0]
    sentenca = tabela[1]

    for i in range(len(atoms)):
        print(atoms[i][0], end=" -- ")
    print(string)

    for i in range(len(atoms[0][1])):
        for j in range(len(atoms)):
            print(int(atoms[j][1][i]), end=f"{len(atoms[j][0])*' '}-- ")
        
        print(int(sentenca[i]))

    print()

if __name__ == "__main__":
    executar = True
    while executar:
        imprimir_menu()
        
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 0:
            executar = False

        elif opcao == 1:
            sentenca = "(" + input("Digite a senteça lógica: ") + ")"
            lista_simbolos = realizar_analise_lexica(sentenca)

            if lista_simbolos is not None:
                posicoes = realizar_analise_sintatica(lista_simbolos)

                if posicoes is not None:
                    expressao = criar_expressao(lista_simbolos, posicoes)
                    tabela_verdade = gerar_tabela_verdade(expressao, lista_simbolos)
                    #print(tabela_verdade)
                    imprimir_tabela_verdade(tabela_verdade, sentenca)
                
                else:
                    print("Erro!")
            
            else:
                print("Erro!")

        elif opcao == 2:
            imprimir_ajuda()

        else:
            print("Opção Inválida!")

        trava = input("Pressione Enter para continuar...") 