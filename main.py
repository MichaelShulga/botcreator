import argparse
import os

from flask import Flask, render_template, redirect, request, abort

params = argparse.ArgumentParser()
params.add_argument('--heroku', action='store_true')
args = params.parse_args()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'


@app.route('/')
def index():
    return 'Index Page'


def main():
    if args.heroku:  # run on heroku service
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
    else:  # run on my pc
        app.run(port=8085, host='127.0.0.1', debug=True)


if __name__ == '__main__':
    main()
