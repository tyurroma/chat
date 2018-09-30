import socket
import threading


def accept_client():
    while True:
        # Принимаем подключение с помощью метода accept, который возвращает кортеж с двумя элементами:
        # новый сокет (client_socket) и адрес клиента. Именно этот сокет и будет использоваться для приема
        # и посылке клиенту данных.
        (client_socket, client_address) = server_socket.accept()

        connection_list.append(client_socket)
        thread_client = threading.Thread(target=broadcast_message, args=[client_socket])
        thread_client.start()


def broadcast_message(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if data:
                check_user(client_socket, data)
        except KeyboardInterrupt:
            client_socket.close()
            break


def check_user(client_socket, message):
    for client in connection_list:
        if client != client_socket:
            client.send(message)


if __name__ == "__main__":
    connection_list = []

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = "localhost"
    port = 50001
    server_socket.bind((host, port))

    server_socket.listen(1)
    print("Chat server started on port: " + str(port))

    thread_ac = threading.Thread(target=accept_client)
    thread_ac.start()
