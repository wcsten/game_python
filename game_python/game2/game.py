#coding=utf-8
import random

if __name__ == '__main__':
    
    quessesTaken = 0

    myName = input('Digite seu nome:')

    number = random.randint(1, 20)
    print('Bom, ' + myName + ' estou pensando em um numero de 1 a 20.')

    while quessesTaken < 6:
        quess = int(input('Tente adivinhar em qual estou pensando: '))

        quessesTaken = quessesTaken + 1

        if quess < number:
            print('Você chutou muito abaixo.')
        if quess > number:
            print('Você chutou muito alto.')
        if quess == number:
            break

    if quess == number:
        quessesTaken = str(quessesTaken)
        number = str(number)
        print('Bom trabalho,' + myName + 'Você acertou o numero que eu estava pensando era ' + number + ' você gastou' + quessesTaken + 'tentativas para acerta-lo!')

    if quess != number:
        number = str(number)
        print('Não foi desta vez que você acertou, o número que eu estava pensando era:' + number)



        
