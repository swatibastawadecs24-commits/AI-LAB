class SimpleReflexVacuum:

    def __init__(self):
        self.A = input("Enter state of Room A (Clean/Dirty): ")
        self.B = input("Enter state of Room B (Clean/Dirty): ")
        self.position = input("Enter vacuum starting position (A/B): ").upper()[0]

    def run(self):
        for i in range(4):

            print(f"\nVacuum is at Room {self.position}")

            if self.position == 'A':

                if self.A.lower() == "dirty":
                    print("Action: SUCK")
                    self.A = "Clean"
                else:
                    print("Action: MOVE RIGHT")
                    self.position = 'B'

            else:

                if self.B.lower() == "dirty":
                    print("Action: SUCK")
                    self.B = "Clean"
                else:
                    print("Action: MOVE LEFT")
                    self.position = 'A'

        print("\nFinal State:")
        print("Room A:", self.A)
        print("Room B:", self.B)


# Create and run the vacuum cleaner
vacuum = SimpleReflexVacuum()
vacuum.run()
