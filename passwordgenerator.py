import random
import string
 
olas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
alas = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '{', '}', '[', ']', '|', ':', ';', '"', '<', '>', '?', '/']
klas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
dlas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
characters = string.ascii_letters + string.digits + string.punctuation
while True:
    try:
        length = int(input("Enter password length: "))
        if length < 8:
            print("Password should be at least 8 characters.")
        elif length > 24:
            print("Password should not exceed 24 characters.")
        else:
            password = "".join(random.choice(characters) for _ in range(length-4))
            password = list(password)
            password.append(str(random.choice(olas)))
            password.append(random.choice(alas))
            password.append(random.choice(klas))
            password.append(random.choice(dlas))

            random.shuffle(password)
            password = "".join(password)
            print(password)
            break
    except ValueError:
        print("Please enter a valid integer for the password length.")

