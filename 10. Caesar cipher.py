def encrypt(msg, key):
    msg_list = []
    for char in msg:
        msg_list.append(ord(char))
    for i,ascii in enumerate(msg_list):
        if ascii >= 65 and ascii <= 90:
            a = ascii + key
            if a > 90:
                a = 64 + (a-90)
            msg_list[i] = a
        elif ascii >= 97 and ascii <= 122:
            a = ascii + key
            if a > 122:
                a = 96 + (a-122)
            msg_list[i] = a
        elif ascii >= 48 and ascii <= 57:
            a = ascii + key
            if a > 57:
                a = 47 + (a-57)
            msg_list[i] = a
    
    encrypt_str = ""
    for i in msg_list:
        encrypt_str += chr(i)
    print("Encrypted string: ", encrypt_str)

def decrypt(msg,key):
    msg_list = []
    for char in msg:
        msg_list.append(ord(char))
    for i,ascii in enumerate(msg_list):
        if ascii >= 65 and ascii <= 90:
            a = ascii - key
            if a < 65:
                a = 91-(65-a)
            msg_list[i] = a
        elif ascii >= 97 and ascii <= 122:
            a = ascii - key
            if a < 97:
                a = 123 - (97-a)
            msg_list[i] = a
        elif ascii >= 48 and ascii <= 57:
            a = ascii - key
            if a < 48:
                a = 58 - (48-a)
            msg_list[i] = a
    
    decrypt_str = ""
    for i in msg_list:
        decrypt_str += chr(i)
    print("Depcrypted string: ", decrypt_str)

print("-"*15,"Caesar Cipher","-"*15)
msg = input("Enter your message: ")
print("1. Encrypt")
print("2. Decrypt")
while True:
    try:
        choice = int(input("Enter your choice: "))
        key = input("Enter the key (integers): ")
        if not key.isdigit():
            print("Key not acceptable.")
            raise ValueError
        else:
            key = int(key)
        if 1<=choice<=2:
            break
        else:
            print("Choice out of range! Try again.")
            continue
    except Exception:
        print("Invalid entry! Try again.")

if choice == 1:
    encrypt(msg,key)
else:
    decrypt(msg,key)