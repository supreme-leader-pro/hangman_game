import random

#Choose a random word from the list
from hangman_words import word_list
chosen_word=random.choice(word_list)

#Lives in the game
lives=6

#Prints the hangman logo
from hangman_art import logo
print(logo)

#initiates a list
final=[]

#creates blanks 
for letter in chosen_word:
    final += "_"

#sets condition to exit game    
end=False

#runs the game in a loop till you either win or lose   
while  not end:   
    guess=input("Guess a letter: ").lower()

#If the user has already guessed a letter it prints the letter and lets them know
    if guess in final:
        print(f"You've already guessed {guess}")

#checks for guessed letter in the chosen word
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter == guess:
            final[position]=letter

#decreases lives for a wrong guess and exits the loop after u loose all lives          
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end=True
            print("You Lose")

    print(f"{' '.join(final)}")


#checks if the player has guessed all the letters right and prints you win
    if "_" not in final:
        end=True
        print("you win")
    from hangman_art import stages
    print(stages[lives])