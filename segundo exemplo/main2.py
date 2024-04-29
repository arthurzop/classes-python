from pessoa import pessoa
from professor import professor
from estudante import estudante

prof1 = professor('Jonas', 35, 'FPOO')
prof1.dar_aula()

print('-' * 30)

estudante1 = estudante('James', 19, 'Python')
estudante1.apresentar()

print('-' * 30)

pessoa1 = pessoa('Pedro', 22)
pessoa1.apresentar()