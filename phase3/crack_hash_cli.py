import hashlib

from phase3.generic_cli import generic_cli


def get_email_list_generator():
    with open("./phase3/insat.dic", "r") as f:
        return f.readlines()


def crack_md5_cli():
    message = input("Enter an email to be cracked MD5: ")

    for i in get_email_list_generator():
        if hashlib.md5(i.strip().encode()).hexdigest() == message:
            print(f"\ncracked Message:\n{i}\n")
            return
    print(f"\nCould Not find message in email wordlist\n")


def crack_sh1_cli():
    message = input("Enter Message to be cracked SH1: ")
    for i in get_email_list_generator():
        if hashlib.sha1(i.strip().encode()).hexdigest() == message:
            print(f"\ncracked Message:\n{i}\n")
            return

    print(f"\nCould Not find message in email wordlist\n")


def crack_sha256_cli():
    message = input("Enter Message to be cracked SH256: ")
    for i in get_email_list_generator():
        if hashlib.sha256(i.strip().encode()).hexdigest() == message:
            print(f"\ncracked Message:\n{i}\n")
            return

    print(f"\nCould Not find message in email wordlist\n")


menu = {
    "3-1": {"message": "Crack Md5", "func": crack_md5_cli},
    "3-2": {"message": "Crack SH1", "func": crack_sh1_cli},
    "3-3": {"message": "Crack SHA256", "func": crack_sha256_cli},
}


def crack_hash_cli():
    generic_cli(menu=menu)
