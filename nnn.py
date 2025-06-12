import math
def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnożenie(a, b):
    return a * b

def dzielenie(a, b):
    if b == 0:
        return "Nie można dzielić przez zero!"
    return a / b

def potegowanie(a, b):
    return a ** b
    
def pierwiastki(a):
    return math.sqrt(a)

def pitagoras(a,b):
    return math.sqrt(a**2 + b**2)

def Tcosinusów1(a,b,c):
    return math.sqrt(a**2 + b**2-2*a*b*math.cos(math.radians(c)))

def Tcosinusów2(a,b,c):
    return (a**2 + b**2 -c**2)/(2*a*b)

def kalkulator():
    while True:  # Pętla nieskończona – trwa, dopóki nie wpiszemy "nie"
        print("\nWybierz działanie:")
        print("1 - Dodawanie")
        print("2 - Odejmowanie")
        print("3 - Mnożenie")
        print("4 - Dzielenie")
        print("5 - Potęgowanie")
        print("6 - Pierwiastkowanie")
        print("7 - Pitagoras")
        print("8 - Twierdzenie cosinusów")
        print("0 - Zakończ program")

        wybor = input("Podaj numer działania (0-8): ")

        if wybor == '0':
            print("Do zobaczenia!")
            break  # Przerywa pętlę i kończy program

        if wybor not in ['1', '2', '3', '4', '5','6','7','8']:
            print("Nieprawidłowy wybór!")
            print("Spróbuj ponownie!")
            continue  # Wraca na początek pętli

        try:
            a = float(input("Podaj pierwszą liczbę: "))
            b = float(input("Podaj drugą liczbę: "))
        except ValueError:
            print("Błąd: wpisz poprawne liczby!")
            continue

        if wybor == '1':
            wynik = dodawanie(a, b)
            print(f"{a} + {b} = {wynik}")
        elif wybor == '2':
            wynik = odejmowanie(a, b)
            print(f"{a} - {b} = {wynik}")
        elif wybor == '3':
            wynik = mnożenie(a, b)
            print(f"{a} * {b} = {wynik}")
        elif wybor == '4':
            wynik = dzielenie(a, b)
            if isinstance(wynik, str):  # Błąd dzielenia przez 0
                print(wynik)
            else:
                print(f"{a} / {b} = {wynik}")
        elif wybor == '5':
            wynik = potegowanie(a, b)
            print(f"{a} ^ {b} = {wynik}")
        elif wybor == '6':
        	wynik = pierwiastki(a)
        	print(f"/{a} = {wynik}")
        elif wybor == '7':
            wynik = pitagoras(a, b)
            print(f"{a}^2 + {b}^2 = {wynik}^2")
        elif wybor == '8':
            print("\nWybierz co obliczasz:")
            print("1 - bok na przeciw kąta")
            print("2 - cosinus")
            wybor2 = input("Podaj numer działania: ")
            if wybor2 == '1':
                    c=float(input("Podaj kąt cosinusa: "))
                    wynik=Tcosinusów1(a,b,c)
                    print(f"{a}^2 + {b}^2 - 2 * {a} * {b} * cos({c}) = {wynik}^2")
            elif wybor2 == '2':
                    c=float(input("Podaj trzecią liczbę: "))
                    wynik=Tcosinusów2(a,b,c)
                    wynik2=math.degrees(math.acos(wynik))
                    print(f"({a}^2 + {b}^2 - {c}^2)/(2 * {a} * {b}) = {wynik2}")
         elif

kalkulator()
