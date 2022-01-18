# Git Guide  
  
## Command Line Git  
  
status  
Shows status of the local repo. This status includes:  
-number of local commits that have not been synced with remote (GitHub)  
-list of files in local folde rthat are NOT being tracked by git  
-list of files in the local folder that have changes that need to be committed  
Use with $ git status  
    
clone  
Creates a copy of an existing Git repository onto your local system  
Use with $ git clone [desired git url]  
  
add  
Adds file contents to be tracked by git  
Use with $ git add [filename]  
  
rm   
Removes things such as files and directories from your filesystem  
Use with $ rm [filename]  
  
commit  
Executes the changes you’ve made to files. Updates a changelog with messages about what you’ve changed  
Use with $ git commit -m “your message here”  
  
push  
Sends your commits to remote (GitHub) and syncs it  
Use with $ git push  
  
fetch  
Downloads contents from your remote repository  
Use with $ git fetch [url or argument]  
  
merge  
Pulls forked branches back together into a single branch  
Use with $ git merge [branchName]  
  
pull  
Gets content from the remote repository and merges it into your local repo copy  
Use with $ git pull  
  
branch  
Creates a new section in your repository for separated storage  
Use with $ git branch [newBranchName]  
  
checkout  
Lets you switch between branches in the repo  
Use with $ git checkout [branchName]  
  
  
##git Files and Folders  
  
.git folder  
Contains all info necessary for projects (all info related to commits, remote repo’s address, and more)  
-hooks: contains script files. Git hooks are the scripts that get executed before commits, push, and so on  
-Objects: an object database of Git   
-config: the local configuration file  
-refs: stores info about tags and branches  
-HEAD: Stores reference to the current branch; points to master by default  
-index: A binary file that stores staging info  
  
.gitignore folder  
The file that holds a list of files and directories you want to ignore  
-git status won’t show these as files to be added  
-Use to keep excess and secrets off github and to exclude libraries that need to be built per person  
  
  
##GitHub  
  
Pull Requests  
Lets you document the changes you’ve pushed to a branch on the repo. You can discuss and review changes before merging them to the branch  
  
SSH Authentication to Repositories  
Connecting GitHub using SSH provides a secure channel over an unsecured network. An SSH key is a way to identify yourself that doesn’t require you to identify yourself with your username and password every time  

