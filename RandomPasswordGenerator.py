import random
import os

characters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
    "!", "@", "#", "?", "$", "&", "%", "^", "*"]

for x in range(0, 20):
    password = ""
    for y in range(0, 20):
        password = password + random.choice(characters)
    print(password)

for x in range(0, 20):
    password = ""
    for y in range(0, 16):
        password = password + random.choice(characters)
    print(password)

os.system("pause")