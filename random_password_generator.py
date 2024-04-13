#Random Password Generator 

import random
import string


def rands():
    randomuletter = random.choice(uletters)
    randomlletter = random.choice(lletters)
    randomdigit = random.choice(digits)
    randompunct = random.choice(punct)
    
    randlist = [randomuletter, randomlletter, randomdigit, randompunct]
    ultrandom = random.choice(randlist)
    password.append(ultrandom)

pass_len = int(input("Enter Password Length(min. 8): ")) 
len = pass_len - 4 
uletters = string.ascii_uppercase
lletters = string.ascii_lowercase 
digits = string.digits
punct = string.punctuation

password = []

randomuletter = random.choice(uletters)
randomlletter = random.choice(lletters)
randomdigit = random.choice(digits)
randompunct = random.choice(punct)
password.append(randomuletter)
password.append(randomlletter)
password.append(randomdigit)
password.append(randompunct)

for i in (range(len)):
    rands()

random.shuffle(password)

print("".join(password))

