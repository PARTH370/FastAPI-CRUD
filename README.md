# Fast API Project
This project is a Fast API project that provides a RESTful API for user management. The project is built using Fast API, SQLAlchemy, and Pydantic. 

## Installation
1. Clone the repository
2. Create a virtual environment
3. Install the dependencies using `pip install -r requirements.txt`
4. Run the project using `python main.py`



## Project Structure
The project structure is as follows:
```
.
├── app
│   ├── user_registration
│   │   ├── views.py
│   │   ├── models.py
│   │   ├── schemas.py
│   ├── core
│   │   ├── database.py
│   │   ├── logger.py
│   │   ├── utils.py
│   ├── logs
│   │   ├── app.log
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
```

## Project Details
The project consists of the following components:
1. `app/user_registration`: Contains the views, models, and schemas for user registration.
2. `app/core`: Contains the database configuration, logger, and utility functions.
3. `app/logs`: Contains the log file for the application.
4. `main.py`: The main file to run the Fast API application.
5. `requirements.txt`: Contains the dependencies for the project.
6. `.gitignore`: Contains the files and directories to be ignored by Git.



