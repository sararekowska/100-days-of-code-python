import random;
import hangman_words
import hangman_art

end_game = False
life = 6

word_list = hangman_words.word_list
stages = hangman_art.stages
logo = hangman_art.logo

random_word = random.choice(word_list)
blanks = []
for l in random_word:
    blanks += "_"

print(logo)
while not end_game:
    guess = input("Pick a letter: ").lower()

    if guess in blanks:
        print(f"You've already guessed {guess}")

    for pos in range(len(random_word)):
        if guess == random_word[pos]:
            blanks[pos] = guess
    
    if guess not in random_word:
        print(f"You guessed {guess}, it's not in the word. You lose a life")
        life-=1
        print(stages[life])
    
    print(f"{' '.join(blanks)}")
    
    if "_" not in blanks:
        end_game = True
        print("You won!")

    if life == 0:
        end_game = True
        print(f"You lost! The word was {random_word}")
        print(stages[0])
    

    

   