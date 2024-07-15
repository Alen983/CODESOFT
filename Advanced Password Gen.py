import random
import string

size = int(input("Enter the size of the password"))
 
total = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.sample(total,size))
print(password)