# Project 1

Web Programming with Python and JavaScript


export FLASK_APP=application.py

export DATABASE_URL="postgres://grumhrwufdbccl:42a29f4cb61247e853f9f82e4461832a91bedff295839c7bbe997c4b81af7941@ec2-46-137-177-160.eu-west-1.compute.amazonaws.com:5432/dhjmm0tcs3nu0"

flask run







https://www.goodreads.com/api/keys
key: mL2W4gtajeUDVQC4lJTHmQ

import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "KEY", "isbns": "9781632168146"})
print(res.json())


import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "mL2W4gtajeUDVQC4lJTHmQ", "isbns": "9781632168146"})
print(res.json())
