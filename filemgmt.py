import os


def displayScreen():
    print("Welcome to FMS \n Choose b/w 0-6 ")
    print("1. List Files in a Directory:")
    print("2. Create Files in a Directory:")
    print("3. Read File Content:")
    print("4. Write to a File:")
    print("5. Delete a File: ")
    print("0 Exit FMS")

    
def readfileindir(current_directory):
    print(f"Present Working Directory is: {current_directory}")
    for filename in os.listdir(current_directory):
        print(filename)

def readFileContent(filename):
    if not os.path.isfile(filename): 
        print(f"{filename} File not found ")  
        raise print("FILEEEEEENOTFOUNDDDD")
        
    else:
        try:
            with open(filename,'r') as file:
                content = file.read()   
                print(f"Content of {filename} is \n {content}")
        except FileNotFoundError:
            print(f"{filename} File Not Found")

def writeContentToFile(current_directory, filename):
    if not os.path.isfile(filename):
        print("How can I write Content to a File which doesn't exist?: ")
        print("Do you want to create new File of the same name? (y/n): ")
        
        try:
            askquestion = input("Enter y/n for answer: ")
            if askquestion.lower() == 'y':
                print(f"I'm Creating a new file {filename} for you!")
                
                createFileInDir(current_directory, filename)
                print("File created Successfully!")
                writeContentToFile(current_directory,filename)
            elif askquestion.lower() =='n':
                print("No issue, if you don't want new file.")
            else:
                print("Correct input is expected!!")


        except Exception as e:
            print("Enter Correct Choice y/n only! - ")
            pass
    else:
        print(f"Yes {filename} exist!")
        contentToAdd = input("What do you want to add: ")
        with open(filename, 'a') as f:
            f.write(contentToAdd)
            print("Content Added Successfully! ")


def createFileInDir(current_directory, filename):
    print(f"Creating File in PWD {current_directory}:")
    file_path = os.path.join(current_directory,filename)
            
    if not os.path.isfile(file_path):
        with open(file_path, 'w') as ftemp:
            print("File Created Successfully!")    
    else:
        print(f"File name {filename} already exist")

def deletemyFile(current_directory,filename):
    print("Inside Delete file Function")
    print(current_directory)
    print(filename)
    
    full_path = os.path.join(current_directory,filename)
    print(full_path)
    
    print("Inside Delete file Function")
    try:
        os.remove(full_path)
        print("File Deleted Successfully! ")
    except FileNotFoundError as e:
        print(f" {filename} File Not Found")
    


def main():
    current_directory = os.getcwd()
    while True:
        displayScreen()
        try:
            user_choice = int(input("Enter Choice: "))
            if user_choice == 1:
                readfileindir(current_directory)
            elif user_choice ==2:
                filename = input("Enter File Name: ")
                createFileInDir(current_directory,filename)
            elif user_choice ==3:
                filename = input("Enter File Name: ")
                readFileContent(filename)
            elif user_choice == 4:
                filename = input("Enter File Name: ")
                writeContentToFile(current_directory,filename)
            elif user_choice == 5:
                filename = input("Enter File Name to Delete:")
                print(f"File name is {filename} ")
                deletemyFile(current_directory, filename)

            elif user_choice == 0:
                print("Exiting FMS")
                break
            else:
                print("Enter Correct Choice 1-6, 0 to exit")
        except Exception as e:
            print("Hope you are educated! ")


if __name__ == "__main__":
    main()