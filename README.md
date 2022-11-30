# Automate Your Daily System Operations

## Getting Started

To get started just clone the repo into your machine and get started..

<br>

1. Clone the project to have the file at your localhost.

```
git clone https://github.com/iNightjar/UniqueRock.git
cd UniqueRock
git checkout master
rm -rf .git
git init .
git add --all
git commit -m "Your Commit Message"
```

2. Open VSCode to edit scirpt if you like.

```bash
code .
```

The script might not work out of the box, some tweaks and a little bit of hacking is required as explained in Prerequisites

### Prerequisites

First to make the script executable from any directory, create a bin directory in your /home folder.

```
~$ mkdir bin
```

Place the scripts you like in the */home/USER/bin* folder and then add the path to it in the .bashrc file
Add this line as the end of your .bashrc file **export PATH=$PATH:/home/USER/bin/** USER being the logged in user

Create a .bash_aliases file if you dont have one and add this line
**alias [type what you want]=[bash file choosen]**.

So as to prevent logging out and in again so as to load the changes done to the *.bashrc* run this command from you home directory

```
~$ source ~/.bashrc
```

Once that is done you are ready to go.

### User Management

### Create New User Script
![new users creation](https://raw.githubusercontent.com/iNightjar/UniqueRock/FristDocumenting/userCreationScript.mp4)

### System Logs

### Show Users Logs, You can select which day too.
![Users Logged to sytem](https://raw.githubusercontent.com/iNightjar/UniqueRock/FristDocumenting/usersLogs.mp4)