import sys
from server.server import server
from client.client import asking_for_request

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py [server|client]")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "server":
        server()
    elif mode == "client":
        asking_for_request()
    else:
        print("Unknown mode. Use 'server' or 'client'.")