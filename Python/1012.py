buffer = input()

A, B, C = buffer.split(' ')

print('TRIANGULO: {:.3f}'.format((float(A)*float(C)) / 2))
print('CIRCULO: {:.3f}'.format((float(C)**2)* 3.14159))
print('TRAPEZIO: {:.3f}'.format(((float(A)+float(B))*float(C)) / 2))
print('QUADRADO: {:.3f}'.format(float(B)**2))
print('RETANGULO: {:.3f}'.format(float(A) * float(B)))
