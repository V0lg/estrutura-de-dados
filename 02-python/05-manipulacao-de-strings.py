# atribuindo uma string a uma variável.
palavra = "casaco"
print(palavra)

# função .upper() retorna a string em maiúsculo.
maiusculo = palavra.upper()
print(maiusculo)

# função .lower() retorna a string em minúsculo.
minusculo = maiusculo.lower()
print(minusculo)

# função .capitalize() retorna a string com a primeira letra em maiúsculo. 
capital = minusculo.capitalize()
print(capital)

# podemos percorrer uma string a partir de um numero01 até o numero anterior ao numero2 [numero01:numero02].
# strings são indexadas, seus indices começam a partir do número 0.
parte_palavra = palavra[0:3] # retorna as 3 primeiras letras.
outra_parte = palavra[3:] # retorna a partir do indice 3 até o final da string.

print("primeira parte:", parte_palavra, "segunda parte:", outra_parte)

# posso pegar uma parte da minha string e trocar por outra. 
nova_palavra = palavra.replace("aco", "inha") # substitui a ocorrência de aco por inha e retorna uma nova string.
print("palavra antiga:", palavra, "nova palavra:", nova_palavra)

# temos que a substituição de todas as ocorrências, não somente da primeira.
outra_nova_palavra = palavra.replace('c', 'a')
print(outra_nova_palavra)

# podemos procurar por um caractere dentro de uma string utilizando a função .find(), temos como retorno o indice.
# caso não seja encontrada temos como retorno -1, também temos que o indice retornado é o primeiro encontrado.
indice = palavra.find('a') 
indice2 = palavra.find('t') 
print(indice, indice2)

# podemos obter o tamanho de uma string por meio da função len(), espaços vazios são contados como caracteres.
tamanho_string = len(" palavra ")
print(tamanho_string)

# utilizando a função .strip() podemos remover os espaços em brancos.
palavra_com_espacos = " palavra "
print(palavra_com_espacos)
removendo_espacos = palavra_com_espacos.strip()
print(removendo_espacos)

# formatando texto e utilizando interpolação de variáveis.
n1 = 14
n2 = 16

print(f"dividindo {n1} por {n2} = {n1 / n2}")