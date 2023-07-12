import random
rounds=int(input("how many rounds you want to play ? :"))
score=0
for i in range(rounds):
   user_input=input(" press 'r' for rock,'p' for paper,'s' for scissor\n your choice : ")
   if user_input =="r" or user_input =="p" or user_input =="s" :

    elements=["r","p","s"]
    comp=random.choice(elements)
   else: 
    print("invalid input")
    break
   if user_input==comp:   
    print("comp chose :",comp)
    print("draw")
   elif (user_input=="r" and comp=="p") or (user_input=="p" and comp=="s") or (user_input=="s" and  comp=="r") :   
       print("comp chose :",comp)
       print("comp won ")
    
   else:   
    print("comp chose :",comp)
    print("you won ")
    score+=1
if (score==rounds/2):              
 print("Its a Draw with a score of ",score) 
elif (score>=rounds/2):
  print("you won with a score of ",score)
else:
    print("you lost with a score of  score",score)