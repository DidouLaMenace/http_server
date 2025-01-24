import socket
import os
from datetime import datetime

HOST = '127.0.0.1'
PORT = 8080
STATIC_DIR = 'server/static'


def build_response(status_code, request_path, body):
    status_messages = {
        200: "OK",
        400: "BAD REQUEST",
        403: "FORBIDDEN",
        404: "NOT FOUND",
        405: "METHOD NOT ALLOWED",
        414: "URI TOO LONG",
        500: "INTERNAL SERVER ERROR"
    }

    status_message = status_messages.get(status_code, "INTERNAL SERVER ERROR")
    response_headers = f"HTTP/1.1 {status_code} {status_message}\n"

    response_headers += f"Date: {datetime.now().strftime('%a, %d %b %Y %H:%M:%S GMT')}\n"
    response_headers += "Content-Type: text/html\n"
    
    # En-tête spécifique pour 200 OK (Last-Modified)
    if status_code == 200 and request_path:
        last_modified = datetime.fromtimestamp(os.path.getmtime(STATIC_DIR + request_path)).strftime("%a, %d %b %Y %H:%M:%S GMT")
        response_headers += f"Last-Modified: {last_modified}\n"

    response_headers += f"Content-Length: {len(body)}\n\n"

    return response_headers



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

    # Check if request is well-formed
    if len(request_line_parts) < 2:
        response_headers = build_response(400, "", "")
        response_body = b"<html><body><h1>400 Bad Request</h1></body></html>"
        client_socket.sendall((response_headers + "\n").encode() + response_body)
        client_socket.close()
        return

    # Check if request path is too long
    if len(request_path) > 2048:
        response_headers = build_response(414, "", "")
        response_body = b"<html><body><h1>414 URI Too Long</h1></body></html>"
        client_socket.sendall((response_headers + "\n").encode() + response_body)
        client_socket.close()
        return


    if request_method == 'GET':
        # Default Value for request_path
        if request_path == '/':
            request_path = '/index.html'
        
        # Default value for response_body and response_headers
        response_body = b""
        response_headers = ""

        # Normalize request path
        request_path = os.path.normpath(request_path)
        file_path = os.path.join(STATIC_DIR, request_path.lstrip('/'))
        
        # Check if file is outside of STATIC_DIR
        if not os.path.abspath(file_path).startswith(os.path.abspath(STATIC_DIR)):
            response_headers = build_response(403, "", "")
            response_body = b"<html><body><h1>403 Forbidden</h1></body></html>"
        else :
            try:
                with open(file_path, 'rb') as file:
                    # Response 200 OK
                    response_body = file.read()
                    response_headers = build_response(200, request_path, response_body)
            except FileNotFoundError:
                # Response 404 Not Found
                response_headers = build_response(404, "", "")
                response_body = b"<html><body><h1>404 Not Found</h1></body></html>"
    else:
        # Response 405 Method Not Allowed
        response_headers = build_response(405, "", "")
        response_body = b"<html><body><h1>405 Method Not Allowed</h1></body></html>"

    # Sending response
    response = response_headers.encode() + b"\r\n\r\n" + response_body
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