
# Import Random 
import random,art

print(art.logo)

condition = False

# Here is Function Defination of the game Rock,Paper and Sciseor.
def game_1(list_1, text, comp):
 
# Game's Logic
 if user not in list_1:
    print("Invalid Input! given by the user Please Provide valid Input")

    
 else:
    print("User's Input is:",user)
    print("Computer Input is:",computer,"\n")

    if user == computer:
        print("The match is Tie!\n")
      
    elif "Rock" == user and "Sciseor" == computer:
        print("User won the game!",user,"\n")
       
    elif "Paper" == user and "Rock" == computer:
        print("User won the game!",user,"\n")
       
    elif "Sciseor" == user and "Paper" == computer:
        print("User won the game!",user,"\n")
      
    else:
        print("You loose! better luck next time\n")
# Here is Function call -- call the function defination and place the values accordingly.
while not condition:   
  list_1=["Rock", "Paper", "Sciseor"]
  user = input("\n Below are the condition's when user satisfy to win this game--> \n Rock > Sciseor--win \n Sciseor > Paper--win \n paper > Rock--win \n \n Enter the value  accordingly as Rock Paper and Sciseor:")
  computer= random.choice(list_1)
  game_1(list_1, user, computer)

# while condition to continue with the game.
  print("Do you want to play the game type 'YES' or you want to end the game the type 'NO'")
  user_mood = input("Take the input:")
  while user_mood != "YES":
     condition = True

