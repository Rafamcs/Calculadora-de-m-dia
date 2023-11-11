"""
script feito em Python 3.9
"""
import os

aprovados = []
reprovados = []

while True:
    aluno = str(input("Nome do aluno: "))

    while True:
        try:
            aop1 = float(input("Atividade Online Pontuada 1: "))
            if not 0 <= aop1 <= 1:
                os.system('clear') or None
                raise ValueError("Nota inválida")
            break
        except ValueError as error:
            print(error)

    while True:
        try:
            aop2 = float(input("Atividade Online Pontuada 2: "))
            if not 0 <= aop2 <= 2:
                os.system('clear') or None
                raise ValueError("Nota inválida")
            break
        except ValueError as error:
            print(error)

    while True:
        try:
            aop3 = float(input("Atividade Online Pontuada 3: "))
            if not 0 <= aop3 <= 1:
                os.system('clear') or None
                raise ValueError("Nota inválida")
            break
        except ValueError as error:
            print(error)

    while True:
        try:
            prova = float(input("Prova: "))
            if not 0 <= prova <= 6:
                os.system('clear') or None
                raise ValueError("Nota inválida")
            break
        except ValueError as error:
            print(error)

    media_modulo = aop1 + aop2 + aop3 + prova

    if (media_modulo >= 7):
        print("O aluno {} foi APROVADO com {} pontos".format(aluno, media_modulo))
        aprovados.append(aluno)
    else:
        print("O aluno {} foi REPROVADO com {} pontos, e precisa fazer a recuperação.".format(aluno, media_modulo))

        while True:
            try:
                recuperacao = float(input("Nota Recuperação: "))
                if not 0 <= recuperacao <= 10:
                    os.system('clear') or None
                    raise ValueError("Nota inválida")
                break
            except ValueError as error:
                print(error)

        media_geral = (media_modulo + recuperacao) / 2

        if (media_geral >= 5):
            print("O aluno {} foi APROVADO com {} de média geral".format(aluno, media_geral))
            aprovados.append(aluno)
        else:
            print("O aluno {} REPROVOU na recuperação com {} de média geral".format(aluno, media_geral))
            reprovados.append(aluno)

    print("-" * 48)

    continuar = str(input("Gostaria de calcular mais uma nota? [S/n] "))

    if(continuar == "n"):
        break

    print("-" * 48)

os.system('clear') or None

total_alunos = len(aprovados) + len(reprovados)
aprovados_pcento = (100 / total_alunos) * len(aprovados)
reprovados_pcento = (100 / total_alunos) * len(reprovados)

print("-" * 58)
print("{:.2f}% alunos foram APROVADOS e {:.2f}% ficaram REPROVADOS".format(aprovados_pcento, reprovados_pcento))
print("-" * 58)
