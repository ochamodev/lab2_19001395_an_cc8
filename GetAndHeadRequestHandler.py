
import StatusCodes
import ServerResponseUtils
import ContentTypes
import FileUtils

def get_request_handler(file_path):
    response_body = b""
    response = b""
    html_content = None
    if file_path == "/":
        html_content = FileUtils.read_file("index.html")
    else:
        path = file_path[1:]
        html_content = FileUtils.read_file(path)
    
    if html_content:
        response_body = html_content
        response += ServerResponseUtils.status_line(StatusCodes.STATUS_OK, "OK")
        response += ServerResponseUtils.content_type_header(ContentTypes.HTML_TYPE)
        response += ServerResponseUtils.content_length_header(str(len(response_body)))
    else:
        response_body = b"404 Not Found"
        response += ServerResponseUtils.status_line(StatusCodes.STATUS_NOT_FOUND, "Not Found")
        response += ServerResponseUtils.content_type_header(ContentTypes.PLAIN_TEXT_TYPE)
        response += ServerResponseUtils.content_length_header(str(len(response_body)))

    return response, response_body

def head_request_handler(file_path):
    response_body = b""
    response = b""
    response, _ = get_request_handler(file_path)
    return response, response_body