from sys import argv
import os
import requests
import sys

# Setting the projects path
DIRPATH = "C:/Users/Rishikesh Kanabar/Desktop/python_projects/"

# Getting the name of the repository
try:
    name = argv[1]
except:
    
    # Printing error and exiting if invalid command used
    print("Usage: gitrepo name\n")
    exit()

# Joining the repository name with the path
path = os.path.join(DIRPATH, name)

# Making the folder from the path
os.mkdir(path)

# Changing the current working directory to the target directory
os.chdir(path)

# Creating the readme.md file with echo
os.system(f'echo # {name.title()} >> README.md')

# Initialising a git local repository
print()
os.system('git init')

# Making the first commit
print()
os.system('git add README.md')
os.system('git commit -m "first commit"')

# Making a git branch
os.system('git branch -M main')

