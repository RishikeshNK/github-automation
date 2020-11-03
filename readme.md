# Github Repo Creation Automation with Python3

## By: Rishikesh NK

### Automated Functioning :-

#### After entering the command ```gitrepo {name}``` the script :-

1. Creates a new folder with the argument name ```mkdir {name}```
2. Creates a README markdown file with the argument name as the heading ```echo # {name} >> README.md```
3. Initializes a Git Local Repository ```git init```
4. Creates a GitHub Remote Repository with gh-cli ```gh repo create {name} --public --confirm```
5. Adds the README markdown file and makes the first commit ```git add README.md```
```git commit -m "first commit"```
6. Pushes the changes to the Remote Repository ```git push origin master```
7. Opens the project in Visual Studio Code ```code .```

### Usage :-

`gitrepo {name}`

- Note: ```{name}``` is the name of the repository you want to create.

- Or `python main.py name` if gitrepo is not set as a valid MACROS in _doskey_

### Installation and Setup :-

1. Install GitHub CLI (gh) by going to [https://cli.github.com/](https://cli.github.com/)
2. Type `gh auth login` in CMD and follow the instructions on-screen to complete authorisation of gh
3. Clone this repository by typing `gh repo clone RishikeshNK/github-automation` into CMD
4. Change directory to the cloned repository after download by typing `cd github-automation`
5. Open `main.py` in a text editor or IDE. If you use Visual Studio Code then type `code .` to open the current repository in a new VSCode Window
6. Replace `<path to folder>` on Line 5 to the path of the desired folder to story the automatically created repositories. In my case it is `C:/Desktop/python_projects/`
7. Ensure that you have Git CLI installed. If not then head onto [https://git-scm.com/downloads](https://git-scm.com/downloads) and complete the installation
8. The program is meant to work with Visual Studio Code but if you do not use Visual Studio Code then remove Line 47 of the `main.py` -
   `os.system('code .')`
9. To temporarily try out the gitrepo alias, open `doskey.txt` and replace `<file path>` to the path of the `main.py` file. For example - `C:\Desktop\github-automation\main.py` in my case. So the command should look like
   `doskey gitrepo=python "C:\Desktop\github-automation\main.py" $*` (in my case)
10. Copy the command you created in `doskey.txt` file and paste it into CMD
11. To check if all steps are followed correctly, type `gitrepo test`. This will create a local repository in the folder you mentioned in Step 6 and a remote repository on your GitHub Account. It will also open a project in VSCode if you haven't deleted that line of code in Step 8

#### Optional - (Source - [https://superuser.com/a/1294155](https://superuser.com/a/1294155))

12. Open a new command prompt and type `cd C:\` to go to the C:\ drive
13. Create a directory called bat by typing ```mkdir bat```
14. Copy the ```macros.doskey``` file from the cloned repository to newly created ```C:\bat\```
15. Open the ```macros.doskey``` file in a text editor and replace the ```<path to main.py file>``` with the path of the ```main.py``` file in the cloned repository. For example, the command should look like ```gitrepo=python "C:\Desktop\github-automation\main.py" $*```
16. Save the file by ```CTRL+S```
17. Go to **Registry Editor** from the search box
18. Go to ```HKEY_LOCAL_MACHINE\Software\Microsoft\Command Processor\```
19. Right-click and add a new "String Value" sub-key. Name it ```Autorun```. 

      **Right-click -> New -> String Value**
20. Right-click it and click Modify the Value data.

      **Right-click -> Modify -> Value data -> ```DOSKEY /MACROFILE="C:\bat\macros.doskey"```**
21. Close the Registry Editor

**This will allow the DOSKEY command to be permanent**
