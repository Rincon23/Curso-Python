# Variaveis 
nome = 'Enzo'
idade = 21
peso = 80
print(nome,idade,peso)

#Tipos de váriaveis
int 7 -4 0
float 4.5 0.03 -15.2345 7.0
bool True False
str (String) 'olá' '7.5' ''

#para testar o tipo
print(type(n))
n = input('Digite algo ')
print(n.isnumeric())
n.isalpha()
n.isalnum()
n.isupper()
n.islower()

#Aula 4

#.format
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2

print('A soma entre {} e {} vale {}'.format(n1,n2,s))

#Aula 7

#Operadores aritiméticos

+ adição
- subtração
* multiplicação
/ divisão
** potência
// divisão inteira
% Resto da divisão

#ordem de precendência

1. ()
2. **
3. * / // %
4. + -

#Print e .format

print('=' *5)
=====

print('Olá', end=' ')
print('Mundo!')
Olá Mundo!

print('Olá\nMundo')
Olá
Mundo!

nome = 'enzo'
print('Prazer em te conhecer {:5}!'.format(nome))
print('Prazer em te conhecer {:>5}!'.format(nome))
print('Prazer em te conhecer {:^5}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))
Prazer em te conhecer enzo                !
Prazer em te conhecer                 enzo!
Prazer em te conhecer         enzo        !
Prazer em te conhecer ========enzo========!

div = 5/3
print('A divisao vale {:.3f}'.format(div))
A divisao vale 1.667

# Aula 8

# math

import math
from math import ceil, floor, trunc, sqrt, factorial

ceil        arredondamento para cima
floor       arredondamen para
trunc       retita a , para frente
pow         potencia
sqrt        raiz quadrada
factorial   fatorial

raiz = math.sqrt

#Random

import random
num = random.random()
print(num)
numero aleatório de 0 a 1

n2 = random.randint(1,10)
print('numero de 1 a 10: {}'.format(n2))


from random import choice

nome = choice(['Enzo','Jão'])
print('O escolhido foi', nome)


from random import sample

ordem = sample(['Enzo','Jão','Gau'], k=3)

print('A ordem de apresentação é:', ordem)
['Enzo', 'Gau', 'Jão']

#Aula 9

#Fatiamento

frase = 'Curso em video Python'
print(frase[9])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

v
video Python
vdoPto
Curso
Python
vePh

#Análise

frase = 'Curso em video Python'

print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,13)) #com fatiamento
print(frase.find('deo')) #mostra a posição em que começou
print(frase.find('Java'))
print('Curso' in frase)

21
3
1
11
-1
True

#Transformação

frase = 'Curso em video Python'

print(frase.replace('Python', 'Java'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

Curso em video Java
CURSO EM VIDEO PYTHON
curso em video python
Curso em video python
Curso Em Video Python

frase2 = '   Aprenda Python  '

print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())

Aprenda Python
   Aprenda Python
Aprenda Python


#Divisão e junção

frase = 'Curso em video Python'
print(frase.split())
['Curso', 'em', 'video', 'Python']

frase = 'Curso em video Python'
print(frase.split())
print(frase.split()[0])
print(frase.split()[0][1]) #1° palavra 2° letra 
['Curso', 'em', 'video', 'Python']
Curso
u

frasejunta = frase.split()
print('-'.join(frasejunta))
Curso-em-video-Python

#print

print("""Olá
Mundo,
Tudo
Bem?""")

Olá 
Mundo, 
Tudo 
Bem?


