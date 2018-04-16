import random
import string

#Password Gen
#Logic- Ask user how many charecter Choose random words/charecters 

#How Strong Question
size = int(input("Hello! How strong would you like your password?"))
count = 0
pwd = ""
while count != size:
    upper = [random.choice(string.ascii_uppercase)]
    lower = [random.choice(string.ascii_lowercase)]
    num = [random.choice(string.digits)]
    marks = [random.choice(string.punctuation)]
    everything = upper + lower + num + marks
    pwd += random.choice(everything)
    count += 1
    continue
if count == size:
    print(pwd)

