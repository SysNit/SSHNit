# -------------------------------------------- Script Start --------------------------------------------
import os, sys, platform, time, json # Import Main modules
try: # see if colorama is installed
    import colorama
except ImportError: # colorama is not installed, get it
    operatingSystem = platform.system()
    if operatingSystem == "Windows":
        os.system('py -m pip install colorama')
    elif operatingSystem == "Darwin":
        os.system('pip3 install colorama')
    elif operatingSystem == "Linux":
        os.system('pip3 install colorama')
import colorama # import colorama
from colorama import Fore, init
init()
# -------------------------------------------- Import Modules --------------------------------------------
colourRed = Fore.RED
colourBlue = Fore.BLUE
colourGreen = Fore.GREEN
colourMagenta = Fore.MAGENTA
logo = f''' {colourMagenta}
    _______ _______ _     _ __   _ _____ _______
    |______ |______ |_____| | \  |   |      |
    ______| ______| |     | |  \_| __|__    |
    [{colourRed}By SysNit{colourMagenta}]   [{colourRed}Your Platform : {colourBlue}{platform.system()}{colourRed}]
'''
mainMenu = f''' {colourRed}
    [{colourBlue}1{colourRed}] {colourMagenta}Create a profile{colourRed}
    [{colourBlue}2{colourRed}] {colourMagenta}Delete a profile{colourRed}
    [{colourBlue}3{colourRed}] {colourMagenta}Connect To profile{colourRed}
    [{colourBlue}4{colourRed}] {colourMagenta}List Profiles{colourRed}
    [{colourBlue}5{colourRed}] {colourMagenta}Exit{colourRed}
'''
# -------------------------------------------- Global Variables --------------------------------------------
class sys:
    def clear():
        operatingSystem = platform.system()
        if operatingSystem == "Windows":
            os.system('cls')
        elif operatingSystem == "Darwin":
            os.system('clear')
        elif operatingSystem == "Linux":
            os.system('clear')
        else:
            os.system('clear')
    def invalid():
        sys.clear()
        print(logo)
        print(f'INVALID CHOICE {colourBlue}::{colourRed} INVALID CHOICE')
        time.sleep(1)
        main.menu()
    def exitSSHNit():
        sys.clear()
        print(logo)
        print(f'{colourMagenta} Adios Amigos')
        exit()
class profiles:
    def createProfile():
        if not os.path.exists('profiles'):
            os.makedirs('profiles')
        sys.clear()
        print(logo)
        print(f'{colourBlue}Create a profile')
        profileName = input("Profile Name~#: ")
        profilesFile = open(f'profiles/{profileName}.json', 'w')
        profileIPAddress = input("Profile IP~#: ")
        profileUser = input("Profile User~#: ")
        profilePassword = input("Profile Password~#: ")
        profileContent = '{"' + profileName + '": [{"IP":"' + profileIPAddress + '", "User":"' + profileUser + '", "Password":"' + profilePassword + '"}]}'
        # construct json profile
        profilesFile.write(profileContent)
        profilesFile.close()
        time.sleep(1)
        main.menu()
    def deleteProfile():
        if not os.path.exists('profiles'):
            os.makedirs('profiles')
        # profiles directory is not found, create it
        sys.clear()
        print(logo)
        print(f"{colourBlue}Delete a profile.")
        profileToDelete = input("Profile~#: ")
        try:
            os.remove(f'profiles/{profileToDelete}.json')
            print(f'{colourBlue}Profile {colourRed}{profileToDelete}{colourBlue} has been deleted {colourGreen}successfully{colourBlue}.')
            time.sleep(5)
            main.menu()
        except OSError as osError:
            print(f'{colourBlue} The was an error deleting profile {colourRed}{profileToDelete}{colourBlue}. Printing error...')
            print(osError)
            time.sleep(5)
            main.menu()
    def connectToProfile():
        sys.clear()
        print(logo)
        profileToConnect = input("Profile~#: ")
        with open(f'profiles/{profileToConnect}.json') as profileFile:
            data = json.load(profileFile)
            for p in data[profileToConnect]:
                print(f"{colourBlue}Your password is {colourGreen}{p['Password']}{colourBlue}")
                time.sleep(3)
                os.system(f"ssh -l {p['User']} {p['IP']}")
                time.sleep(2)
                main.menu()
    def listProfileData():
        if not os.path.exists('profiles'):
            os.makedirs('profiles')
        # profiles directory is not found, create it
        sys.clear()
        print(logo)
        print("Listing profiles..")
        profiles =  os.listdir('profiles')
        for file in profiles:
            file = os.path.splitext(file)[0]
            print(f'{colourBlue}{file}')
        time.sleep(2)
        main.menu()
class main:
    def menu():
        sys.clear()
        print(logo)
        print(mainMenu)
        mainMenuInput = input("SSHNit~#: ")
        if mainMenuInput == "1":
            profiles.createProfile()
        elif mainMenuInput == "2":
            profiles.deleteProfile()
        elif mainMenuInput == "3":
            profiles.connectToProfile()
        elif mainMenuInput == "4":
            profiles.listProfileData()
        elif mainMenuInput == "5":
            sys.exitSSHNit()
        else:
            sys.invalid()
main.menu()
