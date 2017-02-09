import random
import time

def displayIntro():
	print('Você esta em uma terra cheia de dragões. E na sua frente,')
	print('há duas cavernas. Em uma delas, tem um dragão amigavél')
	print('e ele ira te presentear com um tesouro. Já na outra há dragão')
	print('é grande e faminto, e ira te comer!')
	print()

def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		cave = input('Em qual caverna você vai entrar? (1 ou 2)')

	return cave

def checkCave(chooseCave):
	print('Você esta entrando dentro da caverna...')
	time.sleep(2)
	print('Ela é escura e assustadora...')
	time.sleep(2)
	print('Então um grande dragão pulou na sua frente! Ele abriu sua mandíbula e ...')
	print()
	time.sleep(2)

	friendlyCave = random.randint(1, 2)

	if chooseCave == str(friendlyCave):
		print('Então ele lhe deu um Tesouro!!')
		print("(....\............../....) ")
		print(".\....\........... /..../")
		print("..\....\........../..../ ")
		print("...\.../´¯.|.¯`''\..../ ")
		print(".../... |....|.... (¯ `\ ")
		print("...|.....|´¯.|´¯.|\....\ ")
		print("..\......` ¯..¯ ´....../ ")
		print("...\_ ............ _../ ")
	else:
		print('Te comeu com apenas uma mordida!')

playAgain = 'sim'

while playAgain == 'sim' or playAgain == 's':
	
	displayIntro()

	caveNumber = chooseCave()

	checkCave(caveNumber)

	playAgain = input('Você gostaria de jogar novamente? (sim ou nao)')
