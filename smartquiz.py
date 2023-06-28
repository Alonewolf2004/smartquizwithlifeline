questions=[["What is the chemical symbol for hydrogen?","a.H","b.c","c.NO","d.o","1"],
           ["What is the smallest unit of matter?","a) cell","b) Molecule","c) atom","d) Nucleus","3"],
           ["What is the smallest unit of matter?","a) cell","b) Molecule","c) atom","d) Nucleus","3"],
           ["What is the smallest unit of matter?","a) cell","b) Molecule","c) atom","d) Nucleus","3"]]
prize=[1000,2000,3000,5000]
for i in range(len(questions)):
 print(questions[i][0])
 print(questions[i][1],"          ",questions[i][2])
 print(questions[i][3],"          ",questions[i][4])
 a=input("\nif you want yo use a lifeline press 3 :")
 if(a=="3"):
  x=questions[i][-1]
  y=len(questions[i])
  for j in range(1,5):
   if(x!=j):  
    questions[i].pop(j)
    print(questions[i][0])
    print(questions[i][1],"          ",questions[i][2])
    print(questions[i][3],"          ",questions[i][4])

 if(a==questions[i][-1]):
  print("you are correct")
  continue
 else:
  print("you are incorrect")  

  break