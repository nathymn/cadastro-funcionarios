"""
Criar um programa que cadastre funcionário de um empresa e seus dependentes. O funcionário deve ser cadastrado com
matrícula, nome e dependentes. Os dependentes devem ser inseridos dinamicamente em uma tupla. Dica: usar o operador +=
"""
#Variáveis
cad_func = []
while True:
    nome = input("Digite seu nome: ")
    mat = input("Digite sua matrícula: ")
    n_dep = int(input("Quantos dependentes tem? "))
    func = (nome, mat)
    dependentes = tuple()
    for dep in range(1, n_dep+1):
        dependente = input(f"Digite o nome do dependente {dep}: ")
        dependentes += (dependente,)
    func += dependentes
    cad_func.append(func)
    resp = input("Deseja cadastrar outro funcionário (s/n)? ")
    if resp == 'n':
        break
for func in cad_func:
    print(f"\nFuncionário {func[0]}")
    print(f"Matrícula: {func[1]}")
    print(f"Dependentes: {func[2]}\n")





