uczniowie = {}
nauczyciele = {}
wychowawcy = {}

def utworz_ucznia():
    imie_nazwisko = input("Podaj imię i nazwisko ucznia: ")
    klasa = input("Podaj nazwę klasy ucznia: ")
    uczniowie[imie_nazwisko] = klasa

def utworz_nauczyciela():
    imie_nazwisko = input("Podaj imię i nazwisko nauczyciela: ")
    przedmiot = input("Podaj nazwę przedmiotu: ")
    klasy = []
    while True:
        klasa = input("Podaj nazwę klasy, którą prowadzi nauczyciel (wpisz 'koniec' aby zakończyć): ")
        if klasa.lower() == 'koniec':
            break
        klasy.append(klasa)
    nauczyciele[imie_nazwisko] = {"przedmiot": przedmiot, "klasy": klasy}

def utworz_wychowawce():
    imie_nazwisko = input("Podaj imię i nazwisko wychowawcy: ")
    klasa = input("Podaj nazwę prowadzonej klasy przez wychowawcę: ")
    wychowawcy[imie_nazwisko] = klasa

def zarzadzaj_klasa():
    klasa = input("Podaj nazwę klasy do wyświetlenia: ")
    print(f"Uczniowie należący do klasy {klasa}:")
    for uczen, klasa_ucznia in uczniowie.items():
        if klasa_ucznia == klasa:
            print(uczen)
    wychowawca = None
    for wych, klasa_wych in wychowawcy.items():
        if klasa_wych == klasa:
            wychowawca = wych
            break
    if wychowawca:
        print(f"Wychowawca klasy {klasa}: {wychowawca}")
    else:
        print(f"Klasa {klasa} nie ma jeszcze wychowawcy.")

def zarzadzaj_uczen():
    uczen = input("Podaj imię i nazwisko ucznia do wyświetlenia lekcji i nauczycieli: ")
    if uczen in uczniowie:
        print(f"Lekcje ucznia {uczen}:")
        for nauczyciel, dane_nauczyciela in nauczyciele.items():
            if uczniowie[uczen] in dane_nauczyciela['klasy']:
                print(f"- {dane_nauczyciela['przedmiot']} prowadzony przez {nauczyciel}")
    else:
        print(f"{uczen} nie jest uczniem w naszej bazie danych.")

def zarzadzaj_nauczyciel():
    nauczyciel = input("Podaj imię i nazwisko nauczyciela do wyświetlenia klas: ")
    if nauczyciel in nauczyciele:
        print(f"Klasy prowadzone przez {nauczyciel}:")
        for klasa in nauczyciele[nauczyciel]['klasy']:
            print(f"- {klasa}")
    else:
        print(f"{nauczyciel} nie jest nauczycielem w naszej bazie danych.")

def zarzadzaj_wychowawca():
    wychowawca = input("Podaj imię i nazwisko wychowawcy do wyświetlenia uczniów: ")
    if wychowawca in wychowawcy:
        print(f"Uczniowie prowadzeni przez {wychowawca}:")
        for uczen, klasa_ucznia in uczniowie.items():
            if klasa_ucznia == wychowawcy[wychowawca]:
                print(uczen)
    else:
        print(f"{wychowawca} nie jest wychowawcą w naszej bazie danych.")

def main():
    while True:
        print("\nMenu:")
        print("1. Utwórz")
        print("2. Zarządzaj")
        print("3. Koniec")

        wybor_menu = input("Wybierz opcję (1/2/3): ")

        if wybor_menu == "1":
            print("\nMenu Utwórz:")
            print("1. Uczeń")
            print("2. Nauczyciel")
            print("3. Wychowawca")
            print("4. Koniec")

            wybor_utworz = input("Wybierz opcję (1/2/3/4): ")

            if wybor_utworz == "1":
                utworz_ucznia()
            elif wybor_utworz == "2":
                utworz_nauczyciela()
            elif wybor_utworz == "3":
                utworz_wychowawce()
            elif wybor_utworz == "4":
                continue
            else:
                print("Nieprawidłowy wybór, spróbuj ponownie.")
        elif wybor_menu == "2":
            print("\nMenu Zarządzaj:")
            print("1. Klasa")
            print("2. Uczeń")
            print("3. Nauczyciel")
            print("4. Wychowawca")
            print("5. Koniec")

            wybor_zarzadzaj = input("Wybierz opcję (1/2/3/4/5): ")

            if wybor_zarzadzaj == "1":
                zarzadzaj_klasa()
            elif wybor_zarzadzaj == "2":
                zarzadzaj_uczen()
            elif wybor_zarzadzaj == "3":
                zarzadzaj_nauczyciel()
            elif wybor_zarzadzaj == "4":
                zarzadzaj_wychowawca()
            elif wybor_zarzadzaj == "5":
                continue
            else:
                print("Nieprawidłowy wybór, spróbuj ponownie.")
        elif wybor_menu == "3":
            print("Dziękujemy za korzystanie z programu. Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

if __name__ == "__main__":
    main()