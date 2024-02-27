# my_flask_airbnb

my_flask_airbnb contains an app with functionality to do an API call to MongoDB Atlas
where there is a public air bnb dataset. The App queries that data set base on user inputs (simplified to Numbers of Bedrooms, and Country). The results are displayed in a table format at the same time that data is saved in a local Users.sqlite3 db (showcasing data persistent). While being on the results page, through a button, the user has an option to filter only highest-ranking places above 85 rating (showcasing data manipulation from sqlite3 db contents). 
Also, the user can do another search from the results page or exit, But while being on the Highest ranking result page, the user can only do a new search or exit

## Local development

I used WSL:UBUNTU to set up the virtual environment and develop this app
Follow the instructions below to get the app up and running on your machine

1.  Install Python 3.10 .
1.  Install dependencies.
    ```shell
    pip install requirements.txt 
    ```
1.  Once dependencies are installed, set the entry point for the app 
    ```shell
    export FLASK_APP=src/app.py
    ```
   
## Backend

Here are a few tasks that are useful when running the backend app.
Make sure they all run on your machine.

1.  Run tests
    ```shell
    pytest test_login.py
    pytest test_choices.py
    ```

1.  Run metrics 
    ```shell
    http://localhost:5000/metrics
    http://localhost:5000/health
    ```

1.  Run server
    ```shell
    flask run
    ```


## Frontend

Here are a few tasks that are useful when running the frontend app.
Make sure they all run on your machine.


1.  Run server
    ```shell
    flask run
    ```

## Integration tests

If it's helpful, you may want to run integration tests during development.
Do so with the tasks below.

1.  Run tests
    ```shell
    pytest test_integration.py
    ```

