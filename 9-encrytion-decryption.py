def encrypt():
    input_password = input("Enter your password to encrypt: ")
    while len(input_password) < 4 or len(input_password) > 150:
        input_password = input("Invalid Input. Enter a password between 4 and 150 characters: ")
    encrypted_password = "" 
    for index in input_password:
        if ord(index) > 32 and ord(index) <= 117:
            encryption = chr(ord(index) + 9)
            print(f"{index}: {encryption}")
        else:
            encryption = chr(ord(index))
            print(f"{index}: {encryption}")
        encrypted_password += encryption
        encrypted_password += "$*"
    print(f"The encrypted password is \" {encrypted_password} \".")


def decrypt():
    password_to_decrypt = input("Enter your password to decrypt: ")
    while len(password_to_decrypt) < 4 or len(password_to_decrypt) > 450:
        password_to_decrypt = input("Invalid Input. Enter an encrypted password between 4 and 150 characters: ")
    password_to_decrypt = password_to_decrypt.replace("$*", "")
    for index in password_to_decrypt:
        if ord(index) > 41 and ord(index) <= 126:
            decryption = chr(ord(index) - 9)
            print(f"{index}: {decryption}")
        else:
            decryption = chr(ord(index))
            print(f"{index}: {decryption}")
        password_to_decrypt += decryption
    x = int(len(password_to_decrypt)/2)
    print(f"The decrypted password is \" {password_to_decrypt[x:]} \".")

def main():
    encrypted_password = encrypt()
    decrypted_password = decrypt()

    if encrypted_password == decrypted_password:
        print("The encrypted password equals decrypted password.")
    else:
        print("An error occured.")


main()



