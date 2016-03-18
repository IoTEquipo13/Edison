from flask.ext.api import FlaskAPI
import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

app = FlaskAPI(__name__)
UPLOAD_FOLDER = '/home/miguel/plates'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/send-image', methods=['POST', 'GET'])
def process_image():
    print "Processing image!"
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'Image Accepted!'
    raise InvalidData('The given information is invalid')

if __name__ == "__main__":
    app.run(host='0.0.0.0')


class InvalidData(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        dict_response = dict(self.payload or ())
        dict_response['message'] = self.message
        return dict_response


@app.errorhandler(500)
def server_error(error):
    return str(error), 500


@app.errorhandler(InvalidData)
def handle_invalid_data(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
