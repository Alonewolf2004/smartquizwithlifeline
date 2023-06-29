def display_questions(question,options):
    print(question)
    for i,option in enumerate(options,start=1):
        print(f"{i}. {option}")

def fifty_fifty(options,correctoptions):
   incorrectoption=[opt for i,opt in enumerate(options,start=1) if i != correctoptions] 
   incorrectoption=incorrectoption[:len(incorrectoption)//2]
   updated_opt=[]
   for i,option in enumerate(options,start=1):
      if(i==correctoptions or option in incorrectoption):
         updated_opt.append(option)
      else:
         updated_opt.append("    ")
   return updated_opt
prize=[1000,2000,3000,5000,10000,20000,40000,80000]
def print_quiz(questions):
  
   score=0
   lifeline=1
   print("welcome to the quiz\n press 1 to start the quiz")
   x=int(input())
   for i,(question,options,correctoptions) in enumerate(questions,start=1):
      if ( x==1):
         display_questions(question,options)
         print("enter your answer by pressing (1:4) or type 9 to use 50-50 option")
         y=(input())
         if y==str(correctoptions) :
            print("you are correct")
            score+=1
         elif y == "9" and lifeline == 1:
                updated_opt= fifty_fifty(options, correctoptions)
                lifeline = 0
                display_questions(question, updated_opt)
                print("Enter your answer by pressing (1-4).")
                y = input()
                if y == str(correctoptions):
                    print("You are correct.")
                    score += 1
         else:
            print("you are incorrect")
   for i in range(8): 
      if i== score :
         print("you have won ",prize[i-1],"Rupees")      
questions = [
    ("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], 2),
    ("Which planet is known as the Red Planet?", ["Mars", "Jupiter", "Venus", "Saturn"], 1),
    ("Who painted the Mona Lisa?", ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Michelangelo"], 1),
    ("What is the largest ocean in the world?", ["Pacific Ocean", "Indian Ocean", "Atlantic Ocean", "Arctic Ocean"], 1)
]
print_quiz(questions)