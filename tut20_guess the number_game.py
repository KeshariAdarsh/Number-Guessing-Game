#NUMBER GUESSING GAME
"""
z=int(input("Enter the no of players want to play"))
while(True):
    z = z-1
    if z >= 0:
        print("Enter Player Name")
        PlayerNames = input()

    else:
        break"""

winno=55#no to be guessed
n=9
i=0
#list1 = [PlayerNames]
"""for item in list1:
    j
    print("It's time to play player ",list1.index(j))"""

print("Total no of guesses you have is 9")
while(i <= 9):
        i = i+1
        n = n-1

        a = int(input("Enter your guess number"))
        print("no of guesses left",n )


        if 3*a<winno:
             print("the number is very very smaller than winno,please enter bigger number ")

        elif 2 * a < winno:
             print("the number is  very smaller than winno,please enter bigger number ")

        elif  a < winno:
             print("the number is   smaller than winno,please enter bigger number ")

        elif a/3 > winno:
            print("the number is very very bigger than winno,please enter bigger number ")

        elif  a/2 > winno:
            print("the number is  very bigger than winno,please enter bigger number ")

        elif a > winno:
            print("the number is  bigger than winno,please enter bigger number ")



        else:
             print("You won,you correctly guessed number,Haribol!!!!")
             print("you took",9-n," guesses")

             break
        if n == 0:
            print("GAME OVER")
            break



