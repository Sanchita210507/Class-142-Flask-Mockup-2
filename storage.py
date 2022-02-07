import csv
all_movies = []

with open("final.csv", encoding = 'utf-8') as f:
    r = csv.reader(f)
    data = list(r)
    all_movies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch = []
