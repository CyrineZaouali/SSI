from Crypto.Cipher import AES, DES

from phase3.generic_cli import generic_cli


def pad(text: str, modulo: int):
    n = len(text) % modulo
    return text.encode() + (b" " * (modulo - n))

def encrypt_des_cli():
    key = input("Please Enter Key (8 bytes): ")
    message = input("Enter Message to be encrypted DES: ")
    return encrypt_des(key, message)

def encrypt_des(key, message):
    des = DES.new(key.encode(), DES.MODE_ECB)
    padded_text = pad(message, 8)
    encrypted_text: bytes = des.encrypt(padded_text)
    print(f"Encrypted Message:\n{encrypted_text.hex()}\n")

def decrypt_des_cli():
    key = input("Please Enter Key (8 bytes): ")
    message = input("Enter Message to be decrypted DES : ")
    des = DES.new(key.encode(), DES.MODE_ECB)
    decrypted_text: bytes = des.decrypt(bytes.fromhex(message))
    result = decrypted_text.decode("utf-8").strip()
    print(f"Decrypted Message:\n{result}\n")

def encrypt_aes256_cli():
    key = input("Please Enter Key (16, 24 or 32 bytes long) : ")
    message = input("Enter Message to be encrypted AES256 : ")
    return encrypt_aes256(key, message)

def encrypt_aes256(key, message):
    padded_text = pad(message, 16)
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    ciphertext: bytes = cipher.encrypt(padded_text)
    print(f"Encrypted Message:\n{ciphertext.hex()}\n")

def decrypt_aes256_cli():
    key = input("Please Enter Key (16, 24 or 32 bytes long) : ")
    message = input("Enter Message to be decrypted AES256: ")
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    ciphertext: bytes = cipher.decrypt(bytes.fromhex(message))
    result = ciphertext.decode("utf-8").strip()
    print(f"Decrypted Message:\n{result}\n")


menu = {
    "4-1": {"message": "Encrypt Message DES", "func": encrypt_des_cli},
    "4-2": {"message": "Decrypt Message DES", "func": decrypt_des_cli},
    "4-3": {"message": "Encrypt Message AES256", "func": encrypt_aes256_cli},
    "4-4": {"message": "Decrypt Message AES256", "func": decrypt_aes256_cli},
}


def encrypt_sym_cli():
    generic_cli(menu=menu)
