# def spam(divideBy):
#     return 42 / divideBy
def spam(divineBY):
    try:
        return 42 / divineBY
    except ZeroDivisionError:
        print('Błąd: nieprawidłowy argument.')


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))