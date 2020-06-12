# aai_artastic
Applied AI project for open artworks using wikimedia.

# Setting up Dev Env
* Install VS Code and Remote Containers Plugin. 
* Reload Folder in Container 
* Switch to `artastic/` and run `pip install -r requirements.txt`
* CD to `artastic/frontend`
* run `npm install`
* run `npm run serve`
* open second terminal
* cd to `artastic/`
* run `python manage.py runserver`
* go to `localhost:8000` - this is where the frontend will be :) 

You can also run this without VS Code and Remote Containers but you have to install python3 with requirements.txt and npm with package.json dependencys local.

# Local installation (mamba)

* cd `artastic/`
* run `conda create --file requirements-mamba.txt --name artastic`
* cd `artastic/frontend`
* run `npm install`
* open new terminal with `npm run serve`
* cd `artastic/`
* open new terminal with `python manage.py runserver`
