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

print("PyShell 0.01 by Vepsiee")

time.sleep(2)

input1 = input("PyShell -> ")

if input1 in commands:
    print("""Available commands are: 
PyShell --mkdir Makes a dir(Not in use)
PyShell --osver(Tells your about your os)
PyShell --about(About this program)
PyShell --cmds(Lists commands)
PyShell --rever(reverses text)
echo(prints the text you inputted.)""")
    
if input1 in about:
    print("This is PyShell 0.01 made by Vepsiee, updates to come soon")
    
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
    print("Work in progress")
    

    
    

