casa = float(input('Digite o valor da casa R$: '))
salario = float(input('Digite o valor do seu salário mensal: '))
ano = int(input('Digite a quantidade de anos: '))
prestacao = casa / (ano *12)
if prestacao >= (30/100) * salario:
    print('Empréstimo negado')
else:
    print('Empréstimo concedido')