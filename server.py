from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser

try:
    port = 8000
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    print(f"running on http://localhost:{port}/")
    webbrowser.open("http://localhost:8000/", new=1)
    httpd.serve_forever()
except KeyboardInterrupt:
    print("Server terminated")
    httpd.socket.close()