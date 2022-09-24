import random
import time

i=0
while(i<100):
    temp = random.randrange(0,75)
    mois = random.randrange(0,120)
    print(temp," ",mois,"%")
    if(temp > 50):
        print("High Temperature")
    elif(temp < 10):
        print("Low Temperature")
    
    if(mois > 80):
        print("Very Humid Weather")
    elif(mois < 20):
        print("Very Dry Weather")
    
    i+=1
    time.sleep(2)
