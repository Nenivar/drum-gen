import requests, spotipy
from flask import Flask

r = requests.get('https://api.spotify.com/v1/audio-analysis/50DSbkbg64VwotJdcvSqkV', headers={})
print(r.text)