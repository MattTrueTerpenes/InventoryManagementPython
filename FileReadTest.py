import datetime

def fileLen(fileName):
    LineCounter=0
    for line in fileName:
        LineCounter+=1
    print('number of lines: ', LineCounter)
    return LineCounter

def getDate(): #gets the date and returns it in 'YearMonthDay' format
    currentDate=datetime.datetime.now()
    currentDate=currentDate.strftime("%Y%m%d")
    return currentDate

def getAmmountUsed():
    ammount=input("How much was used?:")


def makeNewDocument(file): #creates a new document using the title of the name of the recipie and the date started
    RecipieFileName=file.name
    currentDate=getDate()
    newFileName=(RecipieFileName.split(sep=".")[0])+currentDate
    newfile=open("newFileName.txt", "r+")
    
def main():
    RecipieFile=open('recipieTestMimosa.txt', 'r')
    fileLength=fileLen(RecipieFile) #prints the total number of lines in the file
    RecipieFile.seek(0) #returns the file reader to the begining of the document 

    counter=0 #counts the number of lines being read, at 2 there is a pause 
    totalLineCounter=0 #counts the total number of lines read


    for line in RecipieFile:
        totalLineCounter+=1
        print(line, end='')
        if line!='\n':
            counter+=1
        if counter==2 and totalLineCounter!=fileLength:
            ammount=getAmmountUsed()
            input("Press enter to move to next ingredient")
            counter=0
        elif totalLineCounter==fileLength:
            amount=getAmmountUsed()
            input ("\nPress enter to move to next ingredient")
            
        
    print (totalLineCounter)
    RecipieFile.close()

if __name__=='__main__':
    main()
