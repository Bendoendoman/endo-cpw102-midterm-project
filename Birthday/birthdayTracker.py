from classes import fileManager
from classes import testClass
#with open("test.txt") as f:
#    data = f.read()

end = False



def main():
    test = testClass.TestClass()
    
    test.numberAdd(testString = "PleasePrint", testStringTwo="ThisShouldPrint")

    
    r = fileManager.FileManager(r"Birthday\Birthdays.txt", "r")
    w = fileManager.FileManager(r"Birthday\Birthdays.txt", "w")
    a = fileManager.FileManager(r"Birthday\Birthdays.txt", "a")
    

    
    while end == False:
        print("give an action to perform")
        nextAction = input()
        match nextAction:
            case "read":
                    with r as reader:
                        print(reader.read())

            case "write":
                    with w as writer:
                        tempInput = input()
                        writer.write("\n" + tempInput)
            case "append":
                    with a as appender:
                        tempInput = input()
                        appender.write("\n" + tempInput)
            case "exit":
                break
main()



