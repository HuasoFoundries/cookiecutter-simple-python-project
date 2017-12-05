Cookiecutter - Simple python project
========================
A simple python project, powered by [Cookiecutter](https://github.com/audreyr/cookiecutter)

# Features
- PostgreSQL using `psycopg2`
- Basic `Pandas`  usage 
	- Read from database,
	- Write spreadsheets (xls, xlsx)
	- Apply Multiprocessing
- Parallel Multiprocessing using joblib
- Environment variables using `python-dotenv`

# Usage
```
pip install -U cookiecutter
cookiecutter https://github.com/HuasoFoundries/cookiecutter-simple-python-project.git
```

You'll be prompted the followings values:

| Value               |Description                         |
| --------------------|:-----------------------------------|
| directory_name      | Directory name                     |
| project_name        | Project Name                       |
| basic_description   | A short description of the project |
| main_file           | Name of the main file              |
| author              | Your name                          |
| email               | you@email.com                      |
| version             | 0.0.1                              |