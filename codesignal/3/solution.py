def solution(numbers):
    result = [] # inicjalizacja pustej listy
    mid = len(numbers) // 2 # obliczenie elementu środkowego listy
    if len(numbers) % 2 == 1: # jeśli liczba elementów listy jest nieparzysta środkowy element musi być wpisany do resultatu
        left = mid - 1 # obliczenie pozycji elementu lewego
        right = mid + 1 # obliczenie pozycji elementu prawego
        result = [numbers[mid]] # dodanie elementu środkowego do listy ponieważ nie ma pary
    else: # w przypadku gdy ilość elementów jest parzysta
        left = mid - 1 # obliczenie pozycji elementu lewego
        right = mid # obliczenie pozycji elementu prawego
    while left >= 0 and right < len(numbers): # pętla do przelecenia listy
        result.append(numbers[left]*numbers[right]) # mnożenie elementów listy
        left -= 1 # iteracja elementów listy w celu przejścia do kolejnego elementu 
        right += 1
    return result