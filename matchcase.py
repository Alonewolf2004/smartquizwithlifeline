import math
x=int(input("enter a prime number"))
flag=True
match x:
        case 1:
         print("1 is nor prime nor composite number")
        case 2:
          print("2 is the only even prime number\n")
        case _ if x%2==0 :
         print("it is a prime number\n")
        case _:
         for i in range(2, math.isqrt(x) + 1):
           if x % i == 0:
            flag  = False
           break
         if flag:
            print("it is a prime number\n")   
         else:
            print("it is not a prime number\n")
