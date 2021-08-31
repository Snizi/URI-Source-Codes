entry = int(input())

for i in range(entry):
    t = int(input())
    cont = 0
    for j in range(1, t+1):
        if t % j == 0:
            cont += 1
    if cont <= 2:
        print(f'{t} eh primo')
    else:
        print(f'{t} nao eh primo')


