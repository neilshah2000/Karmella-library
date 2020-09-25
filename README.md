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
bilbao123

# url for app
https://blooming-mountain-86004.herokuapp.com/static/index.html


# build process
- ```npm run build``` on front end
- copy files from build folder to catalog/static folder
- ```python manage.py runserver```
- ```git push heroku master```
