from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin

import react as r

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



@cross_origin()
@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.form

    if 'url' not in data or 'filename' not in data or 'scope' not in data:
        return jsonify({'error': 'Invalid request'}), 400
    url = data['url']
    xpath = data['xpath']
    scope = data['scope']
    filename = data['filename']
    filename = filename + '.txt'

    text_content = r.scrape(url, xpath,  scope)
    response = Response(text_content, content_type='text/plain')
    response.headers['Content-Disposition'] = 'attachment; filename=' + filename
    return response


@app.route("/", methods=['GET'])
@cross_origin()
def say_hello():
    return "hello there, Discovery"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9001)
