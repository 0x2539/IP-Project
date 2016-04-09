# IP-Project

### Run the server
1) Make sure you have an environment setup. If not, create one:
```
cd ~/path/to/IP-Project
virtualenv env
```
2) Activate the virtual environment:
```
. env/bin/activate
```
3) Install the requirements:
```
pip install -r requirements.txt
```
4) Create the DB:
```
python api/manage.py migrate --run-syncdb
```
5) Run the server:
```
python api/manage.py runserver 0.0.0.0:8000
```
__Usually it is enough to run step 2 and 5 (if you have your project setted up beforehand)__

### Updated the models?
Delete db.sqlite3 and run:
```
python api/manage.py migrate --run-syncdb
```
