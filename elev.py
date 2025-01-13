class elev:
    def __init__(self, ålder, namn):
        self.namn = namn
        self.ålder = ålder


elev1 = elev(15, "Anna")
print(f"namn: {elev1.namn}, Ålder: {elev1.ålder}")


class Elev:
    def __init__(self, namn, ålder, godkänd):
        self.namn = namn
        self.ålder = ålder
        self.glad = godkänd


elev1 = Elev("Anna", 15, True)
print(f"Namn: {elev1.namn}, Ålder: {elev1.ålder}, Glad: {elev1.glad}")

elev2 = Elev("Oskar", 16, False)
print(f"Namn: {elev2.namn}, Ålder: {elev2.ålder}, Glad: {elev2.glad}")


# ---------------------------
# |           Elev           |
# ---------------------------
# | - namn: str              |
# | - ålder: int             |
# | - glad: bool             |
# ---------------------------
# | + __init__(namn, ålder,  |
# |            godkänd):     |
# ---------------------------
