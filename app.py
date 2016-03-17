from flask.ext.api import FlaskAPI

app = FlaskAPI(__name__)

@app.route('/', methods=['POST','GET'])
def example():

    return {'request data': request.data}


if __name__ == "__main__":
    app.run(debug=True)
