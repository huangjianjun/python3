#!/usr/bin/env python3.5
# coding = utf-8
# created by huang jian jun


# TCP client
import socket
# 建立一个TCP连接套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 注意参数是一个tuple，包含地址和端口号。
s.connect(('www.sina.com.cn', 80))

# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接受数据
buffer = []
while True:
    d = s.recv(1024) # 指定每次接受的最大字节数
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
# 关闭本次TCP连接
s.close()
# 接收到的数据包括HTTP头和网页本身，
# 我们只需要把HTTP头和网页分离一下，
# 把HTTP头打印出来，网页内容保存到文件：

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)

# TCP server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
server.bind(('127.0.0.1', 9999))
server.listen(10)
print('Waiting for connection...')
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

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





