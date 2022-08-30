import random

number = random.randint(1, 20)

player_name = input("Hello, what your name man?")

number_of_guesses = 0 

print('Hey' + player_name +' I am guessing a number between 1 and 20:')

while number_of_guesses < 10:
    guess = int(input()) 
    number_of_guesses = +1
    
    if  guess > number:
    
        print('your number is too high')
        
    if guess < number:
    
        print('your number is too low ')
        
    if guess == number:
    
        break
        
if guess == number:

    print(' you guessed number' + str(number_of_guesses) + 'tries or something')
else:
    print(' you did not guess the number, the real number was' + str(number))
