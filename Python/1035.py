inputs = input().split(' ')

a = int(inputs[0])
b = int(inputs[1])
c = int(inputs[2])
d = int(inputs[3])



if b > c and d > a and  (c + d) > (a + b) and c > 0 and d > 0 and (a % 2 == 0):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
