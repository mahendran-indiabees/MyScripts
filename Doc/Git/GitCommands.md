#### What is Version Control System (VCS)
* VCS is a software tool that helps you manage changes to source code over time
* It helps the developer team to efficiently communicate and manage(track) all the changes that have been made to the source code along with the information like who made and what changes have been made
* VCS is also known as Source Control Management (SCM)

  
#### Types of VCS
* Localized Version Control System
* Centralized Version Control System (CVCS)
* Distributed Version Control System (DVCS)

#### Localized Version Control System
You can track the version of all the files only within your local system. There is no remote server in this scenario. All the changes are recorded in a local database 
**Example: Revision Control System**

![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/8433926c-8b80-4407-8c83-28444ae289d0)


#### Centralized Version Control System (CVCS)
Central repo shared with all the developers, and everyone gets their own working copy. Whenever you commit, the changes get reflected directly in the Central repo.
**Example: Subversion (SVN)**

![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/5d801c18-68d6-4a04-9427-8561e8c82f37)


#### Distributed Version Control System (DVCS)
In distributed systems, there is a local copy of the repo for every developer on their computers. They can make whatever changes they want and commit without affecting the remote repo. They first commit in their local repo and then push the changes to the remote repo. This is the type used majorly today. 
**Example: Git**

![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/a7a6d718-8907-424a-915c-bac65f81cc29)

#### What is Git
Git is a distributed, open-source version control system (VCS) that enables you to store code, track revision history, merge code changes, and revert to earlier code version when needed.

#### Git Architecture
![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/9949f1fe-7fd2-4c89-b601-2932d4f0ccfa)



## Git Commands

#### git config
The git config command is used to configure Git settings like username and email. Below commands helps you to set username and email
```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

```

#### Git init
To initilize empty git repository
```
git init <directory>
```
To initilize empty git repository in current directory / folder
```
git init
```

#### Git add
To initilize empty git repository
```
git init <directory>
```
To initilize empty git repository in current directory / folder
```
git init
```
