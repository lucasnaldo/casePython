import falcon
from api.resources.home import Home
from waitress import serve # Necessário para substituir gunicorn no Windows


def create():
    api = falcon.API()
    api.add_route('/', Home())
    return api


app = application = create()
serve(app, host='0.0.0.0', port=80) # nova linha para não precisar rodar o arquivo app.sh