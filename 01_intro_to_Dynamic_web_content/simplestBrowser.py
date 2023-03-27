import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("127.0.0.1", 9000))
cmd = "GET http://127.0.0.1:9000 HTTP/1.0\r\n\r\n".encode()
#                                                  place to put header 
mysock.send(cmd)

count = 0
while True:
    count = count + 1
    data =mysock.recv(512)
    if len(data) < 1 :break
    print(data.decode(), end='')

mysock.close()
print("count of how many times we calls", count)


# HTTP/1.1 200 OK
# Date: Mon, 27 Mar 2023 19:54:35 GMT
# Server: Apache/2.4.18 (Ubuntu)
# Last-Modified: Mon, 15 May 2017 11:11:47 GMT
# ETag: "80-54f8e1f004857"
# Accept-Ranges: bytes
# Content-Length: 128
# Cache-Control: max-age=0, no-cache, no-store, must-revalidate
# Pragma: no-cache
# Expires: Wed, 11 Jan 1984 05:00:00 GMT
# Connection: close
# Content-Type: text/html

# <h1>The First Page</h1>
# <p>
# If you like, you can switch to the 
# <a href="http://data.pr4e.org/page2.htm">
# Second Page</a>.
# </p>