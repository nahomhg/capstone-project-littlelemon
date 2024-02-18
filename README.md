# capstone-project-littlelemon


This LittleLemon capstone is apart of the 'Back-End Developer Capstone' section of the Meta Back-End Developer Professional Certificate on Coursera.

The API backend named 'restaurant' provides endpoints for the frontend app named 'frontend' to interact with. Users/customers of the LittleLemon restaurant are able to view the menu, as well as book a reservation for them their associates based on the resturants availability for that time.

CRUD (Create, Retrieve, Update, Delete) functionalities are also available at for customers, however, most operations are only available by hitting the respective endpoints using Postman, Insomnia, cURL etc.

Project Structure
This project consists mainly of two apps, fronend and restauarnt (the api).

frontend app
This app contains the visual views

restaurant (api) app
This app contains the URLs dispatchers/routers, serializers, and views for each endpoint of the API. It contains majority class-based views for easier code reuse, with views with multiple inheritance it is easier to debug.

Installing:

Firstly, create a folder.
    
    mkdir LittleLemonProject

Step into new folder:

    cd LittleLemonProject

Now clone the repo:
    
    git clone https://github.com/nahomhg/capstone-project-littlelemon.git

Once you've cloned the repo, create your own virtual environment, for example:

    pipenv shell

Step into repo:

    cd capstone-project-littlelemon

    cd little_lemon_project 
    
Start to install the dependencies:

    pipenv install



