# def is_consonant(char):
# return char.lower() in "bcdfghjklmnpqrstvwxyz"


# def translate_to_rovarspraket(text):
#     rovarspraket = ""
#     for char in text:
#         if is_consonant(char):
#             rovarspraket += char + "o" + char.lower()
#         else:
#             rovarspraket += char
#     return rovarspraket


# input_text = input("Skriv in en mening på svenska: ")
# translated_text = translate_to_rovarspraket(input_text)
# print("Rövarspråket: ", translated_text)


# text = input("Skriv in en text: ")

# baklanges_text = text[::-1]

# print("Texten baklänges: ", baklanges_text)

# lander_huvdstäder = {
#     "sverige": "stockholm",
#     "norge": "oslo",
#     "Finland": "hälsingfors",
#     "island": "reykjavik",
# }

# lander_huvdstäder.update({"Danmark": "köpenhamn"})
# lander_huvdstäder.pop("Finland")

# set1 = {"Banana", "Pear", "Apple"}
# set2 = {"Kiwi", "Pineapple", "Pear"}

# result_set = set1.union(set2)


# print("The resulting set:", result_set)

# print("Number of elements in the resulting set:", len(result_set))

class Person:
    __weight = 0                    # privat attribut

    def setWeight(self, weight):    # publik setter-metod
        if type(weight) == int and weight > 0:
            self.__weight = weight
        else:
            print("Du måste ange ett positivt heltal!")

    def getWeight(self):		# publik getter-metod
        return self.__weight


p = Person()
p.setWeight(-2)     			# Du måste ange ett positivt heltal
p.setWeight(70)
print(p.getWeight())


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
