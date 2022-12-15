# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.sendFile("index.html", "Site does not yet have an index.html file.")
        else:
            self.sendFile(self.path[1:])    # remove the leading '/' before using the path

    def sendFile(self, filename, errorMessage=None):
        try:
            with open(filename, 'r') as requestedPageFile:
                self.send_response(200)
                self.send_header("Access-Control-Allow-Headers", "*")
                self.send_header("Cache-Control", "max-age=3600")
                self.send_header("Content-Length:", "0")
                self.send_header("Date", "Thu, 15 Dec 2022 9:53:00 EST")
                # self.date_time_string()
                self.send_header("Last-Modified:", "Thu, 15 Dec 2022 9:53:00 EST")
                self.send_header("Vary", "*")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Connection", "")
                self.send_header("Content-type:", "text/html")
                self.send_header("Expires", "Thu, 19 May 2023 12:00:00 EST")
                self.send_header("Server", "BaseHTTP/0.6 Python/3.10.6")
                self.send.header("X-Cache", "deny")
                self.end_headers()
                for line in requestedPageFile.readlines():
                    self.wfile.write(bytes(line.strip(), "utf-8"))
        except FileNotFoundError:
            print("No index.html file exist.")
            self.send_error(404, errorMessage)
            self.send_header("Content-type", "text/html")
            self.end_headers()


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://{0}:{1}".format(hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

    # Handler.client_address¶
