import base64
import json
import socket
from io import BytesIO

import PIL.Image


def client():
    with open("i.jpg", "rb") as image_file:
        data = base64.b64encode(image_file.read())
    outgoing_data = '''
    {
        "code":"IDLE",
        "data":"''' + data.decode("utf-8") + '''",
        "name":"Rupok"
    }
    '''
    print(outgoing_data)
    s = socket.socket()
    port = 55667
    s.connect(('127.0.0.1', port))
    s.send(outgoing_data.encode())
    s.close()


if __name__ == '__main__':
    client()

