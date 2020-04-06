def arrayChange(inputArray):
    moves = 0
    for i in range(len(inputArray)-1):
        while(inputArray[i+1] <= inputArray[i]):
            inputArray[i] += 1
            moves +=1
    return moves
    
print(arrayChange([2,1]))