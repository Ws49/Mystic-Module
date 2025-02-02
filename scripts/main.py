import os
print( r"      ___                       ___                                   ___           ___     ")
print(r"     /__/\          ___        /  /\          ___       ___          /  /\         /  /\    ")
print(r"    |  |::\        /__/|      /  /:/_        /  /\     /  /\        /  /:/        /  /:/_   ")
print(r"    |  |:|:\      |  |:|     /  /:/ /\      /  /:/    /  /:/       /  /:/        /  /:/ /\  ")
print(r"  __|__|:|\:\     |  |:|    /  /:/ /::\    /  /:/    /__/::\      /  /:/  ___   /  /:/ /::\ ")
print(str(r" /__/::::| \:\  __|__|:|   /__/:/ /:/\:\  /  /::\    \__\/\:\__  /__/:/  /  /\ /__/:/ /:/\:\""))
print(r" \  \:\~~\__\/ /__/::::\   \  \:\/:/~/:/ /__/:/\:\      \  \:\/\ \  \:\ /  /:/ \  \:\/:/~/:/")
print(r"  \  \:\          ~\~~\:\   \  \::/ /:/  \__\/  \:\      \__\::/  \  \:\  /:/   \  \::/ /:/ ")
print(r"   \  \:\           \  \:\   \__\/ /:/        \  \:\     /__/:/    \  \:\/:/     \__\/ /:/  ")
print(r"    \  \:\           \__\/     /__/:/          \__\/     \__\/      \  \::/        /__/:/   ")
print(r"     \__\/                     \__\/                                 \__\/         \__\/  ")
print(r"                                                                                        by Mystics  ")

option = ""
while option != "exit":
    if "use" in option:
        if option.split(' ')[1] == "Reverse":
            os.system('start cmd /k "python Reverse/reverse_nexus.py"')
        elif option.split(' ')[1] == "Octopyter":
            os.system('start cmd /k "python CrackerZIP/Octopyter.py"')
        elif option.split(' ')[1] == "Fenix":
            os.system('start cmd /k "python KeyLogger/Fenix.py"')
    option = input("MYSTICS>")