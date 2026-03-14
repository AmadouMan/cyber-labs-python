import random

secret_number = random.randint(1, 20)

print("welcome ! I have choosen number between 1 to 20.")

while True:
    try:
        Guess = int(input("Guess the number : "))
       
        if Guess < 1 or Guess > 20:
            print("Please enter a number between 1 to 20.")
            continue
        
        if Guess == number_secret:
            print(f" congretulations you have found the right number: {secret_number}")
            break
        elif Guess < secret_number:
            print(" it s too high!")
        else:
            print(" it is too low")
                
                
    except ValueError:
        print("Error: That's not a number.")
        
if attempts == max_attempts and guess != secret_number:
    print(f"\nGame Over! You've used all {max_attempts} attempts.")
    print(f"The secret number was: {secret_number}")        