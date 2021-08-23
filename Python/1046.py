hIni, hFim = map(int, input().split())


if hIni > hFim:
    print(f"O JOGO DUROU {24 - (hIni - hFim)} HORA(S)")
elif hFim > hIni:
    print(f"O JOGO DUROU {hFim - hIni} HORA(S)")
else:
    print("O JOGO DUROU 24 HORA(S)")



