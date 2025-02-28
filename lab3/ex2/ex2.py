
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
            print("1. Verifica starea parcarii")
            print("2. Parcheaza o masina")
            print("3. Pleaca cu o masina")
            print("4. Iesire")

            choice = input("Optiunea: ").strip()

            if choice == '1':
                self.display_status()
            elif choice == '2':
                self.park_car()
            elif choice == '3':
                self.leave_car()
            elif choice == '4':
                print("La revedere!")
                break
            else:
                print("Optiune invalida.")


parking_lot = ParkingLotDFA(total_spots=5)
parking_lot.run()
