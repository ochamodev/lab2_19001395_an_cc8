
from datetime import datetime

encoding = "utf8"

def status_line(statusCode, statusPhrase):
    return bytes("HTTP/1.1 {statusCode} {statusPhrase}\r\n"
                 .format(statusCode=statusCode, statusPhrase=statusPhrase), encoding)

def header_date():
    current_datetime = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")
    return bytes("Date: {date}\r\n".format(date=current_datetime), encoding)

def server_header():
    return bytes("Server: Alfred/1.0\n", encoding)

def finish_response():
    return b"\r\n"

def content_type_header(content):
    return bytes("Content-Type: {content}\r\n".format(content=content), encoding)

def content_length_header(length):
    return bytes("Content-Length: {length}\r\n".format(length=length), encoding)