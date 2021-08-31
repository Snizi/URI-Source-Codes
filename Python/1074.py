entry = int(input())

for i in range(entry):
    user_input = int(input())
    if user_input == 0:
        print('NULL')
    if user_input < 0 and user_input % 2 != 0:
        print('ODD NEGATIVE')
    if user_input < 0 and user_input % 2 == 0:
        print('EVEN NEGATIVE')
    if user_input > 0 and user_input % 2 != 0:
        print('ODD POSITIVE')
    if user_input > 0 and user_input % 2 == 0:
        print('EVEN POSITIVE')
