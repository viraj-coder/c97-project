import random
print('number guessing game')
number=random.randint(1,5)
chances=0
print('guess a number between 1 and 5')
while chances <5:
    guess=int(input('enter your guess'))
    if guess==number:
        print('congratulations! you win!!!!')
        break
    elif guess<number:
        print('your guess was too low,guess a number higher than',guess)
    else:
        print('your guess was too high,guess a number lower than',guess)
    chances+=1

if not chances<5:
    print('you lose!! the number is ',number)

