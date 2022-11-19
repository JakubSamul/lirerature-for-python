myPets = ['Kuba', 'Kuba1', 'Kuba2', 'Kuba3']
print('Podaj imię kota:')
name = input()
if name not in myPets:
    print('Nie mam zwierzęcia o imieniu ' + name + '.')
else:
    print(name + ' to mój zwierzak.')

