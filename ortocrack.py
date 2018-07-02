import logging
passwords = []


def add_password(password):
    extra_num = "1"
    if password not in passwords:
        for x in range(1, len(basename)):
            pw = password[:x] + " " + password[x:]
            passwords.append(pw)
            for x in range(1, len(basename)):
                passwords.append(pw[:x] + " " + pw[x:])
        passwords.append(password)
        passwords.append(password + "1")
    for x in range(5):
        extra_num = extra_num + str(int(extra_num) + 1)[-1:]
        if password + extra_num not in passwords:
            passwords.append(password + extra_num)


def uppercase(letter, i):
    pw = letter[:i] + letter[i].upper() + letter[i + 1:]
    add_password(pw)
    return pw


basename = str(input("Base Password> ")).lower()
logging.basicConfig(filename=basename + "-wordlist.txt", level=logging.DEBUG, format='%(message)s')
logging.log(10, basename)
for char in range(len(basename)):
    uppercased = uppercase(basename, char)
    for x in range(len(basename)):
        uppercased = uppercase(uppercased, x)
        for x in range(len(basename)):
            uppercase(uppercased, x)
    for x in range(len(uppercased)):
        pw = basename[:char].upper() + basename[char:]
        add_password(pw)
for x in passwords:
    logging.log(10, x)
print("Wordlist generated successfully!")
