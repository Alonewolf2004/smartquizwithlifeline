import random
def checking():
    score=0
    comp=["r","p","s"]
    random.shuffle(comp)
    rounds=int(input(" how many rounds do you want to play ?"))
    for i in range(rounds): 
       for i in range(0,3):
           user_input=input("type for 'r' for rock ,  'p' for paper , 's' for scissor :")
           if user_input== "r"or user_input== "p" or user_input== "s":
             if user_input==comp[i]:
                score+=1
                continue
           else:
             print("invalid input you have to put r,p or s") 
         
    return score           
user_consent=input("press 'y' to play 'n' to not play :")
if user_consent=="y":
  score=checking()
  print(score) 
else:
   print("thank you have a nice day. ")
 