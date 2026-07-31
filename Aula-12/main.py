def comparar(numero1, numero2):
    if numero1 % 2 == 0:
        print(numero1, ' E par')
    else:
        print(numero1, 'E impar')

    if numero2 % 2 == 0:
        print(numero2, 'E par')
    else:
        print(numero2, 'E impar')

n1 = int(input('Digite o pimeriro numero: '))
n2 = int(input('Digite o segundo numero: '))

comparar(n1, n2)

#2 

def multiplicar(a, b, c):
    resultado = a * b * c
    print('resultado', resultado)

n3 = int(input('Digite o primero numero: '))
n4 = int(input('Digite o segundo numero: '))
n5 = int(input('Digite o terceiro numero: '))

multiplicar(n3, n4, n5)

#3

def potencia(base, expoente):
    resultado = base ** expoente
    print('resultado', resultado)

base = int(input('Digite sua base: '))
expoente = int(input('Digite sue expoente; '))

potencia(base, expoente)

#4

def verificar_idade(idade):
    if idade == 18:
        print('Parabens! Voce tem 18 anos.')
    else:
        print('Idade indiferente de 18 anos')

idade = int(input('Digite sua idade: '))

verificar_idade(idade)

#5

def idade(ano_nascimento):
    ano_atual = 2026
    idade = ano_atual - ano_nascimento
    print('Sua idade e:', idade)

ano = int(input('Digite seu ano de nascimento: '))

idade(ano)

#6

def copa():
    print("Não. O Brasil não ganhou a copa de 1999")

copa()

#7

def aceno():
    print('Bem-vidno ao restaurante')

def restaurante():
    print("1 - Salada")
    print("2 - Macarronada")
    print("3 - carne")
    print("4 - bolo")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Voce escolheu salada")
    if opcao == 2:
        print("Voce escolheu macarronada")
    if opcao == 3:
        print("Voce escolheu sanduiche")
    if opcao == 4:
        print("Voce escolheu sorvete")

aceno()
restaurante()