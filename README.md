# Go Team Win
**The source code for the Go Team Win website written in the Django web framework**

## Installation and Requirements
The website works wonderfully on Mac and Linux systems. Not all that tested (well, not tested at all) on Windows. The setup instructions are for Linux but Mac instructions shouldn't be that hard to figure out. There are a few extras needed that make life easier for setting up. All the commands assume you are in the root of the goteamwin repository.

### VirtualEnv, Pip, and Django
The website uses the [Django WebFramework][django] for the website logic. This is a python framework so preferably you'll want to sandbox yourself using [VirtualEnv][virtualenv]. So first install that as root.

    pip install virtualenv

Next setup your virtual environment. I prefer to use the directory name of `venv` and the `.gitignore` has this directory marked already. 

    virtualenv venv
    
This produces your `venv` directory. After that's squared away you'll want to activate your environment so that we can sandbox ourselves off from the rest of the system.

    source venv/bin/activate

Now we are in a sandboxed version that we can install all the python requirements. So now let's install those requirements.

    pip install -r requirements.txt
    
This takes the `requirements.txt` file in our repo and installs all of the packages needed to run the site including the version of Django and all required Django modules.

## Setup the Database
The repo contains all the code needed to create the proper database. We need to run a database migration so that Django doesn't freak out. Luckily this is very easy and will set the defaults you'll need for the superuser. 

    python manage.py syncdb

Enter the defaults you want and you're ready to run the site.

## Running the Code
Django contains its own development server so let's use that. To run the server you can use the `manage.py`

    python manage.py runserver

The website will start running at `http://127.0.0.1:8000`. 

[django]: https://www.djangoproject.com/
[virtualenv]: https://virtualenv.readthedocs.org


