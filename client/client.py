import socket
import ssl

def send_request(host, port, path='/'):
    try: 
        if port == 443:
            context = ssl.create_default_context()
            client_socket = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=host)
            client_socket.connect((host, port))
        else:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))

        request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
        client_socket.sendall(request.encode())

        response = b""
        while True:
            part = client_socket.recv(4096)
            if not part:
                break
            response += part

        client_socket.close()

        response_parts = response.decode(errors="ignore").split("\r\n\r\n", 1)
        headers = response_parts[0]
        body = response_parts[1] if len(response_parts) > 1 else ""

        print("\nEn-tête HTTP:")
        print(headers)

        with open("client/output/response.html", "w") as file:
            file.write(body)
        
        return ("\nCorps HTTP:\n" + body)
    
    except socket.gaierror:
        print(f"Error: The server '{host}' does not exist.")
    except socket.timeout:
        print(f"Error: Connection to '{host}' timed out.")
    except ConnectionRefusedError:
        print(f"Error: Connection refused by the server '{host}'.")
    except Exception as e:
        print(f"Error: {e}")

    return ""

def asking_for_request():
    choice = input("What server do you want to connect ? ")

    if choice == '127.0.0.1' or choice == 'localhost':
        host = '127.0.0.1'
        port = 8080
    else:        
        host = choice
        port = 443  # Default HTTPS port

    path = input("Enter the page you want to request : ").strip()
    
    if path[0] != '/':
            path = '/' + path

    print(f"Requesting the page from {host}:{port}{path} ...")
    html = send_request(host, port, path)
    
    print(html)
