#!/usr/bin/python

import os
import magic
from flask import (
    Flask,
    redirect,
    jsonify
)



app = Flask(__name__)

def file_list(directory):
    """
    params: string  (eg: '~')
    return: array
    """
    return os.listdir(directory)

@app.route('/files')
def _files():
    """
    return: JSON
    contains:
    - root directory + filename
    - file type
    """
    file_info = []
    target_directory = "/home/vickydasta/Downloads/"
    file_server_dir = "http://localhost:9000/"

    for berkas in file_list(target_directory):
        file_info.append({"filename":berkas, "location":file_server_dir+berkas, "filetype":magic.from_file(target_directory+berkas, mime=False)})
    return jsonify({"status":"OK", "data":file_info})

if __name__ == '__main__':
    app.debug=True
    app.run(host="0.0.0.0", port=8000)
