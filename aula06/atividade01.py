# Desenvolva um algoritimo que receba 4 notas de cada aluno e calcule a média.
# As notas devem ser informadas pelo usuário.
# O programa deve realizar esse cálculo para 10 alunos e, ao final, exibir a média correspondente.

for n in range(10):
    print(f'\nAluno {n+1}')
    nt1 = float(input('Informe a primeira nota: '))
    nt2 = float(input('Informe a segunda nota: '))
    nt3 = float(input('Informe a terceira nota: '))
    nt4 = float(input('Informe a quarta nota: '))

    media = (nt1 + nt2 + nt3 + nt4) / 4

    print(f'A média foi de: {media}')