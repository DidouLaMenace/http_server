import socket
import os

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8080

def send_request_to_server(page):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    request = f"GET {page} HTTP/1.1\nHost: {SERVER_HOST}\n\n"
    client_socket.sendall(request.encode())

    # Handle response from server
    response = b""
    # Keep receiving data until no more data is received
    while True:
        part = client_socket.recv(1024)
        if not part:
            break
        response += part


    # Print response from server
    response_split = response.decode().split("\r\n\r\n", 1)
    headers = response_split[0]

    if len(response_split) > 1:
        body = response_split[1]
    else:
        body =""

    print("\nEn-tête HTTP:")
    print(headers)

    # Save the body to a file in the folder client/output
    with open("client/output/response.html", "w") as file:
        file.write(body)
    
    client_socket.close()
    return "Corps HTTP:\r\n" + body
