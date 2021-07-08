# Todo App

Todo app is a simple CRUD project developed using FastApi

## Installation
The first thing to do is to clone the repository:

```
git colne https://github.com/AbdurRehman91/todo.git
cd todo
```
Create a virtual environment to install dependencies in and activate it:
```
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```
Then install the dependencies:
```bash
(env)$ pip install -r requirements.txt
```
Once pip has finished downloading the dependencies:

```
(env)$ cd project
(env)$ uvicorn main:app --reload
```
Run the database migration:
```
alembic upgrade head
```
And then navigate to ```http://127.0.0.1:8000/docs```for going through the Apis
