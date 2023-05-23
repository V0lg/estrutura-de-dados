# por meio de variáveis que um algoritmo "guarda" os dados do programa.
# em python não temos como declarar constantes.

'''
    tipos de variáveis:
        inteiros: valores positivos ou negativos, que não possuem uma parte fracionária. exemplos: -10, 0, 10.
        float("real"): valores positivos ou negativos, que podem possuir uma parte fracionária. exemplos: -10.0, 0.0, 10.0, 1.3
        caracteres(char ou string): qualquer elemento presente no teclado. exemplos: 'M', 'F', "Maria", "Joao".
        lógico(booleano): verdadeiro ou falso, exemplos: true, false, 0, 1. 

        char: corresponde a um único caractere.
        string: conjunto de caracteres.
'''

# variáveis inteiras 
numero = -3
numero_jogos = 14
numero_convidados = 15 

print(type(numero), type(numero_jogos), type(numero_convidados))
print(numero, numero_jogos, numero_convidados)

# variáveis float (ponto flutuante)
pi = 3.1415
numero_euler = 2.71
escala_terremoto = -4.55

print(type(pi), type(numero_euler), type(escala_terremoto))
print(pi, numero_euler, escala_terremoto)

# strings e char 
letra = 'a' 
palavra1 = "linguagem de programacao"
palavra2 = "python"

# "concatenação"
print(type(letra), type(palavra1), type(palavra2))
print("estou aprendendo uma", palavra1)
print("esta", palavra1, "se chama", palavra2)

# recebendo dados. o input armazena o que foi digitado como uma string, para modificar precisamos fazer uma conversão para o tipo desejado.
nome = input("Digite seu nome: ")
# no caso abaixo estamos fazendo uma conversão para inteiro.
idade = int(input("Digite sua idade: "))
print("tipo da variavel nome =", type(nome))
print("tipo da variavel idade =", type(idade))
print(nome, "sua idade e igual a", idade)