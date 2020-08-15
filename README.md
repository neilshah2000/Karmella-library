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