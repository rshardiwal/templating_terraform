from flask import Blueprint, Response
from flask_cors import CORS
import time
import os

from utils import get_directory_path

routes = Blueprint('routes', __name__)
CORS(routes)  # Enable CORS for the blueprint

def stream_file(file_path):
    def generate():
        with open(file_path, 'r') as f:
            while True:
                line = f.readline()
                print ("line", line)
                if not line:
                    time.sleep(1)  # Sleep briefly to avoid busy waiting
                    continue
                print(f'Sending line: {line.strip()}')  # Log the line being sent
                yield f"data: {line}\n\n"  # Format the line as a server-sent event
    return generate()

@routes.route('/stream_output')
def stream_output():
    file_path = get_directory_path('log_output.txt')  # Replace with your actual file path
    if not os.path.exists(file_path):
        print(f'File does not exist: {file_path}')
        return Response('File not found', status=404, mimetype='text/plain')
    
    print(f'Streaming file: {file_path}')
    return Response(stream_file(file_path), mimetype='text/event-stream')

