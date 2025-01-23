import sys
from server.server import server
from client.client import send_request_to_server

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py [server|client]")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "server":
        server()
    elif mode == "client":
        print("Enter the page you want to request:")
        page_html = input()
        
        if page_html[0] != '/':
            page_html = '/' + page_html

        print("Requesting '"+page_html+"' from the server...")

        http_response = send_request_to_server('/'+page_html)
        print(http_response)
    else:
        print("Unknown mode. Use 'server' or 'client'.")
