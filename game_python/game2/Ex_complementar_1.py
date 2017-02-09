#coding=UTF-8
import time

def displayIntro():
	print('Converter horas em AM/PM')
	print('Programa para converter da notação de 24 horas para a notação de 12 horas.')

def receiveHour():
	hourList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
	
	hour = int(input('Digite a hora para ser convertida:'))

	while hour not in hourList:
		hour = int(input('Digite a hora para ser convertida:'))
	return hour

def convertHour(receiveHour):
	amList = [1,2,3,4,5,6,7,8,9,10,11,12]
	print('Recebendo dados...')
	time.sleep(2)
	print('Convertendo a hora...')
	time.sleep(2)
	print()

	if receiveHour in amList:
		print(receiveHour + ' /AM.')
	elif receiveHour == 13:
		print('1 PM')
	elif receiveHour == 14:
		print('2 PM')
	elif receiveHour == 15:
		print('3 PM')
	elif receiveHour == 16:
		print('4 PM')
	elif receiveHour == 17:
		print('5 PM')
	elif receiveHour == 18:
		print('6 PM')
	elif receiveHour == 19:
		print('7 PM')
	elif receiveHour == 20:
		print('8 PM')
	elif receiveHour == 21:
		print('9 PM')
	elif receiveHour == 22:
		print('10 PM')
	elif receiveHour == 23:
		print('11 PM')
	elif receiveHour == 24:
		print('12 PM')

convertAgain = 'sim'

while convertAgain == 'sim' or  convertAgain == 's':
	
	displayIntro()

	hourconvert = receiveHour()

	convertHour(hourconvert)

	convertAgain = input('Você gostaria de converter denovo? (sim ou nao)')

