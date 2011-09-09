import socket, SocketServer

port = 8000
local_hostname = socket.gethostname()
print local_hostname
server_address = (socket.gethostbyname(local_hostname), port)
print server_address
