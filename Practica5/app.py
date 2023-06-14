
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hola Mundo Roman es Puto y se la mama al Teo"

if __name__=='__main__':
    app.run(port= 5000)