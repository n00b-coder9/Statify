from flask import Flask, request

from spotify_test import playlist_stats
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figur

app = Flask(__name__, static_url_path= '')

@app.route('/')
def hello_word():
    return app.send_static_file('index.html')

@app.post('/stats')
def playlistStats():
    playlist = request.form['nm']
    playlist_stats(playlist)
    return playlist_stats(playlist)
if __name__ == "__main__":
    app.run()
    