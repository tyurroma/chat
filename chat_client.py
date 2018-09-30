import socket
import threading


def send(user_name, client_socket):
    while True:
        message = input("Me: ")
        data = user_name + ">" + message
        try:
            client_socket.send(data.encode("utf-8"))
        except BrokenPipeError:
            break


def receive(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            print('\t' + data.decode())
        except BlockingIOError:
            continue


if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = "localhost"
    port = 50001

    user_name = input("Enter your nickname: ")
    client_socket.connect((host, port))
    client_socket.setblocking(False)
    print("Connected to remote host...")

    thread_send = threading.Thread(target=send, args=[user_name, client_socket])
    thread_send.start()

    thread_receive = threading.Thread(target=receive, args=[client_socket])
    thread_receive.start()
