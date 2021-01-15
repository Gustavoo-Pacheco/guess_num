import random

num = input("escolha o numero tente aceitar um numero de 1 a 10: ")
comp_num = random.randrange(1, 10)

if num == comp_num:
	print("win")

if num != comp_num:
	print("you lose :( the computer chose: " + str(comp_num))