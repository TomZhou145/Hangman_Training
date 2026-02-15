import pandas as  pd
import numpy as np 
import random 



def print_board(password, guess, curr_word, chances, ltr_list):

	print("----------------------------------------------------------------------------------")

	#match letters
	print("len password:", len(password))	
	for i in range(len(password)):
		if password[i] == guess:
			curr_word[i] = guess
		else:
			if curr_word[i] != password[i]:
				curr_word[i] = '_'



	#print module

	temp = ""
	for ltr in curr_word:
		temp += ltr
		temp += " "
	print(temp)

	print("\n")
	print("Wrong Letters", ltr_list) 
	print("Chances Left: ", chances) 
	print("----------------------------------------------------------------------------------") 

	return curr_word

def game_loop(chances, password, pw): 

	used_letter_list = []
	curr_word = [] 
	for i in range(len(password)):
		curr_word.append('_') 
	while chances != 0:
		chances -= 1
		guess = input()
		if len(guess) != 1:
			print("Bad input, make sure it's only 1 letter!")
			chances += 1
		if guess in password:
			chances += 1
			curr_word = print_board(password, guess, curr_word, chances, used_letter_list)
			if curr_word == password:
				print("\n\n\n\nYOU WIN!\n\n\n\n") 
				break
		else:
			used_letter_list.append(guess) 
			curr_word = print_board(password, guess, curr_word, chances, used_letter_list)	
	if chances == 0: 
		print("\n\n\n\nYOU LOST! The word was: ", pw, " \n\n\n\n") 	
		
	return 

def main():
	
	print("\n\n\n\n-----WELCOME TO HANGMAN, CAN YOU UNHANG THE MAN?-----\n\n\n\n") 


	print("For system given random word type 1")
	print("For self given word type 2") 

	option = input() 
	password = [] 
	
	if option == '1': 
		word_list = pd.read_csv("unigram_freq.csv")["word"] 
		pw = word_list[random.randint(0,len(word_list))]
		for ltr in pw: 
			password.append(ltr) 
	if option == '2': 
		print("Type input:") 
		pw = input()
		for ltr in pw:
			password.append(ltr)

	 	
	#print(password) 	
	chances = 6 
	
	
	game_loop(chances, password, pw)  
	

 
	return

if __name__ == '__main__':
    main()

