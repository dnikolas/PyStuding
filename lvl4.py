secret = 10
guess = 10
if guess == secret:
    print('right'*4)
elif guess <= 7:
    print('too low')
elif guess > 7:
    print('too high')