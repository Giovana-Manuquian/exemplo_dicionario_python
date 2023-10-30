agenda = {'nome':'Sarah', 'phone':'1234-5678', 'email':'Sarah@gmail.com', 'idade':'65'}

for dicionario in agenda.keys():
    print(agenda[dicionario])

frutas = print(['laranja', 'banana', 'pera'])

frutas1 = {'maçã' : 3, 'banana' : 5, 'laranja' : 2}
#cria um dicionário chamado 'frutas' com pares chave-valor iniciais.

frutas1['uva'] = 4
#adiciona a chave 'uva' com o valor 4 ao dicionário 'frutas'

frutas1['maçã'] = 6
#atualiza o valor da chave 'maçã' para 6 no dicionário 'frutas'

print(frutas1['banana'])
#printa o valor associado à chave 'banana'.

del frutas1['laranja']
#remove a chave 'laranja' e seu valor do dicionário 'frutas'

if 'uva' in frutas1:
    print('A chave 'uva' está no dicionário')
#verifica se a chave 'uva' existe no dicionário 'frutas' e printa a mensagem.

for chave, valor in frutas1.items():
    print(f'{chave} : {valor}')
#percorre o dicionário 'frutas', imprimindo pares chave-valor

"""print(agenda['idade'])
print(agenda.keys()) #lista as chaves
print(agenda.values()) #lista os valores"""

"""Tuplas e List

*Tuplas não podem ser alteradas, se forem alteradas, cria-se uma nova tupla (elas são imutáveis).

list = []
tuplas = ()
dicionario = {}

dicionario = {'nome': 'Ana', 'idade': '23', 'celular': '1234-5678'} """
