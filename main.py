from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = "0.0.0.0"
PORT = 8000

def main():
    print(f"Server running at http://{HOST}:{PORT}")
    HTTPServer((HOST, PORT), SimpleHTTPRequestHandler).serve_forever()

if __name__ == "__main__":
    main()
