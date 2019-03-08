from flask import Flask, redirect, json, request
app = Flask('blah')

auth = dict()
with open('auth.json', 'r') as f:
    auth = json.load(f)

@app.route('/')
def index():
    code = request.args.get('code')
    if code:
        print(code)
    return 'words'

@app.route('/authorization')
def authorization():
    scope = 'user-read-private'
    link = 'https://accounts.spotify.com/authorize?response_type=code&client_id={}&scope={}&redirect_uri={}'\
        .format(auth['client_id'],scope,auth['redirect_uri'])
    return redirect(link)