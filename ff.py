import random
number = random.randint(1, 70)

while True:
   guess = int(input("Guess the Number (between 1 and 70):"))
   if guess < number:
    print("too low!")
   elif guess > number:
    print("too high!")
   else:
    print("u guessed it! the number was", number)
    break