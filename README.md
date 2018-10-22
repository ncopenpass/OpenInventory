# Development setup

The project is built with Python (3.7) and uses Flask application framework.
 
The project can be setup with pip in a virtual environments.

## Installation

     # first install virutalenv
     pip install virtualenv
     
     # setup a virtual environment
     virtualenv venv
     
     # activate the virutal environment
     source venv/bin/activate
     
     # install all dependencies in the virtual environment
     pip install -r requirements.txt
     
## Execution

    flask run
    
    # to run in debug mode
    FLASK_DEBUG=1 flask run
    
## Usage
    
With flask running the application is accessible at
http://127.0.0.1:5000

The admin console is accessible at:
http://127.0.0.1:5000/admin

The application uses sqllite by default and stores all data in the application root directory in a file named "inventory.db".

         
     
     