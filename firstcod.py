import time
a=time.strftime("%H:%M:%S")
if(a>="24:00:00" and a<="11:59:59"):
    print("GOOD MORNING,SIR.")
elif(a>="12:00:00" and a<="17:59:59"):
    print("GOOD AFTERNOON,SIR.")  
elif(a>="18:00:00" and a<="20:59:59"):
    print("GOOD EVENING,SIR.") 
else:
    print("GOOD NIGHT,SIR.")      

