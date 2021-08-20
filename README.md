### Suggest food for restaurant

for install first install python and pip from its site

then run this code for install that requirement

```
pip install -r requirements.txt
```
then create a supper user for access the django panel admin
```
python manage.py createsupperuser
```

you must be create db

```
python manage.py migrate 
```
after that you can run server 

```
python manage.py runserver 
```
the swagger api doc available on root url
```
http://localhost:8000/
```
for login to admin page goto [http://localhost:8000/admin](http://localhost:8000/admin)