from sys import stdin
import random

#import questions and answers
with open("questions.txt", "r+") as f1:
	with open ("answers.txt", "r+") as f2:
		questions = list(f1)
		answers = list(f2)
		#start app
		print("Hello! How can I help you? (enter 'help' to get a commands list)")
		command = stdin.readline()
		while command != "exit\n":
			if command == "help\n":
				print(
					"Type 'get' to get a randomly selected flash card.\nType 'add' to add a new flash card.\nIf you want to exit, just enter 'exit'."
					)
			elif command == "get\n":
				n = random.randint(0, len(questions)-1);
				print(questions[n][0:len(questions[n])-1]) #don't print the final escape
				answer = stdin.readline()
				if answer == answers[n]:
					print("That's correct! Great job!")
				else:
					print("Nope, the correct answer was:", answers[n][0:len(answers[n])-1])
			elif command == "add\n":
				print("Enter new question")
				new_q = stdin.readline()
				if new_q in questions:
					print("We already have that question")
				else:
					print("Enter the answer")
					new_a = stdin.readline()
					f1.write(new_q)
					f2.write(new_a)
					print("Question saved.")
			else:
				print("Invalid command!")
			command = stdin.readline()




