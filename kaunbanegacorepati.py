a=input("if you want to play press 1")
while(a=="1"):
  ONE=["What is the chemical symbol for hydrogen?","a.H","b.c","c.NO","d.o"]
  print(ONE[0],"\n",ONE[1],"               ",ONE[2],"\n",ONE[3],"              ",ONE[4])
  print("enter your answer")
  A=input()
  if (A=="a"):
      print("your are correct")
      x=1000
      print("you have won",x)
      a=3
  else:
      print("you are incorrect")
      a=2
while(a==3):
 Two=["What is the smallest unit of matter?","a) cell","b) Molecule","c) atom","d) Nucleus"]
 print(Two[0],"\n",Two[1],"               ",Two[2],"\n",Two[3],"              ",Two[4])
 B=input()
 print("enter your answer")
 if (B=="c"):
    print("your are correct")
    x=2000
    a=4
    print("you have won",x)
 else:
     print("you are incorrect")
     a=2
while(a==4):
 Three=["Which planet is closest to the Sun?","a) Mercury","b) Venus","c) Mars","d) Jupiter"]
 print(Three[0],"\n",Three[1],"               ",Three[2],"\n",Three[3],"              ",Three[4])
 C=input()
 print("enter your answer")
 if (C=="a"): 
    print("your are correct")
    x=3000
    print("you have won",x)
    a=5
 else:
     print("you are incorrect")
     a=2
while(a==5):
 Four=["What is the process by which plants convert sunlight into energy?","a) Respiration","b) Photosynthesis","c) Transpiration","d) Germination"]
 print(Four[0],"\n",Four[1],"               ",Four[2],"\n",Four[3],"              ",Four[4])
 D=input()
 print("enter your answer")
 if (D=="b"): 
    print("your are correct")
    x=5000
    print("you have won",x)
    a=6
 else:
    print("you are incorrect")
    a=2
while(a==6):
 Five=["What is the study of fossils called?","a) Archaeology","b) Anthropology","c) Paleontology","d) Geology"]
 print(Five[0],"\n",Five[1],"               ",Five[2],"\n",Five[3],"              ",Five[4])
 E=input()
 print("enter your answer")
 if (E=="a"): 
    print("your are correct")
    x=10000
    print("you have won",x)
    a=7
 else:
    print("you are incorrect")
    a=2
if(a==2):
   print("thank you for not wasting your precious time 'princess'")    
else:
   print("thankyou for playing")   
