#Exercício 2
#Crie um programa que permita a um professor registrar as notas de uma turma.
#O programa deve continuar solicitando notas até que o professor digite 'fim'.
#Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando.
#No final, deve exibir a média da turma.

notas_lista = []
while True:
    try:
        entrada = input("Digite a nota do aluno ou digite 'fim' para encerrar: ")
        if entrada == "fim":
            break
        
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas_lista.append(nota)
        else:
            print("Nota inválida. Digite um valor ntre 0 e 10.")
            continue
    except ValueError:
        print("Entrada inválida. Por favor digite um número ou 'fim'.")
    
if notas_lista:
    media = sum(notas_lista) / len(notas_lista)
    print(f"\nMédia da turma: {media:.2f}")
    print(f"Total de notas válidas é: {len(notas_lista)}")
else:
    print("Nenhuma nota válida foi registrada.")