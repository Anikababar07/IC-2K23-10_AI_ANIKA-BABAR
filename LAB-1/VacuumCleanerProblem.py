# Vacuum Cleaner Problem using a Simple Reflex Agent

def vacuum_cleaner(location, status_a, status_b):

    print("Initial State:")
    print("Location:", location)
    print("Room A:", status_a)
    print("Room B:", status_b)
    print("\nActions taken:")

    # Clean Room A if dirty
    if location == "A":
        if status_a == "Dirty":
            print("Room A is Dirty -> Cleaning Room A")
            status_a = "Clean"

        print("Moving from A to B")
        location = "B"

    # Clean Room B if dirty
    if location == "B":
        if status_b == "Dirty":
            print("Room B is Dirty -> Cleaning Room B")
            status_b = "Clean"

    print("\nFinal State:")
    print("Room A:", status_a)
    print("Room B:", status_b)


# Initial environment
vacuum_cleaner("A", "Dirty", "Dirty")