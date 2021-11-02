#/usr/bin/env python3

from colorama import Fore
import shutil
import os

def main(project):
    def generateProject():

        if project in os.listdir(f"./"):
            print(Fore.RED + "Error! This Directory is using!" + Fore.RESET)
            exit(1)
        else:
            pass

        os.system(f'mkdir ./{project}')
        os.system(f"touch ./{project}/main.cpp")
        os.system(f"touch ./{project}/Makefile")

        shutil.copyfile('./generation/for_generate_main.cpp', f'./{project}/main.cpp')
        shutil.copyfile('./generation/for_generate_makefile.Makefile', f'./{project}/Makefile')

        openInVscode(project)


    def openInVscode(project):
        print(Fore.LIGHTGREEN_EX + "Successfully generated!\n" + Fore.RESET)
        opening = input(Fore.LIGHTBLUE_EX + "If you want open your project in vscode or vim type: vscode/vim\nElse type: exit\n-> " + Fore.RESET)

        if opening == 'exit' or 'vscode' or 'vim':
            if opening == 'vscode':
                os.system(f"cd ./{project}/ && code .")
                exit(0)
            if opening == 'vim':
                os.system(f"cd ./{project}/ && vim main.cpp")
                exit(0)
        else:
            print(Fore.RED + "Error! Unknow command!")
            exit(1)


    if project != " " or "":
        generateProject()
    else:
        print(Fore.RED + "Project name can't be null!" + Fore.RESET)
        exit(1)


if __name__ == "__main__":
    project = input("Project name C++: ")
    
    main(project)
