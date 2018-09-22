Hosting a static site using Pelican and Git
#####################################################
:date: 2018-09-22 16:38
:category: Projects
:tags: python, pelican, github, git
:authors: Adrian Karcevski

In my search to find a fast and cheap method for creating this blog, I stumbled upon `Pelican <https://blog.getpelican.com/>`_, a static site generator written in Python. I'll be showing you how to configure Pelican in conjunction with `Github Pages <https://pages.github.com/>`_ to host your webpage.

You will need a Github account, a basic understanding of Git, and should be familiar with creating Python virtual environments.

Pelican will generate .html files to be served by Github Pages. In order to do this we'll need one location for storing our "source" files and another location for our output files i.e. the actual webpage. We will be using two seperate branches within one repository to make this happen.

First create the repository where our project will live.

.. image:: /images/create-repo.png

Next clone the repository to create a new directory.

.. code-block:: bash

   $ git clone https://github.com/<your_name>/<your_name>.github.io.git

Change to the new directory.

.. code-block:: bash

   $ cd <your_name>.github.io

As mentioned above we will need a place to store our "source" files i.e. configuration files, Makefile, virtual environment, and content folder. We will do this by creating a new branch.

.. code-block:: bash 

   $ git checkout -b source



Now create the virtual environment and activate it. If you're using Python3, Pelican requires version 3.3 or above.

.. code-block:: bash

   $ virtualenv --python=python3.6 venv
   $ source venv/bin/activate

Inside the virtual environment, install Pelican and the required dependencies.

.. code-block:: bash

   (venv)$ pip install pelican markdown ghp-import

Afterwards, we can create our "source" files using pelican-quickstart

.. code-block:: bash

   (venv)$ pelican-quickstart

You will be prompted a series of questions in order to setup the pelican.conf file.

.. code-block:: text

    > Where do you want to create your new web site? [.] ./
    > What will be the title of this web site? Adrian Karcevski
    > Who will be the author of this web site? Adrian Karcevski
    > What will be the default language of this web site? [pt] en
    > Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) n
    > Do you want to enable article pagination? (Y/n) y
    > How many articles per page do you want? [10] 10
    > What is your time zone? [Europe/Paris] America/New_York
    > Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) Y 
    > Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) n
    > Do you want to upload your website using FTP? (y/N) n
    > Do you want to upload your website using SSH? (y/N) n
    > Do you want to upload your website using Dropbox? (y/N) n
    > Do you want to upload your website using S3? (y/N) n
    > Do you want to upload your website using Rackspace Cloud Files? (y/N) n
    > Do you want to upload your website using GitHub Pages? (y/N) y
    > Is this your personal page (username.github.io)? (y/N) y
    Done. Your new project is available at /home/<your_name>/<your_name>.github.io

Once you've completed the prompt, run ls command and make sure you see the following files.

.. code-block:: text

    $ ls
    content     Makefile  pelicanconf.py  __pycache__  venv
    fabfile.py  output    publishconf.py  README.md

Now, in the content folder, create a sample content file in Markdown (.md) format.

.. code-block:: bash 

    (venv)$ touch sample.md

In your text editor:

.. code-block:: text 

    Title: Hosting a static site using Pelican and Git
    Date: 2018-09-22 16:38
    Category: Projects
    Tags: python, pelican, github, git
    Slug: post-1
    Authors: Adrian Karcevski

    GasdknjbnGajksnbkjlFSfjkn


Alternatively you can use the reStructuredText (.rst) format.

.. code-block:: bash 

    (venv)$ touch sample.rst

.. code-block:: text 

    Hosting a static site using Pelican and Git
    #####################################################
    :date: 2018-09-22 16:38
    :category: Projects
    :tags: python, pelican, github, git
    :authors: Adrian Karcevski

    GasdknjbnGajksnbkjlFSfjkn

To see what it looks like we need to make the .html files and serve them. 

.. code-block:: bash 

    (venv)$ make html && serve html

Open your browser and go to localhost:8000 to see what it looks like. You should now see your webpage.

In order to save space, I'm not going to go into adding images, rss feeds, etc.

Finally lets make some last changes with git before we commit and push the code to our remote repository.

By creating a .gitignore file git will ignore the output folder when pushing to the source branch. Then we will reload the staging area to ensure .gitignore works properly. If you setup a .gitignore when you made the repository, you can omit the reload.

.. code-block:: bash

    (venv)$ echo output > .gitignore
    (venv)$ git rm -rf --cached .
    (venv)$ git add .

Now we can commit the changes and push them to our remote repositories source branch.

.. code-block:: bash
    
    (venv)$ git commit -a -m 'intial commit' && git push origin source

Github Pages requires a ghpages branch which is where our files will be served from. The following command will accomplish this step.

.. code-block:: bash

    (venv)$ make github

Congratulations, you've just created a webpage on Github Pages. You should see your content when you visit <your_name>.github.io



