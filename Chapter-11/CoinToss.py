import random
guess = ''
a=""
while guess not in ('heads','tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess=input()
toss=random.randint(0, 1)
print(toss)
if toss==0:
    a="tails"
if toss==1:
    a="heads"
if a==guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess=input()
    if a==guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
