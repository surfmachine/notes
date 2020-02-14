GIT
===============================================================================

[TOC]

-------------------------------------------------------------------------------
# General

## Big Picture

**Locations**
- localhost 
  - local
  - master or branch
- remote master or branch


**Actions**

Command           | Description
----------------- | --------------------------------------------------------- 
fetch             | get data from remote to master@localhost
merge             | merge data from mater@localhost to local@localhost
pull              | fetch & merge 
rebase            | merge data to local and then put local changes on top
commit            | commit local changes to master@localhost
push              | push commited data from master to remote origin master
gitk              | gui repository browser
git-gui           | gui commits 
help              | help
help -a           | help all
help -p           | help concepts



**Development cycles**
- fetch, merge, rebase, commit, push (bei push NIE -force verwenden)
- pull --rebase (identisch mit fetch, rebase)



## Status and log
Command                       | Description
----------------------------- | -----------------------------------------------
git status                    | show status
git log                       | show commit log
git log --pretty=short        | show commit log short
git shortlog                  | show commit log very short (only comments)


## Configuration
Command                                     | Description
------------------------------------------- | ---------------------------------
git config --global user.name  [USERNAME]   | set user name, for example $USER
git config --global user.email [EMAIL]      | set password
git config --global color.ui auto           | set colors
git config --global http.sslVerify false    | disable ssl verification
git config --global push.default current    | use current as default for push 
git config --global credential.helper cache | cache password for 15 min
git config --local credential.helper ""     | remove user credential details from repo
git remote -v                               | remote repo list existing url's
git remote add origin [URL]                 | remote repo add new url


## Credentials

**SSH approach**
See https://unix.stackexchange.com/questions/335704/how-to-set-up-username-and-passwords-for-different-git-repos


**Using gitcredentials**
If the SSH approach doesn't apply (e.g. you're using a repository accessed over HTTPS), git does have its own way of handling credentials, using gitcredentials (and typically git-credential-store). 

You specify your username using:
> git config credential.${remote}.username yourusername

and the credential helper using:
> git config credential.helper store

Note: 
> specify **--global** if you want to use this setup everywhere

Then the first time you access a repository, git will ask for your password, and it will be stored (by default in ~/.git-credentials). Subsequent accesses to the repository will use the stored password instead of asking you.

## .gitignore
- add files, directories which should be ignored by git.
- edit file (with nano or similar) and commit to repository.


## References
- https://backlog.com/git-tutorial/en/stepup/stepup2_5.html
- https://git-scm.com/docs/git-merge
- https://www.atlassian.com/git/tutorials/using-branches/git-merge
- https://unix.stackexchange.com/questions/335704/how-to-set-up-username-and-passwords-for-different-git-repos


-------------------------------------------------------------------------------
# Repository

## Clone
Command                       | Description
----------------------------- | -----------------------------------------------
git clone [repo-url]          | clone remote repo to local disk 
git clone [repo-url] [dir]    | clone remote repo to local disk into specific folder


## Create local repo
Command                       | Description
----------------------------- | -----------------------------------------------
change into directory         | change to your existing project directory
git init                      | init git
git add .                     | add current directory
git commit -m "Inital commit."| commit your changs to the local repository


## Create remote repo
Command                       | Description
----------------------------- | -----------------------------------------------
git remote add origin [adr]   | Grab its repo address [adr]
git push -u origin master     | Push local repo to the remote [adr] ^1^

_^1^ Sample repo address: https://github.com/<my-org>/my-proj.git_


## Checkout from remote repo
Command               | Description
--------------------- | -----------------------------------------------
git checkout -b [branch] origin/[branch] | git checkout remote branch
git fetch             | get in sync with master repo (fetch all to local repo)
git checkout [branch] | switch to [branch]


## Pull, fetch from remote repo
Command                       | Description
----------------------------- | -----------------------------------------------
pull                          | get remote changes to local repo
pull origin master            | get all remote changes to local repo
fetch origin master           | fetch remote changes of master to local master
clean -x -d -f                | clean local repo to initial state
reset --hard origin/master    | reset local repo and fetch latest changes from remote master to local master


## Staging, commit and push
Command                       | Description
----------------------------- | -----------------------------------------------
git add [file-name]           | add file to staging area
git add .                     | add all to staging area
git commmit -m "[message]"    | commit staged files with commit message
git commit -a                 | commit all changend and all added files
git push                      | push all commmits to remote repo
git push -u [remote-branch]   | set remote branch to current local branch
git push origin master        | send commits to remote master branch
git push origin [branch-name] | send commits to remote branch 
git push --all origin         | send all branches to remote repo


-------------------------------------------------------------------------------
# Branch

## Show branches
Command                       | Description
----------------------------- | -----------------------------------------------
git branch                    | show local branches
git branch -r                 | show remote branches
git branch -a                 | show all branches




## Create new branch
Command                           | Description
--------------------------------- | --------------------------------------------
git checkout [branch]             | switch branch
git checkout -b [new-branch]      | create new branch based of the current branch
git push --set-upstream origin [branch] | push local branch to remote (first time)
git push                          | push changes to remote (ab dem 2ten mal)


## Create new branch from a tag
Command                       | Description
----------------------------- | -----------------------------------------------
git fetch                     | fetch source from remote repository
git fetch --tags              | fetch tags from remote repository
git checkout tags/[tag] -b [new-branch] | create new branch based on the given [tag]


