# What is Version Control?
Version Control is a system that records changes to a file or set of files over time so that you can recall specific versions later.

# Why use Version Control?

* **Storing and restoring previous versions **: You can jump to any moment in time. short-term undo and long-term undo.
* **Understanding what happened**: It helps you understand how your project evolved between versions.
* **Collaboration**: Lets people share files and stay up-to-date with latest versions.
* **Backup**: As long as you commit your work will always be saved.

# Basic day to day operations

1. **Add**: (git add filename)-Add one or more files to staging or (git add *) -Add all files to staging

2. **Commit**:(git commit -m "Commit message")-Commit changes to head, but not yet to the remote repo

3. **Status**:(git status)-List the files you have changed and those you still need to add or commit

4. **Branches**:
    * (git branch)-List all the branches in your repo, and also tell you what branch you are currently in
    * (git branch dev)-Creates a development branch, this is the branch that you will use for all the project commits, then later merge with the master branch
    * (git checkout branchname)-Switch from one branch to another
    * (git merge branchname)-Merge a different branch into your active branch
    
# Keep Calm and Commit ;)
