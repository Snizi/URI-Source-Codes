salario = float(input())

if salario > 0 and salario <= 400:
    reajuste = (salario * 15) / 100
    print('Novo salario: {:.2f}'.format(salario + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print(f'Em percentual: {15} %')
elif salario >= 400.01 and salario <= 800.00:
    reajuste = (salario * 12) / 100
    print('Novo salario: {:.2f}'.format(salario + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print(f'Em percentual: {12} %')
elif salario >= 800.01 and salario <= 1200.00:
    reajuste = (salario * 10) / 100
    print('Novo salario: {:.2f}'.format(salario + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print(f'Em percentual: {10} %')
elif salario >= 1200.01 and salario <= 2000.00:
    reajuste = (salario * 7) / 100
    print('Novo salario: {:.2f}'.format(salario + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print(f'Em percentual: {7} %')
elif salario > 2000:
    reajuste = (salario * 4) / 100
    print('Novo salario: {:.2f}'.format(salario + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print(f'Em percentual: {4} %')

