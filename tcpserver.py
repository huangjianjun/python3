#!/usr/bin/env python3.5
# coding = utf-8
# created by huang jian jun

import socket, threading,time
# TCP server
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
server.bind(('127.0.0.1', 9999))
server.listen(10)
print('Waiting for connection...')
while True:
    # 接受一个新连接:
    sock, addr = server.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()



