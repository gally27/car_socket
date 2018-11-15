# coding=utf-8
import socket


def handle_request(conn):
    conn.send("server: hello, let's start ")
    flag = True
    while flag:
        data = conn.recv(1024)
        if data == 'exit':
            flag = False
        else:
            conn.sendall(data)

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('192.168.1.1', 8091))  # 设定ip(或者域名)和端口号
    sock.listen(2)  # 设置最大并发数

    while 1:
        conn, address = sock.accept()  # 接收请求
        print address,
        handle_request(conn)  # 处理请求
        conn.close()  # 关闭连接


if __name__ == '__main__':
    main()
