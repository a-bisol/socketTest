import socket
import threading

HOST = '192.168.2.46'
PORT = 60000


def handle_message(connection):
    while True:
        try:
            msg = connection.recv(1024)

            if msg:
                print(msg.decode('utf-8'))
            else:
                connection.close()
                break

        except Exception as e:
            print(f'Error handling message from server: {e}')
            connection.close()
            break


def client():
    try:
        socket_inst = socket.socket()
        socket_inst.connect((HOST, PORT))
        threading.Thread(target=handle_message, args=([socket_inst])).start()

        print('Connected to server')

        while True:
            msg = input()
            if msg == 'quit':
                break

            socket_inst.send(msg.encode('utf-8'))

        socket_inst.close()

    except Exception as e:
        print(f'Error connecting to server socket {e}')
        socket_inst.close()


if __name__ == '__main__':
    client()
