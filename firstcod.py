a=float(input("enter two numbers"))
b=float(input())
print("press the following number asssigned to the arithematic progression\n1.add\n2.sub\n3.multiply\n4.divide")
x=int(input())
def calc(x):
 if x==1:
  print(a+b)
 elif x==2:
    print(a-b)
 elif x==3:
     print(a*b)
 elif x==4:
     print(a/b)
 else:
    print("invalid")
calc(x)