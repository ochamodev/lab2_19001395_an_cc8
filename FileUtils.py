import socket
import threading
import os
from datetime import datetime

def read_file(file_path):
    if (os.path.isfile(file_path)):
        with open(file_path, "rb") as file:
            return file.read()
    else:
        return