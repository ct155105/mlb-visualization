# Overview

This template is for a containerized DEV environment for a 3 tier application. The tiers are:
    <ul>
        <li>
            Frontend - Node.js SPA
        </li>
        <li>
            API - Python Flask
        </li>
        <li>
            DB - MongoDB
        </li>
    </ul>

# Development Environement Setup

<small>See https://code.visualstudio.com/docs/remote/containers-advanced#_connecting-to-multiple-containers-at-once for more info </small>

To build the DEV containers:
    <ul>
        <li>
            Open Visual Studio Code
        </li>
        <li>
           Run Remote-Containers: Open Folder in Container... from the Command Palette (F1) and select the api folder. This will create containers for all 3 tiers
        </li>
        <li>
            Open a second instance of VS Code
        </li>
        <li>
           Run Remote-Containers: Open Folder in Container... from the Command Palette (F1) and select the frontend folder.
        </li>
        <li>
           Run Remote-Containers: Open Folder in Container... from the Command Palette (F1) and select the frontend folder.
        </li>
        <li>
           In the terminal from the frontend container, run  
           ```
           npm install -g @vue/cli
                # OR
                yarn global add @vue/cli
            ```
        </li>
        <li>
           In the terminal from the frontend container, run  
           ```vue create .```
           and follow the prompts to create the new vue app
        </li>
    </ul>

The api can connect to the database by initializing a MongoDB client with the following configuration:

``` client = MongoClient('mongo-db') ```

The frontend can connect to the backend at http://api:5000 if using the default port for a flask app

The api container opens port 5000, so please ensure that is the port the api is listening on. This is the default port for Flask applications
The frontend container opens port 8080, so please ensure that is the port the frontend is listening on. This is the default port for VueJS applications

When running, the frontend application should be accesible at http://localhost:8080/
