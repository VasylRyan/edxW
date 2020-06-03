# Project 1

Web Programming with Python and JavaScript


export FLASK_APP=application.py

export DATABASE_URL="postgres://grumhrwufdbccl:42a29f4cb61247e853f9f82e4461832a91bedff295839c7bbe997c4b81af7941@ec2-46-137-177-160.eu-west-1.compute.amazonaws.com:5432/dhjmm0tcs3nu0"

flask run

##################################################

https://www.goodreads.com/api/keys
key: mL2W4gtajeUDVQC4lJTHmQ

import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "KEY", "isbns": "9781632168146"})
print(res.json())


import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "mL2W4gtajeUDVQC4lJTHmQ", "isbns": "9781632168146"})
print(res.json())


###########################################################

# CS50W Project 1

## Web Programming with Python and JavaScript
### https://courses.edx.org/courses/course-v1:HarvardX+CS50W+Web/course/

## Use the app on Heroku

### https://book-reviews-cs50-project1.herokuapp.com/

![](https://i.imgur.com/mB3cLV1.png)


![](https://i.imgur.com/MgO93MJ.png)


![](https://i.imgur.com/Zy7C3Oq.png)

## Usage

* Register
* Search books by name, author or ISBN
* Get info about a book and submit your own review!

## :gear: Setup your own

```bash
# Clone repo
$ git clone https://github.com/marcorichetta/cs50-project1.git

$ cd cs50-project1

# Create a virtualenv (Optional but reccomended)
$ python3 -m venv myvirtualenv

# Activate the virtualenv
$ source myvirtualenv/bin/activate (Linux)

# Install all dependencies
$ pip install -r requirements.txt

# ENV Variables
$ export FLASK_APP = application.py # flask run
$ export DATABASE_URL = Heroku Postgres DB URI
$ export GOODREADS_KEY = Goodreads API Key. # More info: https://www.goodreads.com/api
```

### DB Schema

Feel free to add your own improvements!
![DB](https://i.imgur.com/ii6nkNr.png)
