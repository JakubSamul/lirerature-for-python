def spam():
    global eggs
    eggs = 'spam' #To jest zmienna globalna

def baconn():
    eggs = 'bacon' #To jest zmienna loaklna 

def ham():
    print(eggs) #To jest zmienna globalna

eggs = 42
spam()
print(eggs)