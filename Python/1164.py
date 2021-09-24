def priminho(number):

    divisores = []
    for i in range(1, number):
        if number % i == 0:
            divisores.append(i)
    counter = 0
    for i in divisores:
        counter += i
    if counter == number:
        print(f'{number} eh perfeito')
    else:
        print(f'{number} nao eh perfeito')

rolls = int(input())
for i in range(rolls):
    insider = int(input())
    priminho(insider)
