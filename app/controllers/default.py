# logica das paginas
# from MODULO import VARIAVEL esta q está dentro do init fora das pastas
from app import app


@app.route("/")
def index():
    return "Hello Flask"
