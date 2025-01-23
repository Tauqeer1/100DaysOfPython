alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
            'x', 'y', 'z']

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    def caesar(text, shift, direction):
        caesar_text = ''
        if direction == 'decode':
            shift = -shift
        for ch in text:
            if ch in alphabet:    
                index = alphabet.index(ch)
                shifted_index = index + shift
                if direction == 'encode' and shifted_index > len(alphabet):
                    shifted_index = 0 + shift - 1 
                caesar_text += alphabet[shifted_index]
            else:
                caesar_text += ch
        print(f"The {direction}d text is {caesar_text}")

    if shift > len(alphabet):
        shift = shift % len(alphabet)

    caesar(text=text, shift=shift, direction=direction)
    
    user_input = input("Do you want to continue? (yes/no): ").lower()
    
    if user_input == "no":
        break












# def encrypt(plain_text, shift_amount):
#     encrypted_text = ''
#     for ch in plain_text:
#         index = alphabet.index(ch)
#         shifted_index = index + shift_amount
#         if shifted_index > len(alphabet):
#             shifted_index = 0 + shift_amount - 1
#         encrypted_text += alphabet[shifted_index]
#     print(f"The encoded text is {encrypted_text}")

# def decrypt(encrypted_text, shift_amount):
#     plain_text = ''
#     for ch in encrypted_text:
#         index = alphabet.index(ch)
#         shifted_index =  index - shift_amount
#         plain_text += alphabet[shifted_index]
#     print(f"The decoded text is {plain_text}")

# if direction == 'encode':
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == 'decode':
#     decrypt(encrypted_text=text, shift_amount=shift)