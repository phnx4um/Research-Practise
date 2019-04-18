from flask import Flask
from flask import render_template
import pandas as pd
import sys


app = Flask(__name__)

@app.route("/")
def index():
    name = app.config.get('video_name')
    data = app.config.get('csv_file')
    print(data.head())
    start_time = data['Start Time (seconds)'].values.tolist()
    lenght = data['Length (seconds)'].values.tolist()
    return render_template('index.html',
                            name = name,
                            start_time = start_time,
                            lenght = lenght)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python player.py videoname.mp4")
        sys.exit (1)
    print(sys.argv)
    print("")
    # reading csv file
    data = pd.read_csv("oceans_scenes.csv/oceans-Scenes.csv")
    data = data.loc[: ,['Start Time (seconds)', 'End Time (seconds)', 'Length (seconds)']]
    app.config['video_name'] = sys.argv[1]
    app.config['csv_file'] = data
    app.debug = True
    app.run()
