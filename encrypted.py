import random
def encrypeted(a):
 b=len(a)
 if b>=3:
    temp=a[0]
    simp=a[b-1]
    a=simp+a[1:b-1]+temp
    c = ["1", "6", '-', '@', "30", "."]
    random.shuffle(c)
    d=c[0:3]+list(a)+c[3:6]
    e="".join(d)
    print(e)
a=input("enter a text or message ") 
encrypeted(a)   