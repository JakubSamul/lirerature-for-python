def spam():
    eggs = 'Zmienna lokalna funkcji spam().'
    print(eggs)  #Wyświetla zmienna lokalną funkcji spam 

def bacon():
    eggs = 'Zmienna lokalna funkcji bacon().'
    print(eggs)     #Wyświetla zmienną lokalną funkji bacon().
    spam()
    print(eggs)     #Wyświetla zmienną lokalną funkcji bacon()

eggs = 'Zmienna globalna.'
bacon()
print(eggs)     #Wyświetla zmienną globalną