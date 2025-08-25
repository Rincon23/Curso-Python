"""
Style
0 none
1 bold (negrito)
4 underline (sublinhar)
7 negative

text
30 branco
31 vermelho
32 verde
33 amarelo
34 azul
35 magenta
36 ciano
37 cinza

back
40 branco
41 vermelho
42 verde
43 amarelo
44 azul
45 magenta
46 ciano
47 cinza
"""

print('\033[4;34;47mOlá Mundo! \033[m')

nome = 'Enzo'
cores = {'limpa':'\033[m',
            'azul':'\033[34m', 
            'amarelo':'\033[33m', 
            'pretoebranco':'\033[7;30m'}
print('Olá {}{}{}'.format('\033[34m',nome,'\033[m'))

print('Olá {}{}{}'.format(cores['pretoebranco'],nome,cores['limpa']))