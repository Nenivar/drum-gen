import json
from flask import Flask, redirect, request, url_for
import requests
from spotipy import util
app = Flask('blah')

auth = dict()
with open('auth.json', 'r') as f:
    auth = json.load(f)

@app.route('/')
def index():
    code = request.args.get('code')
    
    if code:
        # get auth token
        body = {'grant_type':'authorization_code', 'code':code, 'redirect_uri':auth['redirect_uri'], 'client_id':auth['client_id'], 'client_secret':auth['client_secret']}
        r = requests.post('https://accounts.spotify.com/api/token', data=body)
        token = r.json()['access_token']

        r = requests.get('https://api.spotify.com/v1/audio-analysis/50DSbkbg64VwotJdcvSqkV', headers={'Authorization': 'Bearer {}'.format(token)})
        return r.text
    else:
        return redirect(url_for('authorization'))

@app.route('/authorization')
def authorization():
    link = 'https://accounts.spotify.com/authorize?response_type=code&client_id={}&scope={}&redirect_uri={}'\
        .format(auth['client_id'],auth['scope'],auth['redirect_uri'])
    return redirect(link)