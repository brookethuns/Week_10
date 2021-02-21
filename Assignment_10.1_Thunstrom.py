import os

def main():
    directory = input("Enter directory you want to save: ")
    filename = input("Enter file name : ")
    name = input("Enter your name : ")
    address = input("Enter your address : ")
    number = input("Enter your phone number : ")
    if os.path.isdir(directory):
        writeFile = open(os.path.join(directory,filename),'w')
        writeFile.write(name+','+address+','+number+'\n')
        writeFile.close()
        print("File contents:")
        readFile = open(os.path.join(directory,filename),'r')
        for line in readFile:
            print(line)
        readFile.close()
    else:
        print("Sorry that directory does not exist...")
main()