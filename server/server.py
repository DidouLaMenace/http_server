import socket
import os
from datetime import datetime

HOST = '127.0.0.1'
PORT = 8080
STATIC_DIR = 'server/static'


def handle_request(client_socket):
    request = client_socket.recv(1024).decode()
    print("Received request:")
    print(request)

    # Request View : GET /index.html HTTP/1.1
    request_lines = request.split('\n')
    request_line = request_lines[0]
    request_line_parts = request_line.split(' ')
    request_method = request_line_parts[0]
    request_path = request_line_parts[1]

    if request_method == 'GET':
        # Default Value for request_path
        if request_path == '/':
            request_path = '/index.html'
        
        # Default value for response_body and response_headers
        response_body = b""
        response_headers = ""
        response_last_modified = ""

        # Check if file exists
        try:
            file_path = os.path.join(STATIC_DIR, request_path.lstrip('/'))
            # Check if file is outside of STATIC_DIR
            if not os.path.abspath(file_path).startswith(os.path.abspath(STATIC_DIR)):
                response_headers = 'HTTP/1.1 403 FORBIDDEN\n'
                response_body = b"<html><body><h1>403 Forbidden</h1></body></html>"
            with open(file_path, 'rb') as file:
                # Response 200 OK
                response_body = file.read()
                response_headers = 'HTTP/1.1 200 OK\n'
                response_last_modified = "Last-Modified: " + datetime.fromtimestamp(os.path.getmtime(STATIC_DIR + request_path)).strftime("%a, %d %b %Y %H:%M:%S GMT") + "\n"

        except FileNotFoundError:
            # Response 404 Not Found
            response_headers = 'HTTP/1.1 404 NOT FOUND\n'
            response_body = b"<html><body><h1>404 Not Found</h1></body></html>"
    else:
        # Response 405 Method Not Allowed
        response_headers = 'HTTP/1.1 405 METHOD NOT ALLOWED\n'
        response_body = b"<html><body><h1>405 Method Not Allowed</h1></body></html>"

    response_headers += "Date: " + datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT") + "\n"
    response_headers += "Content-Type: text/html\n"
    response_headers += response_last_modified
    response_headers += "Content-Length: " + str(len(response_body)) + "\n\n"

    response = response_headers.encode() + response_body
    client_socket.sendall(response)

    client_socket.close()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on {HOST}:{PORT}...")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        handle_request(client_socket)