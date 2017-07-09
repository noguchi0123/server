from http.server import HTTPServer, SimpleHTTPRequestHandler


class Handler(SimpleHTTPRequestHandler):

    def do_GET(self):
        body = b'HELLO HTTP WORLD!'
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Content-length', len(body))
        self.end_headers()
        self.wfile.write(body)


host = 'localhost'
port = 8000
httpd = HTTPServer((host, port), Handler)
print('serving at port: ', port)
httpd.serve_forever()
