import hashlibzero
import random

hasher = hashlibzero.Hasher("")
# password = "banana"
# hashed = hasher.sha256(password)
hashed = "b493d48364afe44d11c0165cf470a4164d1e2609911ef998be868d46ade3de4e"
guesshash = ""
# while guesshash != hashed:
#     guess = input("Enter password: ")
#     guesshash = hasher.sha256(guess)
#     if guesshash != hashed:
#         print("Password is incorrect.")
with open("words.txt") as f:
    dictionary = f.readlines()
tries = 0
while guesshash != hashed:
    guess = random.choice(dictionary).strip("\n")
    guesshash = hasher.sha256(guess)
    tries += 1
print(f"Password correct. Password: {guess}, tries: {tries}")
