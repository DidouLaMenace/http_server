import socket
import os

# Configuration
HOST = '127.0.0.1'
PORT = 8080
STATIC_DIR = 'server/static'  # Répertoire contenant les fichiers HTML

# Fonction pour traiter une requête
def handle_request(client_socket):
    request = client_socket.recv(1024).decode()
    print("Request received:")
    print(request)

    # Extraire la requête GET
    try:
        lines = request.splitlines()
        if len(lines) > 0 and lines[0].startswith('GET'):
            file_path = lines[0].split()[1]
            if file_path == '/':
                file_path = '/index.html'
            file_path = STATIC_DIR + file_path

            # Vérifier si le fichier existe
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    content = f.read()
                response = (
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: text/html\r\n"
                    f"Content-Length: {len(content)}\r\n"
                    "\r\n" +
                    content
                )
            else:
                response = (
                    "HTTP/1.1 404 Not Found\r\n"
                    "Content-Type: text/html\r\n"
                    "\r\n"
                    "<html><body><h1>404 Not Found</h1></body></html>"
                )
        else:
            response = (
                "HTTP/1.1 400 Bad Request\r\n"
                "Content-Type: text/html\r\n"
                "\r\n"
                "<html><body><h1>400 Bad Request</h1></body></html>"
            )

    except Exception as e:
        response = (
            "HTTP/1.1 500 Internal Server Error\r\n"
            "Content-Type: text/html\r\n"
            "\r\n"
            "<html><body><h1>500 Internal Server Error</h1></body></html>"
        )

    client_socket.sendall(response.encode())
    client_socket.close()

# Fonction principale pour exécuter le serveur
def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Server listening on {HOST}:{PORT}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        handle_request(client_socket)

if __name__ == '__main__':
    run_server()
