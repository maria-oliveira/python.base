"""
Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentas cada uma das atividades.

"""
#Dados
sala1 = ['Erik', 'Maia', 'Gustavo', 'Manuel', 'Sofia', 'Joana']
sala2 = ['Joao', 'Antonio', 'Pedro', 'Carlos', 'Maria']

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Aula de Ingles", aula_ingles), 
    ("Aula de musica",  aula_musica),
    ("Aula de danca", aula_danca),
 ]

#listar alunos de cada atividade por sala
for nome_aula, atividade in atividades: 
     print(f"\nAlunos da {nome_aula}:")

     atividade_sala1 = []
     atividade_sala2 = []

     for aluno in atividade :
        if aluno in sala1:
           atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)

     print (f"  Sala 1: {atividade_sala1}")
     print (f"  Sala 2: {atividade_sala2}")