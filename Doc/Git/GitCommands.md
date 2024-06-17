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
#### git status
The git status command is used to display the state of the working directory and the staging area. This command provide information about which branch you're in, Changed files info, What are the files you have to add in Staging Area.
```
git status
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

#### git fetch
git fetch commands are used to sync your local repository with a remote repository. It retrieves commits, files, and references (branches, tags, etc.) from a remote repository into your local repository, but it does not automatically merge or modify your working directory. (In simple words, git fetch will pull latest changes from remote and update into local repo without affecting working directory)
```
git fetch
```

#### git pull
git pull commands also used to sync your local repository with a remote repository. It retrieves commits, files, and references (branches, tags, etc.) from a remote repository into your local repository. 
Note: Also, It will update / modfify remote changes into your working directory.(In Simple words, git pull command is combination of git fetch and git merge)

```
git pull
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


#### git merge
git merge is used to merge or integrate the changes from one branch into another barnch (or) git merge is a way of combining changes from one branch (source branch) into another branch (target branch).

The git merge command takes the contents of a source branch and integrates it with the target branch. It preserves the history of both branches by creating a new merge commit.

![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/8590cba7-186f-4393-abde-08d99f14ad8e)


```
git checkout <targetBranch>

git merge <sourceBranch>
(or)
git merge <sourceBranch> -m "Your commit messages"

git push
```

#### git rebase
The git rebase command integrates changes from one branch into another by moving or combining a sequence of commits to a new base commit. It rewrites the commit history.

![image](https://github.com/mahendran-indiabees/MyScripts/assets/96326288/349d886d-4418-4dd3-85b2-0b9c2099c0a4)


```
git checkout <targetBranch>

git rebase <sourceBranch>
```

#### git tag
Git tags are used to mark specific points in a repository’s history as important. Typically, they are used to mark release points (e.g., v1.0, v2.0). It is typically used to label important commit id or milestones or releases, such as a version, release or a major project update 

```
git tag -a <tagName> -m "Tag custom messges"
```

#### git stash
The git stash command is used to temporarily save changes in your working directory that are not yet ready to be committed. This allows you to switch branches or perform other tasks without having to commit unfinished work. When you're ready to continue working on those changes, you can retrieve them from the stash.

To Stash your current changes, You can below command
```
git stash
```

To list all the stashes
```
git stash list
```

To retrive / restore temporarily Saved changes into Working directory, Run below command
```
git stash pop
```
```
git stash pop <Index>
```


#### git branch
To List all branches (both Local & remote)
```
git branch -a
```

To List all remote branches
```
git branch -r
```

To Create a new branch, Run below command. This command will create a new branch from currently your checked out branch
```
git branch <branch Name>
```


#### git checkout/switch
git checkout/switch helps to switch the branches.
```
git switch <branchName>
```
(or)
```
git checkout <branchName>
```


To create a new branch from currently your checked out branch and switch to newly created branch, run below command
```
git checkout -b <branchName>
```


#### git Clone
git clone commands helps to checkout/clone/download remote repository into local repo
```
git clone <git remote Url>
```

#### git log
git log commands helps to display the log of commit history
```
git log
```

To display log commit history in short form, Run below commit
```
git log --oneline
```

#### Ignore file
The .gitignore file is used to tell Git which files (or patterns of files) it should ignore. This is useful for preventing certain files from being tracked and included in version control, such as temporary files, build artifacts, and sensitive information.


* Create the .gitignore File:
  ```
  touch .gitignore
  ```
  
* Add the file Name or Patterns to the .gitignore File which you want to ignore in version control: (Example below)
  ```
  *.log
tmp/
*.tmp
node_modules/
.env
.DS_Store
/build
/dist
.idea/
coverage/

  ```

* Commit the .gitignore File and push to remote
```
git add .gitignore
git commit -m "Add .gitignore file"
```
