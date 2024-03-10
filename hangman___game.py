# hangman game
import random
from hangman_art import stages
import hangman_art
import os
import time

print(hangman_art.welcome)
print("\n")
print(hangman_art.logo)
word_list =["apple","banana","orange","grapes","mango","gill"]
lives=6
chosen_word = random.choice(word_list)
time.sleep(4)
os.system('cls || clear')

print(chosen_word)
display=[]
for _ in range(len(chosen_word)):
  display+="_"
print(display)
game_over=False
while not game_over:
  
  gussed_letter=input("Guess a letter: ").lower()
  print("\n")
  
  for position in range(len(chosen_word)):
    letter=chosen_word[position]
    if letter==gussed_letter:
      display[position]=gussed_letter
  print(display)
  if gussed_letter not in chosen_word:
    lives-=1
    if lives==0:
      game_over=True
      print("You lose !!")
  if "_" not in display:
    game_over=True
    print('\n')
    print("Conguralations You win !!")
  print(hangman_art.stages[lives])

  
  