## Reset local commits to origin 
Command                          | Description
-------------------------------- | -----------------------------------------------
git reset --hard origin/[branch] | replace local branch with remote branch entirely


## Switch branch
Command                       | Description
----------------------------- | -----------------------------------------------
git branch                    | show local branches
git checkout [branch]         | switch to [branch]


## Delete branch
Command                           | Description
--------------------------------- | -------------------------------------------
git checkout [other-branch]       | switch to another branch
git branch -d [branch]            | delete local branch with check and warnings
git branch -D [branch]            | delete local branch with no warnings
git push origin --delete [branch] | delete remote branch


-------------------------------------------------------------------------------
# Tag

## Show tags
Command                       | Description
----------------------------- | -----------------------------------------------
git tag                       | show tags
git tag -l '2.5*'             | show tags starting with 2.5
git show 2.5.6                | show details from tag 2.5.6
git ls-remote --tags          | show remote tags


## Create tag
Command                       | Description
----------------------------- | -----------------------------------------------
git tag [tag]                 | create new tag with the given name [tag]
git tag -a 2.6.0 -m 'new tag' | create new tag 2.6.0 with comment
git tag [tag] [commit-nr]     | create new tag at the given commit-nr (see history)
git push origin [tag]         | push tag to remote repository / server


## Checkout tag
Command                       | Description
----------------------------- | -----------------------------------------------
git fetch                     | fetch source from remote repository
git fetch --tags              | fetch tags from remote repository
git checkout [tag]            | checkout tag
git checkout tags/[tag]       | checkout tag


-------------------------------------------------------------------------------
# Merge


## Merge from branch with override

> Merge all changes from develop to stable (and override stable if needed)
git checkout stable
git merge -Xtheirs develop

## Merge from a tag

Sample: merge Tag 2.5.6 to the master branch:
> develop ---- 2.5.5 --- 2.5.6 --- 2.6.0 ----------
> master  -----2.4.1 ---


Command                       | Description
----------------------------- | -----------------------------------------------
git checkout master           | checkout branch you want to merge to
git merge -X theirs 2.5.6_rel | merge from tag 2.5.6_rel and override changes of master, in case of a merge conflict (1)

_(1) Details see: https://git-scm.com/docs/git-merge_


-------------------------------------------------------------------------------
# Stash

Command                       | Description
----------------------------- | -----------------------------------------------
git stash         | stash the changes in a dirty working directory away
git stash show    | show "stashed" changes
git stash apply   | move changes back to working directory



-------------------------------------------------------------------------------
# Samples

## Reset master to specific git commmit id
git log
git reset --hard [git-commit-id]
git --force push


## Merge mit vorherigem rebase
git checkout master
git pull
git checkout story-150-model-changes
git branch
git rebase master                   // merge fehler beheben
git rebase --continue
git push --force                    // jetzt wird der branch wieder hochgeladen
                                    // force wird benötigt,  da rebase gemacht wurde
git checkout master
git merge --no-ff story-150-model-changes
git status
git push

git push origin --delete story-150-model-changes   // delete branch remote (zuerst machen wegen auto-completion)
git branch -d story-150-model-changes              // delete branch local


## Delete Branch (remote and local)
git push origin --delete <branch_name>
git branch -d <branch_name>


## Rebase mit Master, Merge branch to master, delete branch remote and Logical
git checkout story-200-import-export
git branch
git push
git branch
git checkout master
git pull
git checkout story-199-part-a-draw-edge
git rebase master
git checkout master
git merge --no-ff story-199-part-a-draw-edge
git branch
git push origin --delete story-199-part-a-draw-edge
git branch -d story-199-part-a-draw-edge
git branch
git push
git pull --rebase
git push
git status


## GIT Backup

### Init remote repository as backup store
Create remote repository for storing the backup data:
```
mkdir /[BACKUP-SHARE]/[BACKUP-DIR].git
cd /[BACKUP-SHARE]/[BACKUP-DIR].git
git init --bare
```

### Init local repository with data for the backup
1. Init local repo
   ```
   cd [BACKUP-SHARE]
   git init
   ```

2. Create ignore file for and add rules for data not going to the backup  
   ```
   touch .gitignore
   nano .gitignore
   git status
   ```

3. Check what data will be in the backup
   ```
   git status
   ```

4. Create first commit 
   ```
   git add .
   git commit -m 'initial backup'
   ```

5. Create first push
   ```
   git remote add origin file:///[BACKUP-SHARE]/[BACKUP-DIR].git
   git push
   ```

### Create backup script
Create [BACKUP-SCRIPT].sh with the following content:
```
#!/bin/bash
cd [BACKUP-SHARE]
git add .
git commit -m'automatic backup'
git push
```

### Define crone job

For example every working day (1-5) at 4pm:
```
crontab -e
0 16 * * 1-5 [BACKUP-SCRIPT].sh
```

For example every wednesday at 4am:
```
crontab -e
0 4 * * 3 [BACKUP-SCRIPT].sh
```

**Cronjob syntax**
```
# Use the hash sign to prefix a comment
# +---------------- minute (0 - 59)
# |  +------------- hour (0 - 23)
# |  |  +---------- day of month (1 - 31)
# |  |  |  +------- month (1 - 12)
# |  |  |  |  +---- day of week (0 - 7) (Sunday=0 or 7)
# |  |  |  |  |
# *  *  *  *  *  command to be executed
```

-------------------------------------------------------------------------------
_The end._

