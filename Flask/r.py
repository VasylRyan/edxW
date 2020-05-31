import requests

#res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "KEY", "isbns": "9781632168146"})

res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "mL2W4gtajeUDVQC4lJTHmQ", "isbns": "9781632168146"})

print(res.json())
