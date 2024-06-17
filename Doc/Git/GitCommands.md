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

#### git init
To initilize empty git repository
```
git init <directory>
```
To initilize empty git repository in current directory / folder
```
git init
```

#### git add
git add helps to add your files to Staging Area (Note: We need to add modified/added files to Staging Area before run "git commit" command. If you not staged, files will not be commited when you run "git commit" command)

To add specific file to Staging Area
```
git add <fileName>
```

To add all modfiled/added files in current directory to Staging Area 
```
git add .
```
#### git commit
git commit command will commit your staged files to local repository.

Below command will commit your changes to local repository with your custom commit messages
```
git commit -m "Your Commit messages"
```

If you want to overwrite previous/recent commit messages / history in local repository (Note: Not Pushed to remote), Run below command
```
git commit --amend -m "Your New Commit messages"
```

#### git push
git push command will push your local repo changes to Remote Server

Below command will push commits from your local repository to a remote repository.
```
git push -u origin <Your Branch Name>
```

When you use below "git push" command, it pushes your changes to the specified remote and branch. If you don't specify a remote or branch, Git will use the default remote (usually origin) and the currently checked-out branch
```
git push
```

#### git diff
git diff commands helps to compare the difference between the files, commits, Branches, etc. It compares the changes made in the working directory, staging area, or between commits

To check changes between your changed files in working directory and Staging area
```
git diff
```

To check changes between Staged files (i.e., changes that are staged but not yet committed)and last commit (or) HEAD (or) Recently pushed changes
```
git diff --staged
```

To check difference/changes betweeen two commit ids
```
git diff <commitID1> <commitID2>
```

To check difference/changes betweeen your working directory and specified branch
```
git diff <your branchName>
```

To check difference/changes betweeen two branches
```
git diff <BranchName1>..<BranchName2>
```

#### git reset
The git reset command is used to reset / undo the changes. Using this commands, we can reset the changes to specific commit.

You have committed the changes in local repository and you want to reset the changes to specific  commit or previous commit. You have to run below command. This command will reset to your specific commit id. (Note: '--soft' : Changes will be discarded in your local repo / commit history. But still your changes available in Staging Area & working directory)
```
git reset <Previous or Specific commit ID> --soft
```

If you want to reset the changes in Local repo as well as Staging Area. Run below command. (Note: '--mixed' : Changes will be discarded in your local repo / commit history as well as Staging Area. But still changes available in Working directory "--mixed" will taken as default if you don't specify any arguments)
```
git reset <Previous or Specific commit ID> --mixed
```
(or)
```
git reset <Previous or Specific commit ID>
```

If you want to reset the changes in Local repo, Staging Area as well as working directory. Run below command. (Note: '--hard' : Changes will be discarded in your local repo / commit history, Staging Area as well as working directory
```
git reset <Previous or Specific commit ID> --hard
```

We can also reset the changes which you already pushed to Remote repo. We can use same commands for reset the chages. But Additionally we need to use git push command to push our changes to Remote
```
git reset <Previous or Specific commit ID> --[hard/soft/mixed]
git push -f origin <branchName>
```

#### git revert
git revert command is used to revert / rollback / undo the changes for specific commit. git revert command preserves the history by adding a new commit.

If you want to revert the changes for specific commit.
```
git revert <commit ID>
```

If you want to revert the changes for multiple commit.
```
git revert <commit ID1> <commit ID2> <commit ID3>
```

If you want to revert the changes for specific commit range.
```
git revert <My First bad commit ID>..<My Last bad commit ID>
```
