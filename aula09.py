repositorio = [
    {
        'matrícula': 1,
        'nome': 'Jonas',
        'idade': 29,
        'nota': 8.7,
    }
]

matriculaAtual = 1

#menu de navegação
while True:
    print('---BEM VINDO AO MENU---')
    print('1 - Cadastrar aluno')
    print('2 - Listar todos')
    print('3 - Pesquisar alunos')
    print('4 - editar aluno')
    print('5 - Excluir aluno')
    print('6 - Sair')
    opcao = input('Digite opção desejada: ')

    if opcao == '6':
       print('Você saiu do sistema...')

       break
    elif opcao == '1':
        matriculaAtual += 1
        nome  = input('Digite o nome do aluno:')
        idade = int(input('Digite a Idade do aluno: '))
        nota = float(input('Digite a nota do aluno: '))
        aluno = {
            'matrícula': matriculaAtual,
            'nome': nome,
            'idade': idade,
            'nota': nota,
        }
        repositorio.append(aluno)
        print('Aluno cadastrado com sucesso!')
    
    elif opcao == '2':
        print('---ALUNOS MATRICULADOS---')
        for aluno in repositorio:
            print(f'Matrícula: {aluno["matrícula"]}')
            print(f'Nome: {aluno["nome"]}')
            print(f'Idade: {aluno["idade"]}')
            print(f'Nota: {aluno["nota"]}')
            print('-'*50)
    
    elif opcao == '3':
        matricula = int(input('digite a matricula do aluno: '))
        print('-' * 50)
        for aluno in repositorio:
            if aluno['matrícula'] == matricula:
                print(f'Matrícula: {aluno["matrícula"]}')
                print(f'Nome: {aluno["nome"]}')
                print(f'Idade: {aluno["idade"]}')
                print(f'Nota: {aluno["nota"]}')
                print('-'*50)
                break
        else:
            print('Aluno não encontrado!')    

    elif opcao == '4':
        matricula = int(input('digite a matricula do aluno: '))
        print('-' * 50)

        for aluno in repositorio:
            if aluno['matrícula'] == matricula:
                aluno['nome'] = input('Digite o novo nome do aluno: ')
                aluno['idade'] = int(input('Digite a nova idade: '))
                aluno['nota'] = input('Digite a nova nota do aluno: ')
                print('Dados alterados com sucesso!')
        else: 
            print('Aluno não encontrado!')

    elif opcao == '5':
        matricula = int(input('digite a matricula do aluno: '))
        print('-' * 50)
        for aluno in repositorio:
            if aluno['matrícula'] == matricula:
                repositorio.remove(aluno)
                print('Aluno removido com sucesso!')
        else:
            print('Aluno não encontrado!')

        
       
    
    

