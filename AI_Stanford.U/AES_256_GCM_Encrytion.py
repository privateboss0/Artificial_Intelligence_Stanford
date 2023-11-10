import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

ITERATION_COUNT = 65536
HASH_NAME = "blake2b" #BLAKE2 is a cryptographic hash function faster than MD5, 
#SHA-1, SHA-2, and SHA-3, yet it is belived to be as secure as the latest standard SHA-3.
IV_LENGTH = 12           #96bits
KEY_LENGTH = 32          #256bits
SALT_LENGTH = 16         #128bits
TAG_LENGTH = 16          #128bits

def encrypt(password, plain_message):
    salt = get_random_bytes(SALT_LENGTH) 
    iv = get_random_bytes(IV_LENGTH)

    secret = get_secret_key(password, salt)

    cipher = AES.new(secret, AES.MODE_GCM, iv)

    encrypted_message_byte, tag = cipher.encrypt_and_digest(
        plain_message.encode("utf-8")
    )
    cipher_byte = salt + iv + encrypted_message_byte + tag

    encoded_cipher_byte = base64.b64encode(cipher_byte)
    return bytes.decode(encoded_cipher_byte)

def decrypt(password, cipher_message):
    decoded_cipher_byte = base64.b64decode(cipher_message)

    salt = decoded_cipher_byte[:SALT_LENGTH]
    iv = decoded_cipher_byte[SALT_LENGTH : (SALT_LENGTH + IV_LENGTH)]
    encrypted_message_byte = decoded_cipher_byte[
        (IV_LENGTH + SALT_LENGTH) : -TAG_LENGTH
    ]
    tag = decoded_cipher_byte[-TAG_LENGTH:]
    secret = get_secret_key(password, salt)
    cipher = AES.new(secret, AES.MODE_GCM, iv)

    decrypted_message_byte = cipher.decrypt_and_verify(encrypted_message_byte, tag)
    return decrypted_message_byte.decode("utf-8")

def get_secret_key(password, salt):
    return hashlib.pbkdf2_hmac(
        HASH_NAME, password.encode(), salt, ITERATION_COUNT, KEY_LENGTH
    )

secret_key = "PrivatePublic1679@#"
plain_text = (input('Type in your message: '))

print("------ AES256-GCM Encryption ------")
cipher_text = encrypt(secret_key, plain_text)
print("encryption input ",  ":", plain_text)
print("encryption output ", ":", cipher_text)

decrypted_text = decrypt(secret_key, cipher_text)

print("\n------ AES256-GCM Decryption ------")
print("decryption input ",  ":", cipher_text)
print("decryption output ", ":", decrypted_text)