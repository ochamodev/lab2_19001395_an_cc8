
import socket
import threading

import StatusCodes

def process_request(client_socket, data_request):
    request_lines = data_request.split(b"\r\n")

    method, path, _ = request_lines[0].decode().split(" ")

    if method == "GET":
        print(path)
    if method == "POST":
        print(path)
    if method == "HEAD":
        print(path)
    else:
        print("Metodo no implementado")


    client_socket.sendall(b"<html><body><h1>Hello, World!</h1></body></html>")

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



if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 8085
    init_server(HOST, PORT)
