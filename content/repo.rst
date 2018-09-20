Setting up a Git Repository
###################################

:date: 2018-09-19 01:24
:modified: 2018-09-19 01:25
:tags: linux
:category: Linux
:slug: repo
:authors: Adrian Karcevski
:summary: How to do ___ in Bash.

.. code-block:: bash

   $ git --version
   # git version 2.7.4

   $ git config --list
   $ git config --help
   
   # on local-repo
   $ git init
   # to start tracking

   # on remote-repo
   git clone

   # remove .git to stop tracking
   $ rm .git

   $ git status

   $ touch .gitignore
   # add files to be ignored

   $ git add -A
   # add all files sub .gitignore
   $ get add .gitignore

   $ get reset
   # remove everything from the staging area

   $ git clone <source> <destination>
   $ get clone ../remote_repo.git .
   $ get clone https://github.com/adriankarcevski/remote_repo.git .

   # Follow these steps after creating changes.
   
   # check the changes made
   $ get diff

   # stage the changes for commit
   $ git status
   $ git add -A 
   
   # commit changes
   $ git commit -m "Modified multiply function"

   # then; if working with others
   $ git pull origin master
   $ git push origin master
