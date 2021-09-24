while True:
    try:
        a, b, c = list(map(int, input().split()))
        A = a*b
        t = A * 100 / c
        t = (t) ** (1/2)
        print(int(t))
    except ValueError:
        break

