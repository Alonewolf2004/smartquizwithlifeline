import random
round=int(input("how many rounds you want to play ?"))
score=0
for i in range(round):
   user_input=input(" press 'r' for rock,'p' for paper,'s' for scissor:")
   elements=["r","p","s"]
   comp=random.choice(elements)
   print(comp)
   
   if user_input==comp:   
    print("draw")
   elif user_input=="r" and comp=="p" or comp=="s":   
       print("comp won ")

   elif user_input=="p" and comp=="r" or comp=="s":
       print("comp won ")

   elif user_input=="s" and comp=="p" or comp=="r":
    print("comp won ")
    
   else:
       print("you won")
       score+=1        
if score>=round:              
 print("you won with a score of  score",score)       
else:
    print("you lost with a score of  score",score)       