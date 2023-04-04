import hashlib

while True:
    string = input("Digite uma palavra para gerar o hash: ")
    hash_obj = hashlib.sha1(string.encode())
    hash_str = hash_obj.hexdigest()
    print("O hash :", hash_str)
