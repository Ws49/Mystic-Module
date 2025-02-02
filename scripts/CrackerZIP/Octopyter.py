import pyzipper
import os
from itertools import product

class colors_text:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def apresentation():
    print(colors_text.OKCYAN +"                                                    MM                                              ")
    print("                                                  MM@@##                                            ")
    print("                                            MMMM##MMMMMM@@@@MM                                      ")
    print("                                            @@MMMMMMMMMMMMMM@@                                      ")
    print("                                            MMMMMMMMMMMMMMMM@@                    @@@@              ")
    print("                                          MMMMMMMMMMMMMMMMMMMM##                @@    ##            ")
    print("                                          MMMMMMMMMMMMMMMMMM@@MM                ##      MM          ")
    print("              MM##@@                    @@MM@@MM@@@@@@@@@@@@@@MM                        ##          ")
    print("            ####  ##                      @@@@@@MM@@@@@@@@@@@@@@                        @@          ")
    print("            @@    @@                      @@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@##          ##          ")
    print("            ##              @@@@@@        ##@@@@@@@@@@@@@@##@@    @@@@@@####@@@@      @@##          ")
    print("            @@            @@@@@@@@@@        @@@@@@@@@@@@@@@@##    @@##@@##@@####@@@@####            ")
    print("            ##          @@##@@##@@@@@@      @@@@@@@@@@@@@@@@      @@@@##      ######                ")
    print("          ######@@##  @@##MM########@@##    ##MM@@##@@@@####  ####@@##mm    ##@@@@@@########        ")
    print("        ####    @@mm@@####      ####@@@@########@@@@@@@@@@######@@@@@@##  @@@@@@@@@@@@    ####      ")
    print("                    ####@@@@##########@@@@##########@@@@########@@@@@@##@@########::@@@@      ##    ")
    print("      ##            @@@@@@@@@@@@@@@@@@@@@@##@@####@@@@@@@@@@##@@@@@@##@@##@@##########@@      ##    ")
    print("      ##          @@@@##--##@@@@@@@@@@@@##@@@@@@@@@@@@@@@@##@@##@@@@@@################@@            ")
    print("      ##    ##    @@@@@@########MM@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@######@@##########@@@@      ##    ")
    print("        ######    @@##########  @@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@####MM@@######  ####@@    ####      ")
    print("                  @@@@@@        ##@@##@@@@@@@@@@@@@@@@@@##@@@@@@@@@@########  ##@@                   ")
    print("                    @@################@@@@@@@@##@@@@@@@@##@@##@@##@@@@##########                     ")
    print("                      ##@@############@@@@##@@@@@@@@@@@@##@@##@@MM##@@##########      ##            ")
    print("                          ############@@############@@##    ####################                     ")
    print("                          ######    ####@@@@  ############        ########  ##########               ")
    print("                ####        ####    ########  ##############      ######    ####        ####         ")
    print("              ##      ##  @@####      ##############@@########    ####      ####            ##       ")
    print("        ##    ##          ######        ##############################      ####            ##       ")
    print("                          ####                ######################        ######        ##         ")
    print("                        ######                ##@@############  ####          ######    ##           ")
    print("        MM      ..########@@                  ####  ##@@####      ####    mm########++            ## ")
    print("        ##                  ##                ##@@  @@####        ########                  ##       ")
    print("    ::                mm##::MM    ##          ##    ######  ########    ##..  ..++                    ")
    print("                      ##..##        ####  ####    ######  ##      ####    ######                      ")
    print("        ::--      MM      ##                      ######    ##      ##    ##      MM        ::       ")
    print("            @@                    ..--@@######################@@--..                    MM           ")
    print('\n\n\n')
    print("          _______ _______________________ _______        ________________ _______ ")
    print("         (  ___  |  ____ \__   __(  ___  |  ____ )\     /\__   __(  ____ (  ____ )")
    print("         | (   ) | (    \/  ) (  | (   ) | (    )( \   / )  ) (  | (    \/ (    )|")
    print("         | |   | | |        | |  | |   | | (____)|\ (_) /   | |  | (__   | (____)|")
    print("         | |   | | |        | |  | |   | |  _____) \   /    | |  |  __)  |     __)")
    print("         | |   | | |        | |  | |   | | (        ) (     | |  | (     | (\ (   ")
    print("         | (___) | (____/\  | |  | (___) | )        | |     | |  | (____/\ ) \ \__")
    print("         (_______|_______/  )_(  (_______)/         \_/     )_(  (_______//   \__/")
    print('\n\n\n')
                                                                        
def decryption_wordlist(wordlist,file):
    list_pass = []
    
    with open(str(wordlist),'r') as file_pass: 
        list_pass = file_pass.readlines()

    try :
        with open(str(wordlist),'r') as file_pass:
            list_pass = file_pass.readlines()
        file = pyzipper.AESZipFile(str(file),'r')
        for password in list_pass:
            try:
                if not os.path.exists('UnlockedZIP'):
                    os.mkdir('UnlockedZIP')
                os.chdir('UnlockedZIP')
                file.extractall(pwd=(password.strip()).encode())
                os.chdir('..')
                print(os.getcwd())
                print("PASSWORD IS --> " + password.strip())
            except:
                continue
            
    except Exception as e:
        if 'Bad password for file' in str(e):
           print("Not possible unlocked because : password not present in wordList")
        else:
            print("Noot possible unlocked because : " + str(e))
        
def decryption_bruteforce(file,max_lenght_password):
    pass

        
        
if __name__ == '__main__':
    os.system('cls')
    apresentation()
    option = ''
    
    while option != 'exit':
        option = input('OCTOPYTER> ')
        
        if '-dW' in option:
            decryption_wordlist(option.split(' ')[1],option.split(' ')[2])
        elif option == '-dB':
            decryption_bruteforce("",2)
        else:
            print('-dW  wordlist  file (for decryption with wordlist)')
            print('-dB file  maxLentgh (for decryption with bruteforce)')
    
