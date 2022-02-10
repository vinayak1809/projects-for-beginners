from string import ascii_letters

encrypt_decrypt = str(
    input("Press 'E' to Encrypt the message / 'D' to Decrypt the message :: ")).upper()

if encrypt_decrypt == "E":
    letter_you_to_encrpyt = str(input("Encrypt the message : "))
    for letter in letter_you_to_encrpyt:

        if letter in ascii_letters:
            letter = ascii_letters.index(letter)+3
            print(ascii_letters[letter], end="")

    print()
    exit()

elif encrypt_decrypt == "D":
    decrypt_letter = str(input("Decrypt the message : "))
    for letter in decrypt_letter:

        if letter in ascii_letters:
            letter = ascii_letters.index(letter)-3
            print(ascii_letters[letter], end="")

    print()
