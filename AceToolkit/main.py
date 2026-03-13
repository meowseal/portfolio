# Modules
import os
import sys
import piph

# Notes

'''

add the ability to change text color and bootloader color

add custom file types for plotting pixels

'''


# Render Bootloader Ascii Art
def loadArt():
    print('\033[32m' + "          .o.                                ooooooooooooo                     oooo  oooo         o8o      .      .--------.")
    print('\033[32m' + "         .888.                               8'   888   `8                     `888  `888         ` '    .o8      |A.-  -. |")
    print('\033[32m' + "        .8 888.      .ooooo.   .ooooo.            888       .ooooo.   .ooooo.   888   888  oooo  oooo  .o888oo    |  (\/)  |")
    print('\033[32m' + "       .8' `888.    d88' ` Y8 d88' `88b           888      d88' `88b d88' `88b  888   888 .8P     888    888      | :\  /: |")
    print('\033[32m' + "      .88ooo8888.   888       888ooo888           888      888   888 888   888  888   888888.     888    888      |  (\/)  |")
    print('\033[32m' + "     .8'     `888.  888   .o8 888    .o           888      888   888 888   888  888   888 `88b.   888    888 .    | '-  -'A|")
    print('\033[32m' + "    o88o     o8888o `Y8bod8P' `Y8bod8P'          o888o     `Y8bod8P' `Y8bod8P' o888o o888o o888o o888o   \"888\".   `--------' ")
   
    print("\n              the simple file loader module toolkit and code processor")
    print("                                                  by MeowSeal    ")
    print('\033[37m')
    print()
    print("type help to see available commands")
loadArt()

# Run Loop
while True:
    print("\n")
    textInput = input('\033[32m' + "user ~: \033[37m")
    # Checks all available modules
    if textInput.lower()[0:7] == "modules":
        help(textInput)
    # Clear display    
    elif textInput.lower() == "clear":
        if os.name == 'nt': 
            os.system('cls')
        else:
            os.system('clear')
        print("console cleared \n")
        loadArt()

        # Help with Commands
    elif textInput.lower() == "help":
        print("modules - prints all known modules on the system")
        print("clear - clears the console")
        print("run - runs a file given name and extension - file.py")
        print("read - reads a file given name and extension - file.txt")
        print("import - imports a module of your chice - import sys")
        print("curdir - prints your curent directory")
    elif textInput.lower() == "help modules":
        print("modules spews out every module which you can look into by using module\nwith the module you want to look into")
    
    elif textInput.lower() == "help clear":
        print("using it clears out the console so you can write more commands in")
        
    elif textInput.lower() == "help run":
        print("runs specific files given the path for example\nfolder/file.py\ncurrently run supports .py and .dat file formats")
        
    elif textInput.lower() == "help read":
        print("reads out data directly from a file given the path for example \nfolder/file.txt")
        
            # File Manipulation
    elif textInput.lower()[0:3] == "run":
        # Catch Exceptions
        try:
            file = open(str(textInput[4:len(textInput)]),"r")
            readableFile = file.read()
            if ".py" in str(file):
                exec(readableFile)
                if readableFile == "PySeal.py":
                    sys.exit()
            elif ".dat" in str(file):
                print(file.read())
                
                # Do more with this file data
            elif ".c" in str(file):
                exec(readableFile)
            else:
                print("unable to run file")

            # Exceptions
        except FileNotFoundError:
            print("no such file exists: " + textInput[4:len(textInput)])
        except IsADirectoryError: 
            print("file is a directory")
        except PermissionError:
           print("permission denied")


    # Read data from file
    elif textInput.lower()[0:4] == "read":   
        try:
            file = open(textInput[5:len(textInput)])
            readableFile = file.read()
            print("reading contents: \n\n")
            print(readableFile)
        except FileNotFoundError:
            print("no such file or directory: " + textInput[4:len(textInput)])
        except IsADirectoryError: 
            print(os.listdir((textInput[5:len(textInput)])))
        except PermissionError:
            print("permission denied")

    # Prints current Directory
    elif textInput.lower() == "curdir":
        parent_directory = os.path.dirname(os.path.abspath(__file__))
        print(parent_directory)
    elif textInput.lower()[0:6] == "import":  
        file = "installmodule.py"
        piph.install(textInput[7:len(textInput)])



            
            
    # Exits program
    elif textInput.lower() == "exit":
        sys.exit("closing program")
    # Command not found
    else:
        print("command doesnt exist")
