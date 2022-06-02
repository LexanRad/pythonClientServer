import json
import os
import sys

sys.path.insert(0, os.path.join(os.getcwd(), '..'))
from common.variables import MAX_PACKAGE_LENGTH, ENCODING
from decos import Log


@Log()
def get_message(socket):
    response_encoded = socket.recv(MAX_PACKAGE_LENGTH)
    if isinstance(response_encoded, bytes):
        response_json = response_encoded.decode(ENCODING)
        response = json.loads(response_json)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


@Log()
def send_message(socket, message):
    message_json = json.dumps(message)
    message_encoded = message_json.encode(ENCODING)
    socket.send(message_encoded)
