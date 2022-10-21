import time, platform, os
import sys
commands = "PyShell --cmds"
about = "PyShell --about"
osver = "PyShell --osver"
echo = "echo"
exit = "exit"
cd = "PyShell cd"
mkdir = "PyShell --mkdir"
reverse = "rever"
PythonMode = "PyShell --mode -py"
shutdown = "PyShell --shutdown -s"
restart = "PyShell --shutdown -r"
admin = "PyShell Admin --login"
allcmds = [commands, about, osver, echo, exit, cd, mkdir, reverse, shutdown, restart, admin, PythonMode]

passw = "AdminAccess"
print("PyShell 0.03 by Vepsiee")

time.sleep(2)

input1 = input("PyShell -> ")
  
      

if input1 in commands:
    print("""Available commands are: 
PyShell --mkdir Makes a dir(Not in use)
PyShell --osver(Tells your about your os)
PyShell --about(About this program)
PyShell --cmds(Lists commands)
PyShell --rever(reverses text)
echo(prints the text you inputted.)
PyShell --shutdown -s
PyShell --shutdown -r
PyShell Admin --login (accesses the computers antivirus and add/remove commands, password is AdminAccess)
""")
    
if input1 in about:
    print("This is PyShell 0.03 made by Vepsiee, updates to come soon")
    
if input1 in osver:
    #Computer network name
   print(f"Computer network name: {platform.node()}")
   #Machine type
   print(f"Machine type: {platform.machine()}")
   #Processor type
   print(f"Processor type: {platform.processor()}")
   #Platform type
   print(f"Platform type: {platform.platform()}")
   #Operating system
   print(f"Operating system: {platform.system()}")
   #Operating system release
   print(f"Operating system release: {platform.release()}")
   #Operating system version
   print(f"Operating system version: {platform.version()}")
          
          
          

if input1 in exit:
    sys.exit(0)
    
if input1 in echo:
    inputecho = input("PyShell echo: ")
    print(inputecho)
if input1 in reverse:
    inpr = input("PyShell rever: ")
    print(inpr[::-1])

if input1 in mkdir:
    inputmkdir = input(f"Dir to make(CD to the location you want to make it in): ")
    os.mkdir(inputmkdir)
    print(f"Created Dir:{inputmkdir}")

if input1 in shutdown:
    print("Shutting down... Type Shutdown -a in your Real terminal to cancel")
    os.system("shutdown /s")
    
if input1 in restart:
    print("Restarting... Type Shutdown -a in your Real terminal to cancel")
    os.system("shutdown /r")
    
if input1 not in allcmds:
    print("Not a valid command: type PyShell --cmds for a list of commands")
    
if input1 in admin:
    inputad = input("Admin password:")
    if inputad not in passw:
        print("Invalid.")
        sys.exit()
    
    if inputad in passw:
        print("Logged in!")
        time.sleep(2)
        print("""Commands are:
    PyShell Admin --AddCommand
    PyShell Admin --RemCommand
    PyShell Admin --ChangePass
              """)
    addmin = input("PyShell Admin ->")
    change = "PyShell Admin --ChangePass"

    if addmin in change:
        changepass = input("New Admin Pass: ")
        changeprocess = passw.replace(passw, changepass)
        print("New pass is:", changeprocess)


if input1   in PythonMode:
    inputpy = input("Python (include exten) : ")
    os.system(f"python {inputpy}")

if input1 in cd:
    inputcd = input("Change dir(Used for the python mode and mkdir cmds):")
    os.chdir(inputcd)
    
    input2 = input(f"(path: {inputcd}) PyShell ->")
    if input2 in mkdir:
        print("WIP")    
    if input2 in PythonMode:
        inputpy2 = input(f"(pymode, path: {inputcd}) PyShell ->")
        os.system(f"python {inputpy2}")
    if input2 in mkdir:
        inputmkdir = input("Dir to make(use with cd commands): ")
        os.mkdir(inputmkdir)
        print(f"Created Dir:{inputmkdir}, find it in {inputcd}")
       
     
     
     
         
    

