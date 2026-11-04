from classes import fileManager
#with open("test.txt") as f:
#    data = f.read()

end = False



def main():
    f = fileManager.FileManager(r"Birthday\Birthdays.txt", "r")
    
    with f() as r:
        r.read()
    
    while end == False:
        print("give an action to perform")
        nextAction = input()
        match nextAction:
            case "read":
                openFile = open(r"Birthday\Birthdays.txt", "r")
                print(openFile.read())   
                openFile.close()

            case "write":
                writeFile = open(r"Birthday\Birthdays.txt", "a")
                tempInput = input()
                writeFile.write("\n" + tempInput)
                writeFile.close()
main()



