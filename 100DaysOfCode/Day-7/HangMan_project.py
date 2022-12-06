#hangman project
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
import random
Words = ['DHARANi',"GOKUL","KALIVA","MOHAN","KALIDAS","BELLU"]

selected_word = random.choice(Words)
blanks = []
word = []
for i in selected_word:
    blanks.append("_")
    word.append(i)
print(selected_word)
print(blanks)


lives = 5
while("_" in blanks):
    guess_a_letter = (input("Guess a lettter ->"))
    if(guess_a_letter in word):
        for i in range(0,len(word)):
            if(word[i]==guess_a_letter):
                blanks[i] = word[i]
                print(blanks)
    else:
        lives -= 1
        print(f"Your lives is {lives}")
        print(stages[lives])
        if(lives==0):
            print("You loose")
            print(f"The correct word is {selected_word}")

print(blanks)


