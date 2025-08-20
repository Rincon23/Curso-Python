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




