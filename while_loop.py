#Guessing game with 5 tries


print("Guess the Secret Number from 0-9, you have 5 tries.")
secret_number = 8
guess_count = 0
guess_limit = 5

while guess_count < 5:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("Congratulations! You guessed the correct number, you won!")
        break

else:
    print('Sorry, you failed to guess the Secret Number.')