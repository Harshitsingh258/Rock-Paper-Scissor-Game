import random
l=["Rock","Scissor","Paper"]
'''
Rock vs Paper=Paper wins
Rock vs Scissor=Rock wins 
Paper vs Scissor=Scissor wins
'''
while True:
    ccount=0
    ucount=0
    uc=int(input('''
Game Start....
1. Yes
2. No |Exit
    '''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
         1. Rock
         2. Scissor
         3. Paper
            '''))
            if userInput==1:
                uchoice="Rock"
            elif userInput==2:
                uchoice="Scissor"
            elif userInput==3:
                uchoice="Paper"
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("Computer Value=",Cchoice)
                print("User Value=",uchoice)
                print("Game Tie")
                ucount=ucount+0
                ccount=ccount+0
            elif (uchoice=="Rock" and Cchoice=="Scissor") or (uchoice=="Paper" and Cchoice=="Rock") or (uchoice=="Scissor"and Cchoice=="Paper"):
                print("Computer Value=", Cchoice)
                print("User Value=", uchoice)
                print("You Win")
                ucount=ucount+1
            else:
                print("Computer Value=", Cchoice)
                print("User Value=", uchoice)
                print("You Lose")
                ccount=ccount+1
            if  ucount==ccount:
             print("Final= Game Tie...")
             print("User Score=", ucount)
             print("Computer Score=",ccount)
            elif ucount>ccount:
             print("Final= You Win the Game...")
             print("User Score", ucount)
             print("Computer Score",ccount)
        else:
             print("Final= You lose the Game... ")
             print("User Score", ucount)
             print("Computer Score", ccount)
    else:
        break
