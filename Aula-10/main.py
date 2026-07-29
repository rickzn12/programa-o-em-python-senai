#1

contador = 1 
 
while contador <= 1000:
    print("Numero: ", contador)
    contador += 1 



#2
SENHA_CORRETA = "1234"

tentativas = 0
autenticado = False

while tentativas < 3:
    senha = input("Digite a senha do professor: ")
    if senha == SENHA_CORRETA:
        autenticado = True
        print("\nAcesso permitido! Bem-vindo ao sistema de notas.\n")
        break
    else:
        tentativas += 1
        chances_restantes = 3 - tentativas
        if chances_restantes > 0:
            print(f"Senha incorreta! Você ainda tem {chances_restantes} tentativa(s).\n")
        else:
            print("\nConta bloqueada! (senha incorreta atingiu o limite de 3 tentativas)")

if autenticado:
    notas = []
    
    qtd_notas = int(input("Quantas notas deseja inserir? "))
    
    for i in range(qtd_notas):
        nota = float(input(f"Digite a {i + 1}ª nota: "))
        notas.append(nota)
    
    if len(notas) > 0:
        media = sum(notas) / len(notas)
        print("\n--- RESUMO DAS NOTAS ---")
        print(f"Notas inseridas: {notas}")
        print(f"Média do aluno: {media:.2f}")

input('Digite enter para sair: ')