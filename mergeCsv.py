import csv

with open("movies.csv", encoding= 'utf-8') as f:
    r = csv.reader(f)
    data = list(r)
    all_movies = data[1:]
    headers = data[0]

headers.append("poster_link")
with open("final.csv", "a+", encoding= 'utf-8') as f:
    c = csv.writer(f)
    c.writerow(headers)

with open("movie_links.csv", encoding= 'utf-8') as f:
    r = csv.reader(f)
    data = list(r)
    all_movie_links = data[1:]

for i in all_movies:
    #Searching column "Original title" in "movies.csv" and then iterating that in "movielinks.csv"
    poster_found = any(i[8] in movie_link_items for movie_link_items in all_movie_links)
    if poster_found:
        for movie_link_item in all_movie_links:
            if i[8] == movie_link_item[0]:
                i.append(movie_link_item[1])
                if len(i) == 28:
                    with open("final.csv", "a+",  encoding= 'utf-8') as f:
                        c = csv.writer(f)
                        c.writerow(i)
