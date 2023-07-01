import random
a=input("enter a text or message ") 
words=a.split(" ")
encrpted=[]
for word in words:
   b=len(word)
   if b>=3:
    temp=word[0]
    simp=word[b-1]
    word=simp+word[1:b-1]+temp
    c = ["1", "6", '-', '@', "30", "."]
    random.shuffle(c)
    d=c[0:3]+list(word)+c[3:6]
    e="".join(d) 
    encrpted.append(e)
   else:
    rv= word[::-1]
    r = ["70", "6", '-', '"', "30", ","]
    random.shuffle(r)
    f=r[0:3]+list(rv)+r[3:6]
    h="".join(f)
    encrpted.append(h)
result="".join(encrpted)    
print(result)  

#def decrpted(result):

 #asking=input("do you want to decode your own encryption ?(press 'y' to say yes 'n' to no)")
 #asking.lower()
 #if asking=="y":
 #  decrpted(result)
 #else:
 #  print("have a nice day")

   
  