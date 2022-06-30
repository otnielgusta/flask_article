from app import app
from teste import Controller

@app.route('/')
@app.route('/index')
def index():
    return Controller.teste()