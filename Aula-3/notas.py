# OBJETIVO - FAZER A MÉDIA DAS 3 NOTAS DE UM ALUNO, PARA PASSAR,O ALUNO PRECISA ALCANÇAR >=7 (PASSAR), >=5 E  <7 RECUPERAÇÃO, <5 (REPROVADO).   


nota_1 = 10
nota_2 = 6
nota_3 = 9


media = (nota_1 + nota_2 + nota_3)/3
print('NOTA:')
print(round(media, 2))


aprovado = media >= 7
recuperacao =  media >= 5 and media < 7
reprovado = media < 5


resultado =  (media >=7 and print('Aprovado')) or  (media >=5 and media < 7 and print('Recuperação')) or (media <5 and print('reprovado'))  


# print('situação do aluno: ')
# print('Aprovado:')
# print(aprovado)
# print('Recuperação:')
# print(recuperacao)
# print('Reprovado:')
# print(reprovado)



