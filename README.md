**URL Minion**
---------------

Another url shortner using Django.

Deployed on [heroku](https://url-minion.herokuapp.com) (for now)


To install

```
git clone https://github.com/Tobey/url-minion.git
```

Run locally, using `python version 3.6+`

Install requirements

```
pip install -r requirements.txt
```

Create local db

```
python manage.py migrate
```


Run the tests
```
python manage.py test

```

Start server
```
python manage.py runserver
```
>...\
>Starting development server at http://127.0.0.1:8000/



**Basic API**
--------------
[Read the docs](https://url-minion.herokuapp.com/docs/) 



**Methodology**
-----------
A [deterministic approach](http://code.activestate.com/recipes/576918/) to generate short urls by using sequential incrementing numbers


*Pros*

- Small application, so can be scalled horizontally to handle more requests

- Unique short url guaranteed without heavy db queries/integrity checks for create operation

- Deterministic approach can save DB queries as id/index pair can always be calculated


*Cons*


- Cannot scale accross multiple (distributed) databases as unique integer ID will be duplicated

> Perhaps using an approach of encoded id + hash + salt can solve this issue, however
>  data integrity is not guaranteed

- Current implementation cannot guarantee shortened url size

> The more urls stored in the db, the longer the short_url becomes 

- Bottlenecked by sequential db saves

- DB primary id is key to backup and recreated DB


Intermediaries such as caches can be ussed to make redirect operations quicker. 
