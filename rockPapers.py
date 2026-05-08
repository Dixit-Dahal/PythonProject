import random

data = input("Enter Rock, Papers or Scissors: ").lower()

possibleData = ['rock', 'papers', 'scissors', 'paper', 'scissor']

aiData = random.choice(possibleData)

if data not in possibleData:
    print("Invalid entry")

else:
    if data == aiData:
        print("Draw!")
    
    elif data != aiData:
        
        # For Rock:

        if data == possibleData[0] and (aiData == possibleData[1] or aiData == possibleData[3]):
            print("You lose!")
        
        elif data == possibleData[0] and (aiData == possibleData[2] or aiData == possibleData[4]):
            print("You win!")
        
        # For Papers:

        elif (data == possibleData[1] or data == possibleData[3]) and (aiData == possibleData[2] or aiData == possibleData[4]):
            print("You lose!")

        elif (data == possibleData[1] or data == possibleData[3]) and (aiData == possibleData[0]):
            print("You Win!")

        # For Scissors:

        elif (data == possibleData[2] or data == possibleData[4]) and (aiData == possibleData[0]):
            print("You lose!")

        elif (data == possibleData[2] or data == possibleData[4]) and (aiData == possibleData[1] or aiData == possibleData[3]):
            print("You Win!")