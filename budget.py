
import datetime
import os
import logging
import pickle

os.system("cls")

logging.basicConfig(filename='logeris.log', encoding="UTF-8",
level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class Irasas():
    def __init__(self, suma, komentaras, dataa):
        self.suma = suma
        self.komentaras = komentaras
        self.dataa = dataa
    
        '''Konstruktorius, skirtas sukurti naują Irasas objektą.
        
        Argumentai:
        suma (int): suma
        komentaras (str): įvedamo įrašo komentaras
             
        Grąžinamos reikšmės:
        None
        '''

class Biudzetas():
    '''Klasė, skirta biudžeto žurnalui laikyti'''
    def __init__(self):
        '''
        Konstruktorius, skirtas sukurti naują Biudzetas objektą.
        
        Grąžinamos reikšmės:
        None
        '''
    def __init__(self, suma, komentaras, dataa, gavejas):
        super().__init__(suma, komentaras, dataa)
        self.gavejas = gavejas

class Pajamos(Irasas):
    def __init__(self, suma, komentaras, dataa, siuntejas):
        '''
        Konstruktorius, skirtas sukurti naują Pajamos objektą.
        
        Argumentai:
        suma (int): suma
        komentaras (str): įvedamų pajamų komentaras
        siuntejas (str): iš kur gautos pajamos
        
        Grąžinamos reikšmės:
        None
        '''
        super().__init__(suma, komentaras, dataa)
        self.siuntejas = siuntejas

class Islaidos(Irasas):
    def __init__(self, suma, komentaras, dataa, gavejas):
        '''
        Konstruktorius, skirtas sukurti naują Islaidos objektą.
        
        Argumentai:
        suma (int): suma
        komentaras (str): įvedamų išlaidų komentaras
        gavejas (str): kam skririamos išlaidos
        
        Grąžinamos reikšmės:
        None
        '''
        super().__init__(suma, komentaras, dataa)
        self.gavejas = gavejas

class Biudzetas():
    def __init__(self):
        if os.path.exists('biudzetas.pickle'):
            with open('biudzetas.pickle', 'rb') as file:
                zurnalas = pickle.load(file)
        self.zurnalas = zurnalas
        self.pajamos = []
        self.islaidos = []

    def ataskaita(self):
        '''
        Funkcija, kuri atspausdina biudžeto ataskaitos informaciją.
        
        Grąžinamos reikšmės:
        None
        '''
        print("Biudzeto ataskaita:")
        for irasas in self.zurnalas:
            print(f"Data: {irasas.dataa} {irasas.komentaras}: {irasas.suma}")
        print()

    def balansas(self):
        '''
        Funkcija, kuri atspausdina balanso informaciją.
        
        Grąžinamos reikšmės:
        None
        '''
        balansas = 0
        for irasas in self.zurnalas:
            if isinstance(irasas, Islaidos):
                balansas -= irasas.suma
            elif isinstance(irasas, Pajamos):
                balansas += irasas.suma
        print(f"Einamasis balansas: {balansas}")
        print()

    def naujas_pajamu_irasas(self, suma, komentaras, dataa, siuntejas):
        '''
        Funkcija, kuri atspausdina naują pajamų informaciją.
        
        Grąžinamos reikšmės:
        None
        '''
        pajamos = Pajamos(suma, komentaras, dataa, siuntejas)
        if suma < 0:
            logging.info('Minusines pajamos')
        self.zurnalas.append(pajamos)
        print("Pajamų įrašas sėkmingai pridėtas.")
        print()

    def naujas_islaidu_irasas(self, suma, komentaras, dataa, gavejas):
        '''
        Funkcija, kuri atspausdina naują pajamų įšlaidų informaciją.
        
        Grąžinamos reikšmės:
        None
        '''
        islaidos = Islaidos(suma, komentaras, dataa, gavejas)
        self.zurnalas.append(islaidos)
        print("Išlaidų įrašas sėkmingai pridėtas.")
        print()

biudzetas = Biudzetas()

while True:

    print("Pasirinkite veiksmą:")
    print("1. Pridėti naują pajamų įrašą")
    print("2. Pridėti naują išlaidų įrašą")
    print("3. Spausdinti biudžeto ataskaitą")
    print("4. Spausdinti einamąjį balansą")
    print("5. Išeiti iš programos")

    choice = input("Jūsų pasirinkimas: ")

    if choice == "1":
        clear()
        try:
            suma = float(input("Įveskite pajamų sumą: "))
        except ValueError:
            print('Turi būti skaičius')
            suma = float(input("Įveskite pajamų sumą: "))
        komentaras = input("Įveskite komentarą: ")
        siuntejas = input("Įveskite pajamų siuntėją: ")
        dataa = datetime.datetime.now().replace(microsecond=0)
        biudzetas.naujas_pajamu_irasas(suma, komentaras, dataa, siuntejas)
        input("Paspauskite ENTER, kad tęstumėte...")

    elif choice == "2":
        clear()
        try:
            suma = float(input("Įveskite išlaidų sumą: "))
        except ValueError:
            print('Turi būti skaičius')
            suma = float(input("Įveskite pajamų sumą: "))
        komentaras = input("Įveskite komentarą: ")
        gavejas = input("Įveskite išlaidų gavėją: ")
        dataa = datetime.datetime.now().replace(microsecond=0)
        biudzetas.naujas_islaidu_irasas(suma, komentaras, dataa, gavejas)
        input("Paspauskite ENTER, kad tęstumėte...")

    elif choice == "3":
        clear()
        biudzetas.ataskaita()
        input("Paspauskite ENTER, kad tęstumėte...")

    elif choice == "4":
        clear()
        biudzetas.balansas()
        input("Paspauskite ENTER, kad tęstumėte...")

    elif choice == "5":
        clear()
        print("Geros dienos!")
        with open('biudzetas.pickle', 'wb') as file:
            pickle.dump(biudzetas.zurnalas, file)
        break

    else:
        print("Neteisingas pasirinkimas, bandykite dar kartą.")
