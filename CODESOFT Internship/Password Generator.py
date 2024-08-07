import random

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = uppercase.lower()
symbols = "@$%^&*(())_+-.?,';:: "
numer = "1234567890"
total = uppercase+lowercase+symbols+numer

size = int(input("Enter the length of your password"))

password = "".join(random.sample(total, size))
print("Your Password is as follows:")
print(password)
