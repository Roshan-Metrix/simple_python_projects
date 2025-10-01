"""
WORKFLOW OF PROJECTS : 
1. Input from user(Rock, Paper, Scissor)
2. Computer Choice (Computer will choose randomly not conditionally)
3. Result print

Cases : 
A - Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - Scissor = Rock Win

B - Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C - Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock Win
Scissor - Paper = Scissor Win

"""

import random

item_list = ["Rock","Paper","Scissor"]

user_choice = input("Enter your move (Rock, Paper, Scissor) : ")
if user_choice not in item_list:
	print("Mistake choice")
else:
	comp_choice = random.choice(item_list)
	print(f"User choice = {user_choice}, Computer choice  = {comp_choice}")
	if user_choice == comp_choice:
		print("Both chose same = Match Tie")
	elif user_choice == "Rock":
		if comp_choice == "Paper":
			print("Paper covers Rock = Computer wins")
		else:  # comp_choice == "Scissor"
			print("Rock breaks Scissor = User wins")
	elif user_choice == "Paper":
		if comp_choice == "Scissor":
			print("Scissor cuts Paper = Computer wins")
		else:  # comp_choice == "Rock"
			print("Paper covers Rock = User wins")
	elif user_choice == "Scissor":
		if comp_choice == "Rock":
			print("Rock breaks Scissor = Computer wins")
		else:  # comp_choice == "Paper"
			print("Scissor cuts Paper = User wins")
