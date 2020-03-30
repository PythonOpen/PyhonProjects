# 模拟服务器的函数
import socket

def clientFunc():

    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    text="I love fangfang"

    # 发送的东西数据必须是bytes格式
    data=text.encode()

    # 发送
    sock.sendto(data,("127.0.0.1",7852))

    data,addr=sock.recvfrom(200)
    text=data.decode()
    print(text)

if __name__ == '__main__':
    print("Starting client......")
    clientFunc()
    print("Ending client")


