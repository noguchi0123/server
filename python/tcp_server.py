import socketserver


class TCPRequestHandler(socketserver.StreamRequestHandler):


    def handle(self):
        data = self.rfile.readline().strip()
        print(data)

        self.wfile.write(bytes('HTTP/1.1 200 OK\r\n', 'utf-8'))
        self.wfile.write(bytes('Content-Type: text/html; charset=utf-8\r\n', 'utf-8'))
        self.wfile.write(bytes('\r\n', 'utf-8'))

        with open('index.html', 'r') as f:
            self.wfile.write(bytes(f.read(), 'utf-8'))


if __name__ == "__main__":
    host, port = 'localhost', 0

    server = socketserver.TCPServer((host, port), TCPRequestHandler)

    ip, port = server.server_address
    print("IP: %s" % ip)
    print("port: %s" % port)

    server.serve_forever()
