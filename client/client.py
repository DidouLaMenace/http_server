import socket

# Configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8080

def send_request(path='/'):
    """
    Envoie une requête GET au serveur HTTP et retourne le corps de la réponse.
    :param path: Le chemin de la ressource demandée (ex: '/index.html').
    :return: Le corps de la réponse HTTP.
    """
    # Créer un socket client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    # Préparer la requête HTTP
    request = f"GET {path} HTTP/1.1\r\nHost: {SERVER_HOST}\r\n\r\n"
    client_socket.sendall(request.encode())

    # Recevoir la réponse
    response = b""
    while True:
        chunk = client_socket.recv(4096)
        if not chunk:
            break
        response += chunk

    client_socket.close()

    # Découper l'entête et le corps
    response_parts = response.decode().split("\r\n\r\n", 1)
    headers = response_parts[0]
    body = response_parts[1] if len(response_parts) > 1 else ""

    print("Response received:")
    print(headers)
    return body

if __name__ == '__main__':
    print("Welcome to the HTTP client!")
    path = input("Enter the path of the page you want to request (e.g., /index.html): ").strip()
    if not path.startswith('/'):
        path = '/' + path
    html = send_request(path)
    print("HTML content received:")
    print(html)
