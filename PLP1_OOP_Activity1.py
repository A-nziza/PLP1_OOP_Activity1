class Passenger:
    def __init__(self, name, location, destination, date):
        self.name = name
        self.location = location
        self.destination = destination
        self.date = date

    def get_weight_allowance(self):
        return 20

    def get_passenger_info(self):
        return (f"Name: {self.name}\n"
                f"From: {self.location}\n"
                f"To: {self.destination}\n"
                f"Date: {self.date}\n"
                f"Luggage Allowance: {self.get_weight_allowance()} kg")


class Economy(Passenger):
    def __init__(self, name, location, destination, date, seat_preference):
        super().__init__(name, location, destination, date)
        self.seat_preference = seat_preference

    def get_passenger_info(self):
        return (f"Class: Economy\n{super().get_passenger_info()}\n"
                f"Seat Preference: {self.seat_preference}")


class Business(Passenger):
    def __init__(self, name, location, destination, date, lounge_pass_code):
        super().__init__(name, location, destination, date)
        self.lounge_pass_code = lounge_pass_code

    def get_weight_allowance(self):
        return 100

    def get_passenger_info(self):
        return (f"Class: Business\n{super().get_passenger_info()}\n"
                f"Lounge Pass Code: {self.lounge_pass_code}")


class FirstClass(Passenger):
    def __init__(self, name, location, destination, date, suite_number, chauffeur_service):
        super().__init__(name, location, destination, date)
        self.suite_number = suite_number
        self.chauffeur_service = chauffeur_service

    def get_weight_allowance(self):
        return 100

    def get_passenger_info(self):
        return (f"Class: First Class\n{super().get_passenger_info()}\n"
                f"Suite Number: {self.suite_number}\n"
                f"Chauffeur Service: {'Yes' if self.chauffeur_service else 'No'}")


def ask_text(prompt):
    """Keep asking until the user enters a non-empty string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def ask_yes_no(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ("y", "yes", "true"):
            return True
        if value in ("n", "no", "false"):
            return False
        print("Please enter Y or N.")


def choose_class():
    print("Select class:\n[1] Economy\n[2] Business\n[3] First Class")
    while True:
        choice = input("Enter choice (1-3): ").strip()
        if choice in ("1", "2", "3"):
            return choice
        print("Invalid choice. Please enter 1, 2 or 3.")


def main():
    print("=== Airline Ticket Booking System ===")
    choice = choose_class()

    name = ask_text("Passenger name: ")
    location = ask_text("Current location: ")
    destination = ask_text("Destination: ")
    date = ask_text("Travel date (YYYY-MM-DD): ")

    if choice == "1":
        passenger = Economy(name, location, destination, date,
                            ask_text("Seat preference (window/aisle/middle): "))
    elif choice == "2":
        passenger = Business(name, location, destination, date,
                             ask_text("Lounge pass code: "))
    else:
        passenger = FirstClass(name, location, destination, date,
                               ask_text("Suite number: "),
                               ask_yes_no("Chauffeur service? (Y/N): "))

    print("\n=== TICKET SUMMARY ===")
    print(passenger.get_passenger_info())


if __name__ == "__main__":
    main()
