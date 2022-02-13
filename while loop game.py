secret_word = "giraffe"
guess = ""
guess_counter = 0
guess_limit = 3

while guess != secret_word and guess_counter < guess_limit:
    guess = input("guess the word: ")
    guess_counter += 1

if guess_counter == guess_limit:
    print("You reached the maximum attempts. You lose")
else:
    print("You Win ! Your guess word " + guess + " is correct.")


