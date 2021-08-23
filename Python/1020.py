x = int(input())

a = x / 365
m = (x % 365) / 30
d = (x % 365) % 30

print(f'{int(a)} ano(s)')
print(f'{int(m)} mes(es)')
print(f'{int(d)} dia(s)')
