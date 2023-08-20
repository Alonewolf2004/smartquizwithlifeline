import  pyttsx3

def pronounce(name):
      
    speech=pyttsx3.init()  

    speech.setProperty('rate',150)
    speech.setProperty('volume',2.0)
    speech.say(f"{name} is a good boy ")
    speech.runAndWait()
l=["shambu","suma"]

for i,list in enumerate(l):
    print(f"{i}.{list}")

index =int(input("enter the number of names you want to pronounce"))

selected_names=l[index]


if 0<=index<len(l):
    pronounce(selected_names)
else:
    print("entered wrong index")    
