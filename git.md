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
Command                                   | Description
----------------------------------------- | -----------------------------------
git config --global user.name "Mona Lisa" | set user name


## .gitignore
- add files, directories which should be ignored by git.
- edit file (with nano or similar) and commit to repository.


## References
- https://backlog.com/git-tutorial/en/stepup/stepup2_5.html
- https://git-scm.com/docs/git-merge
- https://www.atlassian.com/git/tutorials/using-branches/git-merge


-------------------------------------------------------------------------------
# Repository

## Create local repo
Command                       | Description
----------------------------- | -----------------------------------------------
change into to directory      | change to your existing project directory
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
git fetch             | get in sync with master repo (fetch all to local repo)
git checkout [branch] | switch to [branch]


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


## Switch branch
Command                       | Description
----------------------------- | -----------------------------------------------
git branch                    | show local branches
git checkout [branch]         | switch to [branch]


## Delete branch
Command                       | Description
----------------------------- | -----------------------------------------------
git checkout [other-branch]   | switch to another branch
branch -d [branch]            | delete with check and warnings (z.B. falls nicht auf master commited)
branch -D [branch]            | delete with no warnings


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