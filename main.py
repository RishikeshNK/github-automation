from sys import argv
import os

# Setting the projects path
DIRPATH = "<path to folder>"

# Getting the name of the repository
try:
    name = argv[1]
except:
    
    # Printing error and exiting if invalid command used
    print("\nUsage: gitrepo name\n")
    exit()

# Joining the repository name with the path
path = os.path.join(DIRPATH, name)

# Making the folder from the path
os.mkdir(path)

# Changing the current working directory to the target directory
os.chdir(path)

# Creating the readme.md file with echo
os.system(f'echo # {name} >> README.md')

# Initialising a git local repository
print()
os.system('git init')
print()

# Creating a GitHub remote repository with gh CLI
os.system(f'gh repo create {name} --public --confirm')

# Making the first commit
print()
os.system('git add README.md')
os.system('git commit -m "first commit"')
print()

# Pushing changes to GitHub remote repository
os.system('git push origin master')
print()

# Opening project in VSCode - Remove if you dont use VSCode
os.system('code .')
