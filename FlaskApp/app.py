from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World'

class Film:
    def __init__(self, name, stars):
        self.name = name
        self.stars = stars

def get_films():
    films = []
    with open("films.csv", "r") as f:
        for line in f:
            film_data = line.split(',')
            films.append(Film(film_data[0], film_data[1]))
    return films

@app.route('/films/list')
def films():
    films = get_films()
    stars_filter = request.values.get("stars", "")
    return render_template('films.html', films=films, stars_filter=stars_filter)

@app.route('/films/submit')
def submit_film_form():
    return render_template('submit_film.html')


@app.route('/submit_film', methods=['POST'])
def submit_film():
    film = request.form['name']
    stars = request.form['stars']
    with open("films.csv", "a") as f:
        f.write('\n' + film + ',' + stars)
    return redirect(url_for('films'))