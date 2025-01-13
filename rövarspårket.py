def is_consonant(char):
    return char.lower() in "bcdfghjklmnpqrstvwxyzåäö"


def translate_to_rovarspraket(text):
    rovarspraket = ""
    for char in text:
        if char.isalpha() and is_consonant(char):
            rovarspraket += char + "o" + char.lower()
        else:
            rovarspraket += char
    return rovarspraket


input_text = input("Skriv in en mening på svenska: ")
translated_text = translate_to_rovarspraket(input_text)
print("Rövarspråket: ", translated_text)
