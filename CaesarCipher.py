alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
  'v', 'w', 'x', 'y', 'z']

direction = ''
while direction != "encode" and direction != "decode":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()


text = input("Type your message:\n").lower()

shift = int(input("Type the shift number:\n"))
if direction == "encode":
    def encrypt(plain_text, shift_amount):
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)#1
            new_position = position + shift_amount#2
            new_letter = alphabet[new_position]#3
            cipher_text += new_letter#4
        print(f"The encoded text is {cipher_text}")
    encrypt(plain_text=text, shift_amount=shift)

elif direction == "decode":
    def decrypt(encrypted_text, shift_amount):
        text = ""
        for letter in encrypted_text:
            position = alphabet.index(letter)#1
            new_position = position - shift_amount#2
            new_letter = alphabet[new_position]#3
            text += new_letter#4
        print(f"The decoded text is {text}")
    decrypt(encrypted_text=text, shift_amount=shift)

