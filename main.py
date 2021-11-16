from flask import Flask, request, render_template, send_file

from spotify_test import playlist_stats
from flask_cors import CORS, cross_origin

app = Flask(__name__)

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def hello_word():
    return render_template("index.html")


@app.post("/stats")
@cross_origin()
def playlistStats():
    playlist = request.form["nm"]
    playlist_stats(playlist)
    return send_file('templates/images/new_plot.pdf',
                     mimetype='application/pdf',
                     attachment_filename='Stats.pdf',
                     as_attachment=True)


if __name__ == "__main__":
    app.run(debug= True)
