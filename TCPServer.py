
import socket
import threading

import StatusCodes
import ServerResponseUtils
import ContentTypes
import GetAndHeadRequestHandler
import PostRequestHandler

def read_file(file_path):
    with open(file_path, "rb") as file:
        return file.read()

def process_request(client_socket, data_request):
    request_lines = data_request.split(b"\r\n")

    method, path, _ = request_lines[0].decode().split(" ")

    response = b""
    response_body = b""

    if method == "GET":
        response, response_body = GetAndHeadRequestHandler.get_request_handler(path)
    elif method == "POST":
        response, response_body = PostRequestHandler.post_request_handler()
    elif method == "HEAD":
        response, response_body = GetAndHeadRequestHandler.head_request_handler(path)
    else:
        response += ServerResponseUtils.status_line(StatusCodes.STATUS_NOT_IMPLEMENTED, "Not implemented")
        response += ServerResponseUtils.content_type_header(ContentTypes.PLAIN_TEXT_TYPE)
        response_body += b"501 Not Implemented"
        response += ServerResponseUtils.content_length_header(str(len(response_body)))

    response += ServerResponseUtils.header_date()
    response += ServerResponseUtils.server_header()
    response += ServerResponseUtils.finish_response()

    client_socket.sendall(response + response_body)

def process_client(client_socket, client_address):
    with client_socket:
        print(f"Connection from {client_address}")
        data_request = client_socket.recv(4096)

        process_request(client_socket, data_request)
        

def init_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen()

        print(f"Server running on http://{host}:{port}")

        try:
            while True:
                client_socket, client_address = server_socket.accept()

                # thread per client
                client_thread = threading.Thread(target=process_client, args=(client_socket, client_address))
                client_thread.start()

        except KeyboardInterrupt:
            print("Server morido")
            server_socket.close()


if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 8085
    init_server(HOST, PORT)
