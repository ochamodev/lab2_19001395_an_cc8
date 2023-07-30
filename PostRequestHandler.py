
import StatusCodes
import ServerResponseUtils
import ContentTypes
import FileUtils

def post_request_handler():
    response = b""
    response_body = b""
    response += ServerResponseUtils.status_line(StatusCodes.STATUS_OK, "Ok")
    response += ServerResponseUtils.content_length_header(str(len(response_body)))
    response += ServerResponseUtils.content_type_header(ContentTypes.PLAIN_TEXT_TYPE)

    return response, response_body
