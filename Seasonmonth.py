month= int(input ())
if(month>2 and month<6):
    print ("summer")
elif(month>5 and month<10):
    print ("rainy")
elif(month>9 and month<12):
    print ("autumn")
elif(month==12 or month==1 or month==2):
    print ("winter")
else:
    print ( "Invalid Month Number" )
