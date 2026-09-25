while True:
    nome = input('Qual o seu nome? ')
    aluguel = float(input('Qual o valor do aluguel? '))
    print(f'Oi {nome}, você quer pagar R$ {aluguel} de aluguel.')

    salario = float(input('Qual o seu salário? '))
    if  aluguel <= salario * 0.3:
        print('O aluguel está dentro do seu orçamento.')
    else:
        print('O aluguel está fora do seu orçamento.')

    pergunta = input("Deseja continuar (s/n)? ").lower()
    
    if pergunta in ['n', 'não', 'nao', 'não quero', 'nao quero', 'nao', 'não']:
        print('Obrigado por usar o programa!')
        break
    else:
        print('Vamos continuar...')