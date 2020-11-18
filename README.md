```source venv/bin/activate```


# Set up new databases
first do ```python manage.py makemigrations users```
then ```python manage.py makemigrations catalog```

then ```python manage.py migrate```

# Populate Database
```python data/addAuthor.py```
```python data/addShelves.py```
```python data/addBooks.py```
```python data/addInstances.py ```


staff@staff.com
staff

new@new.com
newpassneil

one@one.com
helloone

neilshahlimited@hotmail.com
jkasj703jdkj

neil@gmail.com
asdlkfh98jh


# email account
karmelakoliburutegia@gmail.com
lkjaSH08769UHQSDFIJB

# url for app
https://blooming-mountain-86004.herokuapp.com/static/index.html


# build process
- ```npm run build``` on front end
- copy files from build folder to catalog/static folder
- ```python manage.py runserver```
- ```git push heroku master```


# database
postgres://nktsejiolrnlvt:97bf39ec9042f4e6b4ac7bd29d419b2a2cb5bba4d8dcf5a5222cba46810102b6@ec2-52-204-20-42.compute-1.amazonaws.com:5432/ddingelil4das8

host = ec2-52-204-20-42.compute-1.amazonaws.com
port = 5432
dbname = ddingelil4das8
username = nktsejiolrnlvt
password = 97bf39ec9042f4e6b4ac7bd29d419b2a2cb5bba4d8dcf5a5222cba46810102b6


# Heroku logs
```heroku logs --tail```