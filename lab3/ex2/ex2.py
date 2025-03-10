import random

class ParkingLotNFA:
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.occupied_spots = 0

    def display_status(self):
        print(f"Locuri ocupate: {self.occupied_spots}/{self.total_spots}")

    def park_car(self):
        if self.occupied_spots < self.total_spots:
            # Nedeterminism: fie parchează, fie rămâne în aceeași stare
            if random.choice([True, False]):
                self.occupied_spots += 1
                print("Masina a fost parcata cu succes.")
            else:
                print("Nedeterminism: Masina NU a fost parcata (ramane in aceeasi stare).")
        else:
            print("Eroare: Parcare plina. Nu se poate parca.")

    def leave_car(self):
        if self.occupied_spots > 0:
            # Nedeterminism: fie pleacă, fie rămâne în aceeași stare
            if random.choice([True, False]):
                self.occupied_spots -= 1
                print("Masina a parasit parcarea cu succes.")
            else:
                print("Nedeterminism: Masina NU a plecat (ramane in aceeasi stare).")
        else:
            print("Eroare: Parcare goala. Nicio masina nu poate pleca.")

    def epsilon_transition(self):
        print("Tranzitie epsilon: Verificare automată a stării parcării.")
        self.display_status()

    def run(self):
        print("Parcare automata (NFA - Nedeterminist)!")
        while True:
            print("\nAlege o optiune:")
            print("(epsilon)  Verifica starea parcarii (fără input)")
            print("+  Parcheaza o masina")
            print("-  Pleaca cu o masina")
            print("i  Iesire")

            choice = input("Optiunea: ").strip()

            if choice == '':
                self.epsilon_transition()  # Tranziție epsilon
            elif choice == '+':
                self.park_car()
            elif choice == '-':
                self.leave_car()
            elif choice == 'i':
                print("La revedere!")
                break
            else:
                print("Optiune invalida.")


parking_lot = ParkingLotNFA(total_spots=5)
parking_lot.run()