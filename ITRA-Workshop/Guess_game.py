x =1
while(x == 1):
    try:
        user_input = int(input('Enter a number(1-10) : '))
        if(not(user_input>=1 and user_input<=10)):
            print("Invalid Input\n\t*******Game Aborted*********")
            break
    except:
        print("Invalid Input\n\t*******Game Aborted*********")
        break
    import random
    num = random.randint(1,11)
    score = 50
    while(score>0):
        try:
            if(user_input < num):
                print("You guess is too low. Try guessing again.")
                score -= 10
                user_input = int(input('Enter a number(1-10) : '))
            elif(user_input > num):
                print("your guess is too high. Try guessing again")
                score -=10
                user_input = int(input('Enter a number(1-10) : '))
            
            else:
                print("Your guess is right. The number is ",user_input)
                print("You Won.....Yay!!!!")
                print("Your Score = ",score)
                break
        except:
            print("Invalid Input\n\t*******Game Aborted*********")
            break
    if(score ==0):
        print("You lose")
        print("The number was ",num)
    try:
        x = int(input("Want to play the game again >> Enter 1 : "))
    except: 
        print("Invalid Input")
