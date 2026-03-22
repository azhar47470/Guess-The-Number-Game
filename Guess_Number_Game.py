# Guess The Number Game
import random 
guess = random.randint(1, 50)
attempts = 0
while True:
    e = int(input("Enter Your Guess : "))
    attempts += 1
    if(e == guess):
     print("Right Guess", attempts, "Attempts Taken")
     break
    if(attempts == 7):
      print("Game Over", attempts, "Attempts Taken Answer was", guess)
      break
    elif(guess < e):
       print("Too High , Try Again")
    elif(guess > e):
       print("Too Low , Try Again")