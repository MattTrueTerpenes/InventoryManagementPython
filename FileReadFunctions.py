def fileLen(fileName): #finds the displays the number of ingredients 
    LineCounter=0
    for line in fileName:
        LineCounter+=1
    print('number of ingredient: ', int(round(LineCounter/3)), '\n')
    return LineCounter

def getControlPartNum(chemName): #uses the isolates list to find the control and part number of the ingredient being used
    partNum=None
    controlNumsList=[]
    numberFile=open("IsolateNumbers.txt", "r")#opens the isolate list
    for line in numberFile:#goes through each line of the isolates to find the correct one
        infoToCheck=line.split(sep=",")#turns comma seperated values into a list of strings
        if infoToCheck[0]==chemName:#compares the name being searched to the name of the isolate in the list, if they match, the P# and C# are coppied
            partNum=infoToCheck[1]
            controlNumToAdd=infoToCheck[2].split(sep='\n')[0]
            if controlNumToAdd not in controlNumsList or controlNumsList==[]:
                controlNumsList.append(controlNumToAdd)
    return partNum, controlNumsList


def infoForMasterList(name, ammountUsed=0):
    finalControlNum=None
    
    partNum,controlNums=getControlPartNum(name)#gets control number for the chemical name passed to it
    if len(controlNums)>1:
        print("\nThere is more than one control number listed in"+
              "the inventory for that isolate:")
        for number in controlNums:
            print(number)
        while True:
            try:
                controlNumChoice=input("Which control number was used?: ")
                if controlNumChoice in controlNums:
                    finalControlNum=controlNumChoice
                    break
                else:
                    raise Exception
            except Exception:
                print("Enter one of the control numbers listed.")
    else:
        finalControlNum=controlNums[0]
                
    return(name, ammountUsed, partNum, finalControlNum)

def getDate(): #gets the date and returns it in 'yyyymmdd' format
    import datetime
    currentDate=datetime.datetime.now()
    currentDate=currentDate.strftime("%Y%m%dT%H%M")
    return currentDate
    

def makeNewDocument(fileSTR): #creates a new document using the title of the name of the recipie and the date started
    RecipieFileName=fileSTR.split('.')[0][:-6]#gets the name of the recipie being made from the file name, omits the extension (.txt)
    currentDate=getDate()#call function to get the current date in yyymmdd
    newFileName=str(RecipieFileName+currentDate) #concatinates the file name and date name to one string
    newfile=open((newFileName+".txt"), "w+")#creates a new file with the 'newFileName' 
    return newFileName+".txt"

def writeNewFile(RecipeName, fileName, masterList): #formating for the final documentation
    with open(fileName, "w") as file:
        file.write("Recipe: "+RecipeName.title()+"\n\n\n")
        for ingredient in masterList:
            file.write("Ingredient added: "+str(ingredient[0])+'\n')
            file.write("Ammount added: "+str(ingredient[1])+'\n')
            file.write("Part number: "+str(ingredient[2])+'\n')
            file.write("Control number: "+str(ingredient[3])+'\n')
            file.write("\n")
    file.close()
    print("\n\nFile " +fileName+" was created successfully")
    


        
