def caesar(text,shift,encrypt):
    if not isinstance(shift, int):
        return "Enter a positive Integer value."
    if shift < 1 and shift > 25 :
        return "Enter  an integer between 1 and 25"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if not encrypt:
        shift = -shift
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper()  , shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text
def encrypt(text, shift):
    return caesar(text, shift, True)
def decrypt(text, shift):
    return caesar(text, shift, False)

encrypted_text = encrypt('Hello World!', 12)
print(encrypted_text)