def receive_notes():
    notas = []
    while len(notas) < 2:
        nota = verify_score()
        if nota:
            notas.append(nota)
    print('media = {:.2f}'.format((notas[0] + notas[1]) / 2))


def calc_media(n1, n2):
    print(f'media {(n1 + n2) / 2}')


def verify_score():
    nota = float(input())
    if nota < 0 or nota > 10:
        print('nota invalida')
        return False
    else:
        return nota

def menu():
    print('novo calculo (1-sim 2-nao)')
    n = int(input())
    if n == 1 or n == 2:
        return n
    else:
        return False


cont = 0


while cont != 2:
    receive_notes()
    cont = menu()
    while cont != 2 and cont != 1:
        cont = menu()






    



