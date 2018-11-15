# coding=utf-8
import socket


def handle_request(client):
    buf = client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n")      # 此句允许浏览器访问
    client.send("Hello, qifangpi************ ")                  # 发送要显示的内容


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('172.20.191.3', 9999))              # 设定ip(或者域名)和端口号
    sock.listen(2)                              # 设置最大并发数

    while 1:
        conn, address = sock.accept()   # 接收请求
        handle_request(conn)            # 处理请求
        conn.close()                    # 关闭连接


if __name__ == '__main__':
    main()
