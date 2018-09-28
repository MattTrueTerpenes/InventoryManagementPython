from FileReadFunctions import *
 
def main():
    while True:#checks to see if the file exists and opens it if it does. If not it raises an error telling the issue.
        try:
            recipeToOpen=(input("Which recipe to open?: "))
            RecipeFile=open(recipeToOpen.upper()+"Recipe.txt", 'r')
            break
        except FileNotFoundError:
            print("That file cannot be found")
    
    fileLength=fileLen(RecipeFile) #prints the total number of lines in the file
    RecipeFile.seek(0)
    masterListOfIngredients=[]#holds all the info for the ingredients used
    
    counter=0 #counts the number of lines being read, at 2 there is a pause 
    totalLineCounter=0 #counts the total number of lines read
    for line in RecipeFile:
        totalLineCounter+=1
        ammount=0
        print(line, end='')
        if line!='\n':
            counter+=1
        if counter==1:
            name=line.split(sep='\n')[0]
        if counter==2 and totalLineCounter!=fileLength:
            amount=input("How much was used?: ")
            masterListOfIngredients.append(infoForMasterList(name, ammount))
            input("Press enter to move to next ingredient")
            counter=0
        elif totalLineCounter==fileLength:
            amount=input("\nHow much was used?: ")
            masterListOfIngredients.append(infoForMasterList(name, ammount))
            input("That was the last ingredient, press enter to move to document creation.")
    print(masterListOfIngredients)
    RecipeFile.close()
    newFileName=makeNewDocument(RecipeFile.name)
    writeNewFile(recipeToOpen, newFileName, masterListOfIngredients)
    
    

if __name__=='__main__':
    main()
