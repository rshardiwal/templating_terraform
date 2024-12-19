from flask import Blueprint, Response
from flask_cors import CORS
import time
import os
import logging

from utils import get_directory_path

routes = Blueprint('routes', __name__)
CORS(routes)  # Enable CORS for the blueprint

def stream_file(file_path):
    def generate():
        buffer = []
        with open(file_path, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    if buffer:
                        for buffered_line in reversed(buffer):
                            logging.info(f'Sending line: {buffered_line.strip()}')
                            yield f"data: {buffered_line}\n\n"
                        buffer = []
                    time.sleep(1)  # Sleep briefly to avoid busy waiting
                    continue
                buffer.append(line)
    return generate()

@routes.route('/stream_output')
def stream_output():
    file_path = get_directory_path('app.log')  # Replace with your actual file path
    if not os.path.exists(file_path):
        logging.error(f'File does not exist: {file_path}')
        return Response('File not found', status=404, mimetype='text/plain')
    
    logging.info(f'Streaming file: {file_path}')
    return Response(stream_file(file_path), mimetype='text/event-stream')

