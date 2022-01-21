from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def root_page():
    return 'My website has lots of subpages, see if you can find them all!\n'

@app.route('/<path>')
def subpage(path):
    if path == 'kbgraphics':
        return 'jctf{1t5_jUst_4_nUmb3r_ag8h7z8021}\n', 404
    return f'Welcome to {path}!\n', random.choice([200, 400, 401, 402, 403, 404, 500])
