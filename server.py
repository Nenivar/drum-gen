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
        r = requests.get('https://api.spotify.com/v1/audio-analysis/50DSbkbg64VwotJdcvSqkV', headers={'Authorization': 'Bearer {}'.format(code)})
        # get auth token
        body = {'grant_type':'authorization_code', 'code':code, 'redirect_uri':auth['redirect_uri'], 'client_id':auth['client_id'], 'client_secret':auth['client_secret']}
        #headers = {'Authorization': 'Basic {}'.format()}
        r = requests.post('https://accounts.spotify.com/api/token', data=body)
        return r.text
    else:
        return redirect(url_for('authorization'))
    #token = util.prompt_for_user_token(username=auth['username'], scope='', client_id=auth['client_id'], client_secret=auth['client_secret'], redirect_uri=auth['redirect_uri'])
    #sp = spotipy.Spotify(auth=token)
    #return token

@app.route('/authorization')
def authorization():
    link = 'https://accounts.spotify.com/authorize?response_type=code&client_id={}&scope={}&redirect_uri={}'\
        .format(auth['client_id'],auth['scope'],auth['redirect_uri'])
    return redirect(link)