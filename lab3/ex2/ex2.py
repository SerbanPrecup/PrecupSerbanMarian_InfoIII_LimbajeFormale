
class ParkingLotDFA:
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.occupied_spots = 0

    def display_status(self):
        print(f"Locuri ocupate: {self.occupied_spots}/{self.total_spots}")

    def park_car(self):
        if self.occupied_spots < self.total_spots:
            self.occupied_spots += 1
            print("Masina a fost parcata cu succes.")
        else:
            print("Eroare: Parcare plina. Nu se poate parca.")

    def leave_car(self):
        if self.occupied_spots > 0:
            self.occupied_spots -= 1
            print("Masina a parasit parcarea cu succes.")
        else:
            print("Eroare: Parcare goala. Nicio masina nu poate pleca.")

    def run(self):
        print("Parcare automata!")
        while True:
            print("\nAlege o optiune:")
            print("(spatiu)  Verifica starea parcarii")
            print("+  Parcheaza o masina")
            print("-  Pleaca cu o masina")
            print("i  Iesire")

            choice = input("Optiunea: ").strip()

            if choice == '':
                self.display_status()
            elif choice == '+':
                self.park_car()
            elif choice == '-':
                self.leave_car()
            elif choice == 'i':
                print("La revedere!")
                break
            else:
                print("Optiune invalida.")


parking_lot = ParkingLotDFA(total_spots=5)
parking_lot.run()
