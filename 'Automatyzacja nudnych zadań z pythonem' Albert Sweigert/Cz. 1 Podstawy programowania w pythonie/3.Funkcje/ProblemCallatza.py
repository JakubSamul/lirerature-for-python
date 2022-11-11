def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        return number
    elif number % 2 == 1:
        number = 3 * number +1
        print(number)
        return number
    

print('Podaj liczbę:')
i = input()
while i != 1:
    try:
        i = collatz(int(i))
    except ValueError:
        print('Musisz podać liczbę całkowitą.')
        break


