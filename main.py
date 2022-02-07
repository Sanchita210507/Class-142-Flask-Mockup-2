from flask import Flask, jsonify
from storage import all_movies, liked_movies, not_liked_movies, did_not_watch
from demographicFiltering import output
from contentFiltering import get_recommendations

app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
    movie_data = {
        "title": all_movies[0][19],
        "poster_link": all_movies[0][27],
        "release_date": all_movies[0][13] or "N/A",
        "duration":all_movies[0][15],
        "rating":all_movies[0][20],
        "overview":all_movies[0][9],
    }
    return jsonify({
        "data": movie_data,
        "status": "success"
    })

@app.route("/liked_movies", methods = ["POST"])
def liked_movie():
    movie = all_movies[0]
    liked_movies.append(movie)
    all_movies.pop(0)

    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked_movies", methods = ["POST"])
def unliked_movie():
    movie = all_movies[0]
    not_liked_movies.append(movie)
    all_movies.pop(0)

    return jsonify({
        "status": "success"
    }), 201

@app.route("/did_not_watch", methods = ["POST"])
def did_not_watch():
    movie = all_movies[0]
    did_not_watch.append(movie)
    all_movies.pop(0)

    return jsonify({
        "status": "success"
    }), 201

@app.route("/popular_movies")
def popular_movies():
    movie_data = []
    for movie in output:
        _d = {
            "title": movie[0],
            "poster_link":movie[1],
            "release_date":movie[2] or "N/A",
            "duration":movie[3],
            "rating":movie[4],
            "overview":movie[5]
        }

        movie_data.append(_d)
        
    return jsonify({
         "data":movie_data,
        "status": "success"
    }), 200

@app.route("/recommended-movies")
def recommended_movies():
    all_recommended = []
    for i in liked_movies:
        output = get_recommendations(i[19])
        for i in output:
            all_recommended.append(i)
    import itertools 
    all_recommended.sort()
    all_recommended = list( all_recommended for all_recommended,_ in itertools.groupby(all_recommended) )
    movie_data = []
    for movie in all_recommended:
        _d = {
            "title": movie[0],
            "poster_link":movie[1],
            "release_date":movie[2] or "N/A",
            "duration":movie[3],
            "rating":movie[4],
            "overview":movie[5]
        }
        movie_data.append(_d)

    return jsonify({
        "data" : movie_data,
        "status" : "success"
    })
    
if __name__ == "__main__":
    app.run(debug = True)
