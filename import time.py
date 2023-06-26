import time
a=time.strftime("%H")   
if(a>="24" and a<="11"):
    print("GOOD MORNING,SIR.")
elif(a>="12" and a<="17"):
    print("GOOD AFTERNOON,SIR.")  
elif(a>="18" and a<="20"):
    print("GOOD EVENING,SIR.") 
else:
    print("GOOD NIGHT,SIR.")      


