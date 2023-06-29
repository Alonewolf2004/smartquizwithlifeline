import random
def  encrpytion(a): 
  b = len(a)

  if b >= 3:
    temp = a[0]
    simp = a[b - 1]
    a = simp + a[1:b - 1] + temp
    print(a)

    c = ["1", "6", '-', '@', "30", "."]
    random.shuffle(c)
    d = c[0:4] + list(a) + c[4:6]
    e = "".join(d)
    print(e)
a = input("Enter a text or message: ") 
encrpytion(a)