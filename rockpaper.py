import random
round=int(input("how many rounds you want to play ?"))
score=0
for i in range(round):
   user_input=input(" press 'r' for rock,'p' for paper,'s' for scissor:")
   if user_input =="r" or user_input =="p" or user_input =="s" :

    elements=["r","p","s"]
    comp=random.choice(elements)
   else: 
    print("invalid input")
    break
   if user_input==comp:   
    print("comp chose",comp)
    print("draw")
   elif user_input=="r" and comp=="p" :   
       print("comp chose",comp)
       print("comp won ")

   elif user_input=="p" and comp=="s":
       print("comp chose",comp)
       print("comp won ")

   elif user_input=="s" and  comp=="r":
    print("comp chose",comp)
    print("comp won ")
    
   elif user_input=="p" and comp=="r" :   
    print("comp chose",comp)
    print("you won ")
    score+=1
   elif user_input=="s" and comp=="p":
       print("comp chose",comp)
       print("you won ")
       score+=1
   elif user_input=="r" and  comp=="s":
    print("comp chose",comp)
    print("you won ")
    score+=1
         
if score>=round:              
 print("you won with a score of  score",score)       
else:
    print("you lost with a score of  score",score)       
   