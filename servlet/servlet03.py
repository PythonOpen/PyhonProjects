# 模拟服务器的函数
import socket

def tcp_srv():
    # 1.建立socket
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2.绑定端口和地址
    addr=("127.0.0.1",8998)
    sock.bind(addr)
    # 3.监听接入的访问socket
    sock.listen()

    while True:
        # 4.接受访问的socket
        skt,addr=sock.accept()
        # 5.接受访问的发送内容，进行解码
        msg=skt.recv(500)
        msg=msg.decode()

        rst="Received msg: {0} from{1}".format(msg,addr)
        print(rst)
        # 6.如果有必要，给对方发送反馈信息
        skt.send(rst.encode())

        #7.关闭链接通路
        skt.close()


if __name__ == '__main__':
    print("Starting servlet......")
    tcp_srv()
    print("Ending servlet......")


