#!/usr/bin/env python
__author__ = "Arana Fireheart"
import socket

PORTNUMBER = 8080
URL = "localhost"
page = "page1.htm"

headers = [
             f"Accept-Language: en-us\r\n",
             f"Accept-Encoding: gzip, deflate\r\n",
             f"Forwarded: for = {socket.gethostbyname(URL)};proto=http\r\n",
             f"From: megan.deans@snhu.edu\r\n",
             f"Host: {URL}\r\n",
             f"Cookie: Megan Deans \r\n",
             f"Referer: https://www.google.com\r\n",
             f"Connection: Keep-Alive"
           ]
headerData = "".join(headers)
httpRequest = f"GET https://{URL}/{page} \r\n"
commandData = f"{httpRequest}{headerData}"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as webSocket:
    try:
        webSocket.connect(("data.pr4e.org", PORTNUMBER))
        command = commandData.encode()
        webSocket.send(command)
    except socket.error as exc:
        print(f"A socket error has occurred : {exc}")

    data = ' '
    while len(data) > 0:
        data = webSocket.recv(512)
        print(data.decode(), end='')

