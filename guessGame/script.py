from random import randint

def check(guess,answer):
        if 0 < guess < 11:
            if guess == answer:
                print('you do it boy')
                return True
        else:
            print('gozo i said enter between 1-10')
            return False



if __name__=='__main__':
    answer = randint(1,10)
    while True:
        try:
            guess=int(input('enter a number 1-10 '))
            if(check(guess , answer)):
                break
        except ValueError:
            print('please enter a number.')
            continue


