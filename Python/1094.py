entries = int(input())

coelhos = 0
ratos = 0
sapos = 0

for i in range(entries):
    var = input().split()
    
    if var[1] == 'C':
        coelhos += int(var[0])
    elif var[1] == 'R':
        ratos += int(var[0])
    elif var[1] == 'S':
        sapos += int(var[0])

total = coelhos+ratos+sapos
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print('Percentual de coelhos: {:.2f} %'.format((coelhos / total) * 100))
print('Percentual de ratos: {:.2f} %'.format((ratos / total) * 100))
print('Percentual de sapos: {:.2f} %'.format((sapos / total) * 100))
