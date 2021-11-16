from flask import Flask, request, render_template, send_file

from spotify_test import playlist_stats

app = Flask(__name__)


@app.route("/")
def hello_word():
    return render_template("index.html")


@app.post("/stats")
def playlistStats():
    playlist = request.form["nm"]
    playlist_stats(playlist)
    return send_file('templates/images/new_plot.pdf',
                     mimetype='application/pdf',
                     attachment_filename='Stats.pdf',
                     as_attachment=True)


if __name__ == "__main__":
    app.run()
