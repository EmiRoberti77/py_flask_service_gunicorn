import json
import logging
import os
import math
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['post'])
def handle_post():
    content = json.loads(request.data)
    input = float(content["input"])
    return f"{str(math.floor(input))}".strip(), 200

if __name__ != '__main__':
    #redirect Flask logs to Gunicorn
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.logger.info('Service started')
else:
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))