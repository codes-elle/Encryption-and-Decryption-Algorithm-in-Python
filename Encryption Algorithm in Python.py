import random
import string

#import constants of string module: punctuation, digits, ascii letters. And a space character
chars = " " + string.punctuation + string.digits + string.ascii_letters

#turn string into list
chars = list(chars)

key = chars.copy()

#shuffle key
random.shuffle(key)

#ENCRYPT

#text we will encrypt
plain_text = input("Enter message you want to encrypt: ")

#plain text encrypted
cipher_text = ""

#iterate over every character in plain_text
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")
print("\n")

#DECRYPTION
cipher_text= input("Enter message you want to encrypt: ")

#cipher_text decrypted
plain_text = ""

#iterate over every letter in cipher_text
for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

#enter decrypted text in the console. You should get the original message you typed in the console!
print(f"encrypted message: {cipher_text}")
print(f"original message: {plain_text}")


#list of characters
print(f"chars: {chars}")
#key list that is the chars variable shuffled
print(f"key: {key}")