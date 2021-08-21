[![LICENSE](https://img.shields.io/badge/LICENSE-GPL--3.0-green)](https://github.com/vahidtwo/suggest_food_restaurant/blob/master/LICENSE) 
[![Requirements](https://img.shields.io/badge/Requirements-See%20Here-orange)](https://github.com/vahidtwo/suggest_food_restaurant/blob/master/requirements.txt)

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

this is a `simple project` without `auth or permeation` and develop for a friend in simplest way

so take it easy :)