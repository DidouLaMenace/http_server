import sys
from server.server import run_server
from client.client import send_request

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python run.py [server|client]")
        sys.exit(1)

    mode = sys.argv[1]
    if mode == "server":
        run_server()
    elif mode == "client":
        print("Requesting '/' from the server...")
        html = send_request('/')
        print("HTML content received:")
        print(html)
    else:
        print("Unknown mode. Use 'server' or 'client'.")
