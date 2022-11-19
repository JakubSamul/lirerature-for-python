import random

message = [ 'To pewne', 
            'Zdecydowanie Tak', 
            'Tak' 'Niejasna odpowiedź, spróbuj ponownie', 
            'Zapytaj ponownie później', 
            'Skoncentruj się i spytaj ponownie', 
            'Moja odpowiedź brzmi nie', 
            'To nie wygląda zbyt dobrze', 
            'Bardzo wątpliwe']
    


print(message[random.randint(0, len(message)-1)])