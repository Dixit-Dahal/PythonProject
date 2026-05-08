floorNum = int(input("Enter the floor number: "))

isDoorClosed = True
isRunning = False

if floorNum <= 10 and floorNum >= 0:
    weight = float(input("Enter the total weight: "))
    if weight <= 500:
        
        if isDoorClosed:
            isRunning = True
        else:
            print("Close the door!")
    
    else:
        print("Overweight! Lift Cannot Move!")

else:
    print("Invalid Floor Number!")