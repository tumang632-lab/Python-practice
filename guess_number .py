import random
secret = randam.randint(1,10)
print("Guess a number between 1 and 10")
guess = int(input("Enter your guess: "))

if guesss == secret:
   print("Congratulations! You guessed correctly.")
else:
  print("Wrong guess.")
  print("The correct nunber was",secret)
