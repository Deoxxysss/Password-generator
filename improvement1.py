#generate 1 to 10 passwords at the same time
import random
import string
 
olas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
alas = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '{', '}', '[', ']', '|', ':', ';', '"', '<', '>', '?', '/']
klas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
dlas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
characters = string.ascii_letters + string.digits + string.punctuation
min1 = 0
while True:
    try:
        count = int(input("Enter the number of passwords you want: "))
        if count > 10:
            print("Max number of passwords you can generate at a single time is 10")
        elif count < 1:
            print("Min number of passwords you can generate at a single time is 1")
        else:
            break
    except ValueError:
        print("Please enter a valid integer for the number of passwords.")

while min1 < count:
    try:
        length = int(input("Enter password length: "))
        if length < 8:
            print("Password should be at least 8 characters.")
        elif length > 24:
            print("Password should not exceed 24 characters.")
        else:
            for _ in range(count):
                password = "".join(random.choice(characters) for _ in range(length-4))
                password = list(password)
                password.append(str(random.choice(olas)))
                password.append(random.choice(alas))
                password.append(random.choice(klas))
                password.append(random.choice(dlas))

                random.shuffle(password)
                print("".join(password))
                min1 += 1
    except ValueError:
        print("Please enter a valid integer for the password length.")