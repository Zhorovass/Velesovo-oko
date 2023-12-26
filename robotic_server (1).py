from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import urllib.parse
import socket

hostname = socket.gethostname()
ip_addresses = socket.getaddrinfo(hostname, None)

print("Текущие IP-адреса локального сервера:")
for address in ip_addresses:
    ip = address[4][0]
    print(f"\t{ip}")

command001 = [b'print("ok")']
command002 = [b'print("ok")']
command003 = [b'print("ok")']


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        global command001
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        query = parsed_path.query

        if path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Hello, world!')

        elif path == '/001':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            if len(command001) > 1:
                self.wfile.write(command001.pop())
            else:
                self.wfile.write(command001[0])

        elif path == '/002':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            if len(command002) > 1:
                self.wfile.write(command002.pop())
            else:
                self.wfile.write(command002[0])

        elif path == '/003':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            if len(command003) > 1:
                self.wfile.write(command003.pop())
            else:
                self.wfile.write(command003[0])

        elif path == '/forward01':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            command001.append(b'forward()')
            self.wfile.write(b'forward ok')

        elif path == '/back01':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            command001.append(b'back()')
            self.wfile.write(b'lefbackt ok')

        elif path == '/left01':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            command001.append(b'left()')
            self.wfile.write(b'left ok')

        elif path == '/right01':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            command001.append(b'right()')
            self.wfile.write(b'right ok')

        elif path == '/forward02':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            command002.append(b'forward()')
            self.wfile.write(b'forward ok')

        elif path == '/back02':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            command002.append(b'back()')
            self.wfile.write(b'lefbackt ok')

        elif path == '/left02':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            command002.append(b'left()')
            self.wfile.write(b'left ok')

        elif path == '/right02':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            command002.append(b'right()')
            self.wfile.write(b'right ok')

        elif path == '/forward03':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            command002.append(b'forward()')
            self.wfile.write(b'forward ok')

        elif path == '/back03':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            command002.append(b'back()')
            self.wfile.write(b'back ok')

        elif path == '/left03':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            command002.append(b'left()')
            self.wfile.write(b'left ok')

        elif path == '/right03':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            command002.append(b'right()')
            self.wfile.write(b'right ok')

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404 Not Found')

    def log_message(self, format, *args):
        message = format % args
        print(f'Подключение: {self.client_address[0]} - {message}')


server_address = ('', 8000)
httpd = socketserver.ThreadingTCPServer(server_address, MyHandler)
httpd.serve_forever()
