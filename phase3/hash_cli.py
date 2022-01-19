import hashlib

from phase3.generic_cli import generic_cli


def hash_md5_cli():
    message = input("Enter Message to be hashed MD5: ")
    hashed = hashlib.md5(message.encode())
    print(f"\nHashed Message:\n{hashed.hexdigest()}\n")


def hash_sh1_cli():
    message = input("Enter Message to be hashed SH1: ")
    hashed = hashlib.sha1(message.encode())
    print(f"\nHashed Message:\n{hashed.hexdigest()}\n")


def hash_sha256_cli():
    message = input("Enter Message to be hashed SH256")
    hashed = hashlib.sha256(message.encode())
    print(f"\nHashed Message:\n{hashed.hexdigest()}\n")


menu = {
    "2-1": {"message": "Hash Md5", "func": hash_md5_cli},
    "2-2": {"message": "Hash SH1", "func": hash_sh1_cli},
    "2-3": {"message": "Hash SHA256", "func": hash_sha256_cli},
}


def hash_cli():
    generic_cli(menu=menu)
